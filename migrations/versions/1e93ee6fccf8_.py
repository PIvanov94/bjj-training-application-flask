"""empty message

Revision ID: 1e93ee6fccf8
Revises: 8282ffed4c74
Create Date: 2022-01-09 14:11:09.891929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e93ee6fccf8'
down_revision = '8282ffed4c74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('advanced', sa.Column('group', sa.String(length=100), nullable=False))
    op.add_column('beginners', sa.Column('group', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('beginners', 'group')
    op.drop_column('advanced', 'group')
    # ### end Alembic commands ###