"""auto-vote

Revision ID: 2acd97c67610
Revises: 8c1cdd2001b7
Create Date: 2023-01-11 12:24:19.947564

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2acd97c67610'
down_revision = '8c1cdd2001b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    op.alter_column('posts', 'published',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.drop_column('users', 'creted_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('creted_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.drop_column('users', 'created_at')
    op.alter_column('posts', 'published',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.drop_table('votes')
    # ### end Alembic commands ###