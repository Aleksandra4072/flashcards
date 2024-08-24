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
    prefix="/user",
    tags=["Users"]
)


@flashcard_router.get(
    path="/",
    response_model=common.GeneralResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN'])
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
