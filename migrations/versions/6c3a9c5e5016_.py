"""empty message

Revision ID: 6c3a9c5e5016
Revises: b2a6f1228f31
Create Date: 2022-05-22 00:29:16.911770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c3a9c5e5016'
down_revision = 'b2a6f1228f31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('birth', sa.Date(), nullable=False))
        batch_op.create_unique_constraint(batch_op.f('uq_user_phone'), ['phone'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_phone'), type_='unique')
        batch_op.drop_column('birth')
        batch_op.drop_column('phone')

    # ### end Alembic commands ###