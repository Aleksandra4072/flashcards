import jwt
from fastapi import Response, Request, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from loguru import logger
from functools import wraps

from app.schemas import auth, common
from app.crud.user import crud_user
from app.core.error_handler import Error400, Error401, Error403
from app.core.security import security
from app.core.env_settings import settings
from app.core.db_config import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


class _AuthService:
    @staticmethod
    async def signup(
        user_details: auth.SignupRequest,
        db: AsyncSession
    ) -> common.GeneralResponse:
        if await crud_user.get_by_email(db=db, email=user_details.email):
            raise Error400(details="Email already registered")

        if not await crud_user.sign_up(db=db, user=user_details):
            raise Error400(details="Something went wrong")

        return common.GeneralResponse(
            message="Signup successful"
        )

    @staticmethod
    async def login(
            response: Response,
            credentials: auth.LoginRequest,
            db: AsyncSession
    ) -> auth.LoginResponse:
        user = await crud_user.get_by_email(db=db, email=credentials.email)

        if not user or not security.verify_pass(
                plain_password=credentials.password,
                hashed_password=user.password
        ):
            raise Error401(details="Wrong credentials")

        roles = [role.name for role in user.roles]
        access_token = security.create_access_token(
            data={'email': user.email, 'roles': roles}
        )

        refresh_token = security.create_refresh_token(
            data={'email': user.email},
            expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        )
        logger.info('Setting refresh token')
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)

        return auth.LoginResponse(
            access_token=access_token
        )

    @staticmethod
    async def refresh_token(
            request: Request,
            db: AsyncSession
    ) -> auth.LoginResponse:
        refresh_token = request.cookies.get('refresh_token')
        if not refresh_token:
            raise Error401(details="Refresh token not found")

        try:
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            email: str = payload.get("email")
            if email is None:
                raise Error401(details="Payload is empty")
        except jwt.ExpiredSignatureError:
            raise Error401(details="Expired token")
        except jwt.InvalidTokenError:
            raise Error401(details="Invalid token")

        user = await crud_user.get_by_email(db=db, email=email)
        roles = [role.name for role in user.roles]
        access_token = security.create_access_token(
            data={'email': user.email, 'roles': roles}
        )

        return auth.LoginResponse(
            access_token=access_token
        )

    @staticmethod
    async def logout(response: Response) -> common.GeneralResponse:
        response.delete_cookie(key="refresh_token")
        return common.GeneralResponse(message="Logged Out")

    @staticmethod
    async def decode_token(token: str):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return {"token_payload": payload}
        except jwt.ExpiredSignatureError:
            raise Error401(details="Token is expired")
        except jwt.PyJWTError:
            raise Error401(details="Token is invalid")

    @staticmethod
    async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
        credentials_exception = Error401(details="Could not validate credentials")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            email: str = payload.get("email")
            if email is None:
                raise credentials_exception
        except jwt.ExpiredSignatureError:
            raise Error401(details="Token is expired")
        user = await crud_user.get_by_email(db, email=email)
        if user is None:
            raise credentials_exception
        return user

    @staticmethod
    def authorize(role: list):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                user_role = kwargs.get("current_user")['role']
                if user_role not in role:
                    raise Error403
                return await func(*args, **kwargs)
            return wrapper
        return decorator


auth_service = _AuthService()
