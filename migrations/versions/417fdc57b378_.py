"""empty message

Revision ID: 417fdc57b378
Revises: a70688a9f3a0
Create Date: 2019-10-23 11:02:35.459192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '417fdc57b378'
down_revision = 'a70688a9f3a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person_admin', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('person_user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person_user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('person_admin', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###