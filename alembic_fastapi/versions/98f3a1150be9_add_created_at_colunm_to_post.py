"""add created at colunm to post

Revision ID: 98f3a1150be9
Revises: e4c20c5ddd60
Create Date: 2025-12-13 19:45:32.733975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98f3a1150be9'
down_revision: Union[str, Sequence[str], None] = 'e4c20c5ddd60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column("posts" , sa.Column("published" , sa.Boolean() , nullable=False , server_default="True"))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts" , "published")
