"""Init

Revision ID: d14641028cf7
Revises: 
Create Date: 2023-09-13 10:06:14.047587

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'd14641028cf7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('passwords',
    sa.Column('passwd', sqlalchemy_utils.types.password.PasswordType(max_length=1094), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('login', sa.VARCHAR(length=40), nullable=False),
    sa.Column('email', sa.VARCHAR(length=40), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('tokens',
    sa.Column('token', sa.VARCHAR(length=40), nullable=False),
    sa.Column('key', sa.VARCHAR(length=40), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tokens')
    op.drop_table('users')
    op.drop_table('passwords')
    # ### end Alembic commands ###