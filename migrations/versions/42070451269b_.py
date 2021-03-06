"""empty message

Revision ID: 42070451269b
Revises: c1fc3b901ee0
Create Date: 2019-10-27 09:33:54.757919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42070451269b'
down_revision = 'c1fc3b901ee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('description', sa.String(length=4096), nullable=True))
    op.add_column('submission', sa.Column('notes', sa.String(length=4096), nullable=True))
    op.add_column('submission', sa.Column('pitch', sa.String(length=4096), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'pitch')
    op.drop_column('submission', 'notes')
    op.drop_column('submission', 'description')
    # ### end Alembic commands ###
