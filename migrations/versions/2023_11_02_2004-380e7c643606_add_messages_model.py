"""add_messages_model

Revision ID: 380e7c643606
Revises: d333f98c4eff
Create Date: 2023-11-02 20:04:42.261161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '380e7c643606'
down_revision: Union[str, None] = 'd333f98c4eff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('user', 'registered_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('user', 'role_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'role_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user', 'registered_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_table('messages')
    # ### end Alembic commands ###
