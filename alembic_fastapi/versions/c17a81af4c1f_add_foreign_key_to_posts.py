"""add foreign key to posts

Revision ID: c17a81af4c1f
Revises: 4dc380db6469
Create Date: 2025-12-13 20:29:31.789170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c17a81af4c1f'
down_revision: Union[str, Sequence[str], None] = '4dc380db6469'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts" , sa.Column("owner_id" , sa.Integer() , nullable=False))
    op.create_foreign_key("posts_users_fk" , 
                          source_table="posts" , 
                          referent_table="users" , 
                          local_cols=["owner_id"], 
                          remote_cols=["id"] , 
                          ondelete="CASCADE"
                          )
    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk" , table_name="posts")
    op.drop_column("posts" , "owner_id")
