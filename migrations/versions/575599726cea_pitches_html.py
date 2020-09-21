"""pitches.html

Revision ID: 575599726cea
Revises: 0c2ade9137bd
Create Date: 2020-09-21 11:56:41.198178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575599726cea'
down_revision = '0c2ade9137bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.add_column('pitches', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='categories_pkey')
    )
    # ### end Alembic commands ###