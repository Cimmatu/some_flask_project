"""empty message

Revision ID: 1294b83cc0a1
Revises: e83c1d714a07
Create Date: 2020-09-06 21:13:30.277883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1294b83cc0a1'
down_revision = 'e83c1d714a07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=3), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('experience', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='employee_pkey')
    )
    # ### end Alembic commands ###