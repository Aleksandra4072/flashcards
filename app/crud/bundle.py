from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from sqlalchemy import Uuid, delete
from loguru import logger

from app.models.models import Bundle, Flashcard
from app.schemas import bundle
from app.core.error_handler import Error400, Error403


class _CrudBundle:
    @staticmethod
    async def add(
        db: AsyncSession,
        bundle_data: bundle.AddRequest,
        user_id: Uuid
    ) -> Bundle:
        new_bundle = Bundle(
            title=bundle_data.title,
            description=bundle_data.description,
            user_id=user_id

        )
        db.add(new_bundle)
        await db.commit()
        await db.refresh(new_bundle)
        return new_bundle

    @staticmethod
    async def get_all_by_user(db: AsyncSession, user_id: Uuid) -> list[Bundle]:
        logger.info("Fetching all the bundles of the current user")
        stmt = select(Bundle).where(Bundle.user_id == user_id)
        result = await db.execute(stmt)
        bundles = result.scalars().all()
        if not bundles or len(bundles) == 0:
            return []
        return bundles

    @staticmethod
    async def get_by_id(db: AsyncSession, bundle_id: Uuid, user_id: Uuid) -> Bundle:
        logger.info("Fetching bundle by id")
        stmt = select(Bundle).where(Bundle.id == bundle_id)
        result = await db.execute(stmt)
        fetch_bundle = result.scalars().first()
        if fetch_bundle:
            if fetch_bundle.user_id != user_id:
                raise Error400(details="This bundle does not belong to the current user")
            return fetch_bundle
        raise Error400(details="Such bundle does not exist")

    @staticmethod
    async def delete_by_id(db: AsyncSession, bundle_id: Uuid, user_id: Uuid) -> bool:
        await db.execute(delete(Flashcard).where(Flashcard.bundle_id == bundle_id))

        await db.execute(delete(Bundle).where(Bundle.id == bundle_id, Bundle.user_id == user_id))

        await db.commit()

        logger.info('Bundle and all the associated flashcards have been deleted')
        return True


crud_bundle = _CrudBundle()
