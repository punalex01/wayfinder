"""empty message

Revision ID: d0362036116b
Revises: afe839627861
Create Date: 2024-02-25 23:54:33.616180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0362036116b'
down_revision = 'afe839627861'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('jwt_auth_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_auth')
    # ### end Alembic commands ###