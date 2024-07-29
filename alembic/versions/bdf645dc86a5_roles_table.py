"""roles table

Revision ID: bdf645dc86a5
Revises: 242fc811a36f
Create Date: 2024-07-29 15:58:17.252133

"""
from typing import Sequence, Union
from alembic import op
from sqlalchemy import Column, VARCHAR, UUID, func
import sqlalchemy as sa
from loguru import logger


# revision identifiers, used by Alembic.
revision: str = 'bdf645dc86a5'
down_revision: Union[str, None] = '242fc811a36f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "roles",
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        Column("name", VARCHAR(255), unique=True, nullable=False)
    )
    logger.info("Upgrade: table 'roles' created")


def downgrade() -> None:
    op.drop_table("roles")
    logger.info("Downgrade: table 'roles' deleted")
