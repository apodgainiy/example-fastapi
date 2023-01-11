"""add content column to posts table

Revision ID: 42bbbf5feee3
Revises: 048eccd29001
Create Date: 2023-01-11 09:41:51.498779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42bbbf5feee3'
down_revision = '048eccd29001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
