"""add user's col.

Revision ID: b2ea294b35eb
Revises: 
Create Date: 2024-05-10 22:38:46.216750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ea294b35eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=6), nullable=True))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('mobile', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('signature', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.drop_column('signature')
        batch_op.drop_column('email')
        batch_op.drop_column('mobile')
        batch_op.drop_column('age')
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
