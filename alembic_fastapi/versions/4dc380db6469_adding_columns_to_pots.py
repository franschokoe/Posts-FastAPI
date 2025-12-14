"""adding columns to pots

Revision ID: 4dc380db6469
Revises: 1bc3a92c9166
Create Date: 2025-12-13 20:16:15.325000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dc380db6469'
down_revision: Union[str, Sequence[str], None] = '1bc3a92c9166'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts" , sa.Column("created_at" ,
                                      sa.TIMESTAMP(timezone=True) , 
                                      server_default=sa.text("now()") , 
                                      nullable=False)
                                      )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts" , "created_at")
