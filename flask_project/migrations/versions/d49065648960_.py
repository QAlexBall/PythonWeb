"""empty message

Revision ID: d49065648960
Revises: 83ceba6ef73b
Create Date: 2019-08-25 23:49:33.122146

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd49065648960'
down_revision = '83ceba6ef73b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(collation='utf8mb4_general_ci', length=100), nullable=False))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
