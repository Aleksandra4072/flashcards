"""users table

Revision ID: 242fc811a36f
Revises: 
Create Date: 2024-07-29 15:58:05.055909

"""
from typing import Sequence, Union
from loguru import logger
from alembic import op
from sqlalchemy import Column, VARCHAR, INTEGER, UUID, TIMESTAMP, BOOLEAN, text



# revision identifiers, used by Alembic.
revision: str = '242fc811a36f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")),
        Column("email", VARCHAR(255), unique=True, nullable=False),
        Column("password", VARCHAR(255), nullable=False),
        Column("age", INTEGER, nullable=True),
        Column("created_at", TIMESTAMP(timezone=True), nullable=False),
        Column("updated_at", TIMESTAMP(timezone=True), nullable=True),
        Column("is_activated", BOOLEAN, nullable=False, default=False),
        Column("path", VARCHAR(255), nullable=False),
    )
    logger.info("Upgrade: table 'users' created")


def downgrade() -> None:
    op.drop_table("users")
    logger.info("Downgrade: table 'users' deleted")
