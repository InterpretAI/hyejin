"""empty message

Revision ID: 9bf24636dbcd
Revises: 4d1dc89dadb9
Create Date: 2023-09-07 19:05:07.614280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bf24636dbcd'
down_revision = '4d1dc89dadb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('modified_date')

    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('modified_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
