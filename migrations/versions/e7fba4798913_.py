"""empty message

Revision ID: e7fba4798913
Revises: 6c3a9c5e5016
Create Date: 2022-05-23 00:45:59.062314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7fba4798913'
down_revision = '6c3a9c5e5016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('name', name=op.f('pk_category')),
    sa.UniqueConstraint('name', name=op.f('uq_category_name'))
    )
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_name', sa.String(length=20), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_question_category_name_category'), 'category', ['category_name'], ['name'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_question_category_name_category'), type_='foreignkey')
        batch_op.drop_column('category_name')

    op.drop_table('category')
    # ### end Alembic commands ###