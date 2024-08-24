from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import role
from app.core.db_config import get_db
from app.services.auth import auth_service
from app.services.role import role_service
from app.core.security import security
from app.models.models import User

flashcard_router = APIRouter(
    prefix="/role",
    tags=["Roles"]
)


@flashcard_router.get(
    path="/",
    response_model=role.GetAllRolesResponse,
    status_code=201
)
@security.authorize(roles=['ADMIN'])
async def get_all(
    db: AsyncSession = Depends(get_db),
    # current_user: User = Depends(auth_service.get_current_user)
) -> role.GetAllRolesResponse:
    return await role_service.get_all(db=db)
