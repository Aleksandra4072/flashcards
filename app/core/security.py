import jwt
from typing import Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta
from functools import wraps
from typing import List

from app.core.env_settings import settings
from app.core.error_handler import CustomError
from app.models.models import User

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class _Security:
    @staticmethod
    def verify_pass(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def authorize(roles: List[str]):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                current_user: User = kwargs.get("current_user")
                if not current_user:
                    raise CustomError(status_code=401, message="Not authenticated")

                user_roles = [role.name for role in current_user.roles]
                if not any(role in user_roles for role in roles):
                    raise CustomError(status_code=403, message="User is not authorized to access")

                return await func(*args, **kwargs)

            return wrapper

        return decorator


security = _Security()
