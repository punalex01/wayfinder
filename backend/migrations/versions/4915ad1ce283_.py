"""empty message

Revision ID: 4915ad1ce283
Revises: e5d99cc06f5b
Create Date: 2024-03-05 01:08:30.726856

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4915ad1ce283'
down_revision = 'e5d99cc06f5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.drop_table('users')
    with op.batch_alter_table('TripUsers', schema=None) as batch_op:
        batch_op.drop_constraint('TripUsers_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Users', ['user_id'], ['id'])

    with op.batch_alter_table('group_payment_lendees', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['uuid'])
        batch_op.drop_constraint('group_payment_lendees_lendee_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Users', ['lendee_id'], ['id'])

    with op.batch_alter_table('group_payments', schema=None) as batch_op:
        batch_op.drop_constraint('group_payments_lender_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Users', ['lender_id'], ['id'])

    with op.batch_alter_table('user_auth', schema=None) as batch_op:
        batch_op.drop_constraint('user_auth_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_auth', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_auth_user_id_fkey', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('group_payments', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('group_payments_lender_id_fkey', 'users', ['lender_id'], ['id'])

    with op.batch_alter_table('group_payment_lendees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('group_payment_lendees_lendee_id_fkey', 'users', ['lendee_id'], ['id'])
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('TripUsers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('TripUsers_user_id_fkey', 'users', ['user_id'], ['id'])

    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('created', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('uuid', name='users_uuid_key')
    )
    op.drop_table('Users')
    # ### end Alembic commands ###
