"""create table

Revision ID: 94046d42eaef
Revises: 188deab7cf5e
Create Date: 2025-07-29 00:14:20.359847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '94046d42eaef'
down_revision: Union[str, Sequence[str], None] = '188deab7cf5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'image')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('image', postgresql.BYTEA(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
