"""empty message

Revision ID: 138435878f00
Revises: f2ecf51f675e
Create Date: 2023-10-17 18:52:34.011234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '138435878f00'
down_revision = 'f2ecf51f675e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ad_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=False),
    sa.Column('hashed_password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"User_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='User_pkey'),
    sa.UniqueConstraint('username', name='User_username_key')
    )
    op.drop_table('ad_user')
    # ### end Alembic commands ###
