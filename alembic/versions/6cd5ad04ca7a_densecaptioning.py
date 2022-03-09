"""DenseCaptioning

Revision ID: 6cd5ad04ca7a
Revises: bcdeb6b47060
Create Date: 2022-03-09 12:07:45.244683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cd5ad04ca7a'
down_revision = 'bcdeb6b47060'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "denseCaptionParent",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("imageName", sa.String, unique=True, index=True),
    )

    op.create_table(
        "denseCaptionChild",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("caption", sa.String, index=True),
        sa.Column("score", sa.Float),
        sa.Column("bounding_x", sa.Float),
        sa.Column("bounding_y", sa.Float),
        sa.Column("bounding_w", sa.Float),
        sa.Column("bounding_h", sa.Float),
        sa.Column("parent_id", sa.Integer),

        sa.ForeignKeyConstraint(('parent_id',), ['denseCaptionParent.id'], ),
    )


def downgrade():
    op.drop_table("denseCaptionParent")
    op.drop_table("denseCaptionChild")

