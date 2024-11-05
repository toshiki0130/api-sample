"""change Users columns

Revision ID: e398e54a34c2
Revises: bf4445bea4c0
Create Date: 2024-11-04 12:00:13.669963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e398e54a34c2'
down_revision: Union[str, None] = 'bf4445bea4c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
