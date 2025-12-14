"""create post table

Revision ID: e4c20c5ddd60
Revises: 
Create Date: 2025-12-12 22:21:43.215246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4c20c5ddd60'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts" , sa.Column("id" , sa.Integer() , nullable=False , primary_key=True) , 
                    sa.Column("title" , sa.String() , nullable=False),
                    sa.Column("content" , sa.String() , nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
