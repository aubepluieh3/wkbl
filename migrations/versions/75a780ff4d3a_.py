"""empty message

Revision ID: 75a780ff4d3a
Revises: 792ed3b027f5
Create Date: 2022-05-26 22:10:07.122731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75a780ff4d3a'
down_revision = '792ed3b027f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fanswer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('free_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_fanswer_question_id_free', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_fanswer_free_id_free'), 'free', ['free_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('question_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fanswer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_fanswer_free_id_free'), type_='foreignkey')
        batch_op.create_foreign_key('fk_fanswer_question_id_free', 'free', ['question_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('free_id')

    # ### end Alembic commands ###