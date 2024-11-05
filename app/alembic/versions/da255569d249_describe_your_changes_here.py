"""Describe your changes here

Revision ID: da255569d249
Revises: ac7e9a26c98f
Create Date: 2024-11-05 03:17:25.491943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da255569d249'
down_revision: Union[str, None] = 'ac7e9a26c98f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nickname', sa.String(), nullable=True))
    op.add_column('users', sa.Column('comment', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'comment')
    op.drop_column('users', 'nickname')
    # ### end Alembic commands ###
