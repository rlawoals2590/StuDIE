"""empty message

Revision ID: 80201929bfc7
Revises: b39357f9ca48
Create Date: 2023-07-24 14:47:45.260087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80201929bfc7'
down_revision = 'b39357f9ca48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('point', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Text(), nullable=False))
        batch_op.alter_column('stid',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               nullable=True)
        batch_op.alter_column('school',
               existing_type=sa.TEXT(),
               nullable=True)

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Text(), nullable=False))
        batch_op.alter_column('stid',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('passwd',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('school',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('school',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('passwd',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('stid',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('id')

    with op.batch_alter_table('point', schema=None) as batch_op:
        batch_op.alter_column('school',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('stid',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('id')

    # ### end Alembic commands ###