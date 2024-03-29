"""empty message

Revision ID: b38711bb641f
Revises: d237c0eae4dc
Create Date: 2024-02-28 01:26:37.203971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38711bb641f'
down_revision = 'd237c0eae4dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trips',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trips')
    # ### end Alembic commands ###
