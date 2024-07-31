from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import common, bundle
from app.core.db_config import get_db
from app.services.bundle import bundle_service
from app.services.auth import auth_service
from app.core.security import security
from app.models.models import User

bundle_router = APIRouter(
    prefix="/bundle",
    tags=["Bundles"]
)


@bundle_router.post(
    path="/",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN', 'USER'])
async def create(
    bundle_data: bundle.AddRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> common.GeneralResponse:
    return await bundle_service.add(bundle_data=bundle_data, db=db, user_id=current_user.id)


@bundle_router.get(
    path="/",
    response_model=bundle.GetAllBundleResponse,
    status_code=200
)
@security.authorize(roles=['ADMIN', 'USER'])
async def get_all(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> bundle.GetAllBundleResponse:
    return await bundle_service.get_all(user_id=current_user.id, db=db)


@bundle_router.get(
    path="/{bundle_id}",
    response_model=bundle.GetBundleResponse,
    status_code=200
)
@security.authorize(roles=['ADMIN', 'USER'])
async def get_by_id(
    bundle_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> bundle.GetBundleResponse:
    return await bundle_service.get_by_id(bundle_id, db=db, user_id=current_user.id)


@bundle_router.delete(
    path="/{bundle_id}",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN', 'USER'])
async def delete_by_id(
    bundle_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> common.GeneralResponse:
    return await bundle_service.delete_by_id(bundle_id=bundle_id, db=db, user_id=current_user.id)


@bundle_router.put(
    path="/{bundle_id}",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN', 'USER'])
async def update(
    bundle_id: str,
    update_data: bundle.AlterRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> common.GeneralResponse:
    return await bundle_service.update(bundle_id=bundle_id, db=db, user_id=current_user.id, update_data=update_data)


@bundle_router.get(
    path="/{bundle_url}",
    response_model=bundle.GetBundleResponse,
    status_code=200
)
async def get_by_url(
    public_url: str,
    db: AsyncSession = Depends(get_db),
) -> bundle.GetBundleResponse:
    return await bundle_service.get_by_url(db=db, public_url=public_url)
