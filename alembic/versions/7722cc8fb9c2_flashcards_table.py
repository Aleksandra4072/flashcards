"""flashcards table

Revision ID: 7722cc8fb9c2
Revises: 731da6debb51
Create Date: 2024-07-29 15:59:46.888389

"""
from typing import Sequence, Union
from alembic import op
from loguru import logger
from sqlalchemy import Column, VARCHAR, UUID, TIMESTAMP, BOOLEAN, text
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7722cc8fb9c2'
down_revision: Union[str, None] = '731da6debb51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "flashcards",
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")),
        Column("term", VARCHAR(255), unique=False, nullable=False),
        Column("description", VARCHAR(1000), nullable=True),

        Column("bundle_id", UUID(as_uuid=True), sa.ForeignKey('bundles.id'), nullable=False),
    )
    logger.info("Upgrade: table 'flashcards' created")


def downgrade() -> None:
    op.drop_table("flashcards")
    logger.info("Downgrade: table 'flashcards' deleted")
