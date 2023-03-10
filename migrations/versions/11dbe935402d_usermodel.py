"""UserModel

Revision ID: 11dbe935402d
Revises: 3ebfaf82e1f3
Create Date: 2023-03-04 19:40:29.571675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11dbe935402d'
down_revision = '3ebfaf82e1f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_model')
    # ### end Alembic commands ###
