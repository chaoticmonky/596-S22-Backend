"""create messages table

Revision ID: 7de0f169e25d
Revises: 484224105d7d
Create Date: 2022-02-22 20:53:28.475993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7de0f169e25d'
down_revision = '484224105d7d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "messages",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("text", sa.String, index=True),
        sa.Column("sender_id", sa.Integer),
        sa.ForeignKeyConstraint(('sender_id',), ['users.id'], ),
        sa.Column("recipient_id", sa.Integer),
    )


def downgrade():
    op.drop_table("messages")
