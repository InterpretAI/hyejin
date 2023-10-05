"""empty message

Revision ID: 641e51d530ff
Revises: 34b6495a14c9
Create Date: 2023-09-07 15:10:55.369286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '641e51d530ff'
down_revision = '34b6495a14c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_prompt_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_prompt_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
