"""empty message

Revision ID: 98114788ebad
Revises: e8d73cf3a973
Create Date: 2024-03-05 01:18:51.123065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98114788ebad'
down_revision = 'e8d73cf3a973'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jwt_token_blocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jwt_token', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('user',
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
    op.create_table('TripUsers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_payments',
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('is_returned', sa.Boolean(), nullable=False),
    sa.Column('lender_id', sa.Integer(), nullable=True),
    sa.Column('total', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['lender_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('payment_id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('user_auth',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('jwt_auth_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('group_payment_lendees',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('lendee_id', sa.Integer(), nullable=True),
    sa.Column('is_returned', sa.Boolean(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lendee_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['group_payments.payment_id'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_payment_lendees')
    op.drop_table('user_auth')
    op.drop_table('group_payments')
    op.drop_table('TripUsers')
    op.drop_table('user')
    op.drop_table('trip')
    op.drop_table('jwt_token_blocklist')
    # ### end Alembic commands ###
