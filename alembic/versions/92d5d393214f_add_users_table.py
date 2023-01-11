"""add users table

Revision ID: 92d5d393214f
Revises: 42bbbf5feee3
Create Date: 2023-01-11 09:49:53.853886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92d5d393214f'
down_revision = '42bbbf5feee3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('creted_at', sa.TIMESTAMP(timezone=True), nullable=False, 
                            server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
