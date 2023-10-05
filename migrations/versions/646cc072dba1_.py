"""empty message

Revision ID: 646cc072dba1
Revises: c41abfd9c543
Create Date: 2023-09-06 13:16:36.351267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '646cc072dba1'
down_revision = 'c41abfd9c543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=False))
        batch_op.drop_column('answer')
        batch_op.drop_column('create_dt')

    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=False))
        batch_op.drop_column('prompt')
        batch_op.drop_column('create_dt')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_dt', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('prompt', sa.TEXT(), nullable=False))
        batch_op.drop_column('create_date')
        batch_op.drop_column('content')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_dt', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('answer', sa.TEXT(), nullable=False))
        batch_op.drop_column('create_date')
        batch_op.drop_column('content')

    op.create_table('feedback',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('answer_id', sa.INTEGER(), nullable=True),
    sa.Column('feedback', sa.TEXT(), nullable=False),
    sa.Column('create_dt', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['prompt.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###