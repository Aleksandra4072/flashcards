"""user_role table

Revision ID: 8c026da732e1
Revises: bdf645dc86a5
Create Date: 2024-07-29 15:59:14.722336

"""
import sqlalchemy as sa
from typing import Sequence, Union
from alembic import op
from sqlalchemy import Column, UUID
from loguru import logger


# revision identifiers, used by Alembic.
revision: str = '8c026da732e1'
down_revision: Union[str, None] = 'bdf645dc86a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_role",
        Column("user_id", UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        Column("role_id", UUID(as_uuid=True), sa.ForeignKey('roles.id'), nullable=False)
    )
    logger.info("Upgrade: table 'user_role' created")


def downgrade() -> None:
    op.drop_table("user_role")
    logger.info("Downgrade: table 'user_role' deleted")
