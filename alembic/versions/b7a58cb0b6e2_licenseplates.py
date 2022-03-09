"""licensePlates

Revision ID: b7a58cb0b6e2
Revises: bcdeb6b47060
Create Date: 2022-03-09 01:59:12.907478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7a58cb0b6e2'
down_revision = 'bcdeb6b47060'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "license_footage",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("filename", sa.String, unique=True, index=True),
        sa.Column("date_uploaded", sa.TIMESTAMP(), nullable=False, index=True),
        sa.Column("link", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
    )

    op.create_table(
        "recognized_plates",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, index=True),
        sa.Column("description", sa.String, index=True),
        sa.Column("owner_id", sa.Integer),
        sa.ForeignKeyConstraint(('owner_id',), ['users.id'], ),
    )


def downgrade():
    op.drop_table("users")
    op.drop_table("items")
