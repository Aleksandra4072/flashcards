from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.models import Role


class _CrudRole:
    @staticmethod
    async def get_all(
        db: AsyncSession
    ):
        stmt = select(Role)
        result = await db.execute(stmt)
        roles = result.scalars().all()
        if not roles or len(roles) == 0:
            return []
        return roles


crud_role = _CrudRole()