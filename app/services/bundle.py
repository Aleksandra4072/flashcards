import uuid
from sqlalchemy import Uuid
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import bundle, common
from app.crud.bundle import crud_bundle
from app.core.error_handler import Error400, Error404


class _BundleService:
    @staticmethod
    async def add(
        bundle_data: bundle.AddRequest,
        user_id: Uuid,
        db: AsyncSession
    ) -> common.GeneralResponse:
        if not await crud_bundle.add(db=db, bundle_data=bundle_data, user_id=user_id):
            raise Error400(detail="Could not add a bundle")

        return common.GeneralResponse(
            message="Bundle was added successfully"
        )

    @staticmethod
    async def get_all(
        user_id: Uuid,
        db: AsyncSession
    ) -> bundle.GetAllBundleResponse:
        bundles = await crud_bundle.get_all_by_user(db=db, user_id=user_id)
        result = [bundle.GetBundleResponseItem.from_orm(b) for b in bundles]
        return bundle.GetAllBundleResponse(bundles=result)

    @staticmethod
    async def get_by_id(
        bundle_id: str,
        user_id: Uuid,
        db: AsyncSession
    ) -> bundle.GetBundleResponse:
        result = await crud_bundle.get_by_id(db=db, bundle_id=uuid.UUID(bundle_id), user_id=user_id)
        if not result:
            raise Error400(detail="Could not get the bundle")

        return bundle.GetBundleResponse(bundle=result)

    @staticmethod
    async def delete_by_id(
        bundle_id: str,
        user_id: Uuid,
        db: AsyncSession
    ) -> common.GeneralResponse:
        delete_bundle = await crud_bundle.get_by_id(db=db, bundle_id=bundle_id, user_id=user_id)
        if not delete_bundle:
            Error404(detail="Could not find the bundle")

        if not await crud_bundle.delete_by_id(db=db, bundle_id=uuid.UUID(bundle_id), user_id=user_id):
            raise Error400(detail="Could not delete bundle")

        return common.GeneralResponse(message="Bundle was deleted successfully")

    @staticmethod
    async def update(
        bundle_id: str,
        update_data: bundle.AlterRequest,
        user_id: Uuid,
        db: AsyncSession
    ) -> common.GeneralResponse:
        update_bundle = await crud_bundle.get_by_id(db=db, bundle_id=uuid.UUID(bundle_id), user_id=user_id)
        if not update_bundle:
            Error404(detail="Could not find the bundle")

        if not await crud_bundle.update(db=db, update_data=update_data, update_bundle=update_bundle):
            raise Error400(detail="Could not alter bundle")

        return common.GeneralResponse(message="Bundle was altered")

    @staticmethod
    async def is_bundle_owner(
        bundle_id: str,
        user_id: Uuid,
        db: AsyncSession
    ) -> bool:
        update_bundle = await crud_bundle.get_by_id(db=db, bundle_id=uuid.UUID(bundle_id), user_id=user_id)
        if not update_bundle:
            Error404(detail="Could not find the bundle")

        return True

    @staticmethod
    async def get_by_url(
        public_ulr: str,
        db: AsyncSession
    ) -> bundle.GetBundleResponse:
        result = await crud_bundle.get_by_url(db=db, public_url=public_ulr)
        if not result:
            raise Error400(detail="Could not get the bundle")

        return bundle.GetBundleResponse(bundle=result)


bundle_service = _BundleService()
