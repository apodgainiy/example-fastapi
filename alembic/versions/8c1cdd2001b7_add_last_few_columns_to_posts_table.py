"""add last few columns to posts table

Revision ID: 8c1cdd2001b7
Revises: b9383a26b93f
Create Date: 2023-01-11 10:26:59.802045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c1cdd2001b7'
down_revision = 'b9383a26b93f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column(
            'published', 
            sa.Boolean(), 
            nullable=False, 
            server_default='TRUE'
            ),
        )
    op.add_column(
        'posts',
        sa.Column(
            'created_at', 
            sa.TIMESTAMP(timezone=True), 
            nullable=False, 
            server_default=sa.text('now()')
            ),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
