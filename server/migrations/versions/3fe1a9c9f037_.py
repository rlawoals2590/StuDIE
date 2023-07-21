"""empty message

Revision ID: 3fe1a9c9f037
Revises: 336d48f0a151
Create Date: 2023-07-21 19:32:22.468991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fe1a9c9f037'
down_revision = '336d48f0a151'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('point', schema=None) as batch_op:
        batch_op.drop_constraint('pk_stid_school_point', type_='unique')
        batch_op.create_unique_constraint('pk_stid_school_point2', ['stid', 'school'])
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_constraint('pk_stid_school_student', type_='unique')
        batch_op.create_unique_constraint('pk_stid_school_student2', ['stid', 'school'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_constraint('pk_stid_school_student2', type_='unique')
        batch_op.create_unique_constraint('pk_stid_school_student', ['stid', 'school'])

    with op.batch_alter_table('point', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'student', ['school'], ['stid'])
        batch_op.drop_constraint('pk_stid_school_point2', type_='unique')
        batch_op.create_unique_constraint('pk_stid_school_point', ['stid', 'school'])

    # ### end Alembic commands ###
