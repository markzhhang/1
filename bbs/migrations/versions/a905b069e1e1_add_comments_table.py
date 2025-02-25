"""Add comments table

Revision ID: a905b069e1e1
Revises: e1ca64e587d5
Create Date: 2024-05-14 16:57:29.251588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a905b069e1e1'
down_revision = 'e1ca64e587d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamps', sa.DATETIME(), nullable=True),
    sa.Column('replied_id', sa.INTEGER(), nullable=True),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['t_user.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['t_post.id'], ),
    sa.ForeignKeyConstraint(['replied_id'], ['t_comments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_comments')
    # ### end Alembic commands ###
