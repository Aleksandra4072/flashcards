"""initial roles

Revision ID: c90c96338ce4
Revises: 7722cc8fb9c2
Create Date: 2024-07-29 15:59:58.543924

"""
from typing import Sequence, Union
from alembic import op
from sqlalchemy import String, Uuid
from sqlalchemy.sql import table, column
from loguru import logger


# revision identifiers, used by Alembic.
revision: str = 'c90c96338ce4'
down_revision: Union[str, None] = '7722cc8fb9c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    roles_table = table(
        "roles",
        column("id", Uuid),
        column("name", String)
    )

    op.bulk_insert(
        roles_table,
        [
            {
                "name": "ADMIN"
            },
            {
                "name": "USER"
            }
        ],
    )

    logger.info("ADMIN and USER roles created")


def downgrade() -> None:
    op.execute("DELETE FROM roles")
    logger.info("ADMIN and USER roles created")

