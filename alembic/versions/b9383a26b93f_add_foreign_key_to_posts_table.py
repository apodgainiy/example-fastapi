"""add foreign-key to posts table

Revision ID: b9383a26b93f
Revises: 92d5d393214f
Create Date: 2023-01-11 10:11:16.408846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9383a26b93f'
down_revision = '92d5d393214f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
        )
    op.create_foreign_key(
        'post_users_fk', 
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
        )
    pass



def downgrade() -> None:
    op.drop_constraint(
        'post_users_fk',
        table_name='posts'
        )
    op.drop_column('posts', 'owner_id')
    pass
