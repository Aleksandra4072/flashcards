from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import Uuid, delete
from loguru import logger

from app.models.models import Flashcard
from app.schemas import flashcard
from app.core.error_handler import Error404


class _CrudFlashcard:
    @staticmethod
    async def add(
        db: AsyncSession,
        flashcard_data: flashcard.AddRequest,
        bundle_id: Uuid
    ) -> Flashcard:
        new_flashcard = Flashcard(
            term=flashcard_data.term,
            description=flashcard_data.description,
            bundle_id=bundle_id
        )
        db.add(new_flashcard)
        await db.commit()
        await db.refresh(new_flashcard)
        return new_flashcard

    @staticmethod
    async def get_all_by_bundle(db: AsyncSession, bundle_id: Uuid) -> list[Flashcard]:
        logger.info("Fetching all the flashcards of the bundle")
        stmt = select(Flashcard).where(Flashcard.bundle_id == bundle_id)
        result = await db.execute(stmt)
        flashcards = result.scalars().all()
        if not flashcards or len(flashcards) == 0:
            return []
        return flashcards

    @staticmethod
    async def get_by_id(db: AsyncSession, flashcard_id: Uuid) -> Flashcard:
        logger.info("Fetching flashcard by id")
        stmt = select(Flashcard).where(Flashcard.id == flashcard_id)
        result = await db.execute(stmt)
        fetch_flashcard = result.scalars().first()
        if not fetch_flashcard:
            raise Error404(details="Flashcard does not exist")

        return fetch_flashcard

    @staticmethod
    async def delete_by_id(db: AsyncSession, flashcard_id: Uuid) -> bool:
        await db.execute(delete(Flashcard).where(Flashcard.id == flashcard_id))
        await db.commit()

        return True

    @staticmethod
    async def update(
        db: AsyncSession,
        update_data: flashcard.AlterRequest,
        update_flashcard: Flashcard
    ):
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(update_flashcard, key, value)
        await db.commit()
        await db.refresh(update_flashcard)

        return True


crud_flashcard = _CrudFlashcard()
