"""Create Customer Table

Revision ID: 6f09996258bd
Revises: 
Create Date: 2019-02-27 14:09:57.021353

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6f09996258bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(75))
    )


def downgrade():
    pass
