"""empty message

Revision ID: 98070bda55b5
Revises: efd4ea113803
Create Date: 2024-03-05 00:41:13.452662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98070bda55b5'
down_revision = 'efd4ea113803'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group_payment_lendees', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['uuid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group_payment_lendees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
