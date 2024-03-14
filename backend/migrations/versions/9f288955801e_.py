"""empty message

Revision ID: 9f288955801e
Revises: 5b835d56baca
Create Date: 2024-03-07 22:59:12.661920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f288955801e'
down_revision = '5b835d56baca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group_payment_lendees', schema=None) as batch_op:
        batch_op.drop_constraint('group_payment_lendees_payment_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'group_payments', ['payment_id'], ['id'])

    with op.batch_alter_table('group_payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.drop_column('payment_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group_payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('payment_id', sa.INTEGER(), server_default=sa.text("nextval('group_payments_payment_id_seq'::regclass)"), autoincrement=True, nullable=False))
        batch_op.drop_column('id')

    with op.batch_alter_table('group_payment_lendees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('group_payment_lendees_payment_id_fkey', 'group_payments', ['payment_id'], ['payment_id'])

    # ### end Alembic commands ###
