"""feat: added user foreign to tasks model

Revision ID: a94e7962b39f
Revises: 924cfa178ef3
Create Date: 2025-08-18 18:45:32.692902

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a94e7962b39f"
down_revision: Union[str, Sequence[str], None] = "924cfa178ef3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema for SQLite with batch mode."""
    with op.batch_alter_table("tasks", schema=None) as batch_op:
        batch_op.add_column(sa.Column("user_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_tasks_user_id_users",  # اسم constraint باید دستی بدی
            "users",
            ["user_id"],
            ["id"],
        )


def downgrade() -> None:
    """Downgrade schema for SQLite with batch mode."""
    with op.batch_alter_table("tasks", schema=None) as batch_op:
        batch_op.drop_constraint("fk_tasks_user_id_users", type_="foreignkey")
        batch_op.drop_column("user_id")
