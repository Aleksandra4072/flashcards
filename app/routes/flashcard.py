from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import common, flashcard
from app.core.db_config import get_db
from app.services.bundle import bundle_service
from app.services.auth import auth_service
from app.services.flashcard import flashcard_service
from app.core.security import security
from app.models.models import User

flashcard_router = APIRouter(
    prefix="/flashcard",
    tags=["Flashcards"]
)


@flashcard_router.get(
    path="/bundle/{bundle_id}",
    response_model=flashcard.GetAllFlashcardsResponse,
    status_code=200
)
async def get_all(
    bundle_id: str,
    db: AsyncSession = Depends(get_db)
) -> flashcard.GetAllFlashcardsResponse:
    return await flashcard_service.get_all(db=db, bundle_id=bundle_id)


@flashcard_router.get(
    path="/{flashcard_id}",
    response_model=flashcard.GetFlashcardResponse,
    status_code=200
)
async def get_by_id(
    flashcard_id: str,
    db: AsyncSession = Depends(get_db)
) -> flashcard.GetFlashcardResponse:
    fetch_flashcard = await flashcard_service.get_by_id(db=db, flashcard_id=flashcard_id)
    return flashcard.GetFlashcardResponse(flashcard=fetch_flashcard)


@flashcard_router.post(
    path="/",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN', 'USER'])
async def create(
    flashcard_data: flashcard.AddRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> common.GeneralResponse:
    await bundle_service.is_bundle_owner(
        db=db,
        user_id=current_user.id,
        bundle_id=flashcard_data.bundle_id
    )
    return await flashcard_service.add(flashcard_data=flashcard_data, db=db)


@flashcard_router.delete(
    path="/{flashcard_id}",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN', 'USER'])
async def delete_by_id(
    flashcard_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> common.GeneralResponse:
    return await flashcard_service.delete_by_id(flashcard_id=flashcard_id, db=db, user_id=current_user.id)


@flashcard_router.put(
    path="/{flashcard_id}",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN', 'USER'])
async def update(
    update_data: flashcard.AlterRequest,
    flashcard_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_service.get_current_user)
) -> common.GeneralResponse:
    return await flashcard_service.update(update_data=update_data, db=db, flashcard_id=flashcard_id, user_id=current_user.id)
