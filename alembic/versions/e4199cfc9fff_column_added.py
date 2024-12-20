"""Column Added

Revision ID: e4199cfc9fff
Revises: 93d4b5779860
Create Date: 2024-11-26 13:35:46.352902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4199cfc9fff'
down_revision: Union[str, None] = '93d4b5779860'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('marital_status', sa.String(length=50), nullable=True))
    op.drop_column('user', 'zone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('zone', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_column('user', 'marital_status')
    # ### end Alembic commands ###
