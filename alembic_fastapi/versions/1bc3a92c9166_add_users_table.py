"""add users table

Revision ID: 1bc3a92c9166
Revises: 98f3a1150be9
Create Date: 2025-12-13 20:02:32.929184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bc3a92c9166'
down_revision: Union[str, Sequence[str], None] = '98f3a1150be9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users" , sa.Column("id" , sa.Integer() , nullable=False),
                            sa.Column("email" , sa.String() , nullable=False),
                            sa.Column("password" , sa.String() , nullable=False),
                            sa.Column("created_at" , sa.TIMESTAMP(timezone=True), server_default=sa.text("now()") , nullable=False),
                            sa.PrimaryKeyConstraint("id"),
                            sa.UniqueConstraint("email"),
                            )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")