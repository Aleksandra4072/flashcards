from fastapi import APIRouter, Depends, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.sevices.auth import auth_service
from app.schemas import auth
from app.schemas import common
from app.core.db_config import get_db

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@auth_router.post(
    path="/signup",
    response_model=common.GeneralResponse,
    status_code=201
)
async def signup(
    user_details: auth.SignupRequest,
    db: AsyncSession = Depends(get_db)
) -> common.GeneralResponse:
    return await auth_service.signup(user_details=user_details, db=db)


@auth_router.post(
    path="/login",
    response_model=auth.LoginResponse,
    status_code=200
)
async def login(
    response: Response,
    credentials: auth.LoginRequest,
    db: AsyncSession = Depends(get_db)
) -> auth.LoginResponse:
    return await auth_service.login(credentials=credentials, response=response, db=db)


@auth_router.post(path="/token", response_model=auth.LoginResponse)
async def get_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
) -> auth.LoginResponse:
    credentials = auth.LoginRequest(email=form_data.username, password=form_data.password)
    return await auth_service.login(credentials=credentials, response=response, db=db)


@auth_router.get(
    path="/refresh_token",
    response_model=auth.LoginResponse,
    status_code=200
)
async def refresh_token(
    request: Request,
    db: AsyncSession = Depends(get_db)
) -> auth.LoginResponse:
    return await auth_service.refresh_token(request=request, db=db)


@auth_router.post(
    path="/logout",
    response_model=common.GeneralResponse,
    status_code=201
)
async def logout(
    response: Response
) -> common.GeneralResponse:
    return await auth_service.logout(response=response)


@auth_router.post(
    path="/decode_token",
    status_code=200
)
async def decode_token(
    token: str = Depends(oauth2_scheme)
):
    return await auth_service.decode_token(token=token)
