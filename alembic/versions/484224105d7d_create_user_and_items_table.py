"""Create User and Items Table

Revision ID: 484224105d7d
Revises: 83c0a218cd0b
Create Date: 2022-02-16 15:11:07.484461

"""
from enum import unique
from textwrap import indent
from alembic import op
from graphene import Boolean
from mysqlx import Column
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '484224105d7d'
down_revision = '83c0a218cd0b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("hashed_password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
    )

    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, index=True),
        sa.Column("description", sa.String, index=True),
        sa.Column("owner_id", sa.Integer),
        sa.ForeignKeyConstraint(('owner_id',), ['users.id'], ),
    )


def downgrade():
    op.drop_table("users")
    op.drop_table("items")
