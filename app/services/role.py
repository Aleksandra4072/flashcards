from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import role
from app.crud.role import crud_role


class _RoleService:
    @staticmethod
    async def get_all(
        db: AsyncSession
    ) -> role.GetAllRolesResponse :
        roles = await crud_role.get_all(db=db)
        result = [role.GetRoleResponseItem.from_orm(r) for r in roles]
        return role.GetAllRolesResponse(roles=result)


role_service = _RoleService()
