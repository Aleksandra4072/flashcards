from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from loguru import logger


from app.models.models import User, Role
from app.schemas import auth
from app.core.security import security


class _CrudUser:
    @staticmethod
    async def get_by_email(
        db: AsyncSession,
        email: str
    ) -> User:
        logger.info('Retrieving User by email...')
        stmt = select(User).where(User.email == email)
        result = await db.execute(stmt)
        user = result.scalars().first()

        return user

    @staticmethod
    async def sign_up(
        db: AsyncSession,
        user: auth.SignupRequest
    ) -> User:
        logger.info('Creating new user')
        hashed_password = security.hash_password(user.password)

        new_user = User(
            email=user.email,
            password=hashed_password
        )
        role = await db.execute(select(Role).where(Role.name == 'USER'))
        new_user.roles = role.scalars().all()
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user


crud_user = _CrudUser()
