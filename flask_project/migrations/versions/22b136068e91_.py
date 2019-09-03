"""empty message

Revision ID: 22b136068e91
Revises: d49065648960
Create Date: 2019-08-27 23:43:10.020471

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '22b136068e91'
down_revision = 'd49065648960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('telephone', sa.String(length=11), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('telephone', mysql.VARCHAR(collation='utf8mb4_general_ci', length=11), nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8mb4_general_ci', length=50), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(collation='utf8mb4_general_ci', length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('users')
    # ### end Alembic commands ###