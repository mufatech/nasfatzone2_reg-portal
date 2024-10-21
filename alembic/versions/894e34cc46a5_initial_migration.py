"""Initial migration

Revision ID: 894e34cc46a5
Revises: 
Create Date: 2024-10-02 15:10:57.525646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '894e34cc46a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'payment_mode')
    op.drop_column('user', 'massage')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('massage', mysql.VARCHAR(length=10), nullable=False))
    op.add_column('user', sa.Column('payment_mode', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###