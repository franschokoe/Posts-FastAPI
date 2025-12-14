"""published

Revision ID: 5715d0d2fc07
Revises: c17a81af4c1f
Create Date: 2025-12-14 00:19:53.854974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5715d0d2fc07'
down_revision: Union[str, Sequence[str], None] = 'c17a81af4c1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts" , sa.Column("published" , sa.Boolean() , nullable=False , server_default="True"))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts" , "published")
