"""empty message

Revision ID: 67cd3535dba5
Revises: e64a8f481bc2
Create Date: 2023-07-24 15:57:00.111997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cd3535dba5'
down_revision = 'e64a8f481bc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('stid', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('belong', sa.Text(), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('local', sa.Text(), nullable=True),
    sa.Column('rival_id', sa.Integer(), nullable=True),
    sa.Column('passwd', sa.Text(), nullable=False),
    sa.Column('join_date', sa.DateTime(), nullable=False),
    sa.Column('login_token', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('stid', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('gender', sa.INTEGER(), nullable=False),
    sa.Column('local', sa.TEXT(), nullable=True),
    sa.Column('join_date', sa.DATETIME(), nullable=False),
    sa.Column('login_token', sa.TEXT(), nullable=True),
    sa.Column('passwd', sa.TEXT(), nullable=False),
    sa.Column('id', sa.TEXT(), nullable=False),
    sa.Column('belong', sa.TEXT(), nullable=True),
    sa.Column('rival_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('stid')
    )
    op.drop_table('user')
    # ### end Alembic commands ###