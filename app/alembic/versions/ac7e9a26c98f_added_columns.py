"""Added columns.

Revision ID: ac7e9a26c98f
Revises: e398e54a34c2
Create Date: 2024-11-04 12:07:04.228119

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac7e9a26c98f'
down_revision: Union[str, None] = 'e398e54a34c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.String(), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_column('users', 'email')
    op.drop_column('users', 'username')
    op.drop_column('users', 'id')
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'password')
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###
