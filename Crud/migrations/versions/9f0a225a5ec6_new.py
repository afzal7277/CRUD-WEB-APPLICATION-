"""new

Revision ID: 9f0a225a5ec6
Revises: 
Create Date: 2022-09-16 15:45:14.177309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f0a225a5ec6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hospital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pt_name', sa.Text(), nullable=True),
    sa.Column('sex', sa.Text(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('doc_name', sa.Text(), nullable=True),
    sa.Column('par_name', sa.Text(), nullable=True),
    sa.Column('ph_num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hospital')
    # ### end Alembic commands ###
