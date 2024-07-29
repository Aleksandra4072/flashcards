"""bundles table

Revision ID: 731da6debb51
Revises: 8c026da732e1
Create Date: 2024-07-29 15:59:40.389098

"""
from typing import Sequence, Union
from alembic import op
from loguru import logger
from sqlalchemy import Column, VARCHAR, UUID, TIMESTAMP, text
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '731da6debb51'
down_revision: Union[str, None] = '8c026da732e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bundles",
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")),
        Column("title", VARCHAR(255), unique=False, nullable=False),
        Column("description", VARCHAR(1000), nullable=True),
        Column("last_revised", TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow),
        Column("public_url", VARCHAR(255), nullable=False, server_default=text("gen_random_uuid()")),

        Column("user_id", UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
    )
    logger.info("Upgrade: table 'bundles' created")


def downgrade() -> None:
    op.drop_table("bundles")
    logger.info("Downgrade: table 'bundles' deleted")
