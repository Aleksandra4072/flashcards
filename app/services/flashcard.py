import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from app.schemas import flashcard, common
from app.crud.flashcard import crud_flashcard
from app.core.error_handler import Error400, Error404
from app.models.models import Flashcard
from app.services.bundle import bundle_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


class _FlashcardService:
    @staticmethod
    async def get_all(
        bundle_id: str,
        db: AsyncSession
    ) -> flashcard.GetAllFlashcardsResponse:
        flashcards = await crud_flashcard.get_all_by_bundle(db=db, bundle_id=uuid.UUID(bundle_id))
        result = [flashcard.GetFlashcardResponseItem.from_orm(f) for f in flashcards]
        return flashcard.GetAllFlashcardsResponse(flashcards=result)

    @staticmethod
    async def get_by_id(
        flashcard_id: str,
        db: AsyncSession
    ) -> Flashcard:
        result = await crud_flashcard.get_by_id(db=db, flashcard_id=uuid.UUID(flashcard_id))
        if not result:
            raise Error400(detail="Could not get the flashcard")

        return result

    @staticmethod
    async def add(
        flashcard_data: flashcard.AddRequest,
        db: AsyncSession
    ) -> common.GeneralResponse:
        if not await crud_flashcard.add(
                db=db,
                flashcard_data=flashcard_data,
                bundle_id=uuid.UUID(flashcard_data.bundle_id)
        ):
            raise Error400(detail="Could not add a flashcard")

        return common.GeneralResponse(
            message="Flashcard was added successfully"
        )

    @staticmethod
    async def delete_by_id(
        user_id: uuid,
        flashcard_id: str,
        db: AsyncSession
    ) -> common.GeneralResponse:
        delete_flashcard = await crud_flashcard.get_by_id(db=db, flashcard_id=uuid.UUID(flashcard_id))
        await bundle_service.is_bundle_owner(
            db=db,
            user_id=user_id,
            bundle_id=str(delete_flashcard.bundle_id)
        )
        is_deleted = await crud_flashcard.delete_by_id(db=db, flashcard_id=uuid.UUID(flashcard_id))
        if not is_deleted:
            Error404(detail="Could not find the flashcard")

        return common.GeneralResponse(message="Flashcard was deleted successfully")

    @staticmethod
    async def update(
        user_id: uuid,
        flashcard_id: str,
        update_data: flashcard.AlterRequest,
        db: AsyncSession
    ) -> common.GeneralResponse:
        update_flashcard = await crud_flashcard.get_by_id(db=db, flashcard_id=uuid.UUID(flashcard_id))
        await bundle_service.is_bundle_owner(
            db=db,
            user_id=user_id,
            bundle_id=str(update_flashcard.bundle_id)
        )

        if not await crud_flashcard.update(db=db, update_data=update_data, update_flashcard=update_flashcard):
            raise Error400(detail="Could not alter bundle")

        return common.GeneralResponse(message="Bundle was altered")


flashcard_service = _FlashcardService()
