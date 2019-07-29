"""create user table

Revision ID: d5612011598f
Revises: 
Create Date: 2019-07-29 01:41:13.029676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5612011598f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('email', sa.String(255)),
    )

def downgrade():
    op.drop_table('users')
