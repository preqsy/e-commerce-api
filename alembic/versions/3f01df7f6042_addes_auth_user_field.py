"""addes auth user field

Revision ID: 3f01df7f6042
Revises: 4d5d73ff1b6b
Create Date: 2024-02-19 01:06:02.146037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3f01df7f6042'
down_revision: Union[str, None] = '4d5d73ff1b6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendor')
    op.add_column('customer', sa.Column('phone_number', sa.String(), nullable=False))
    op.add_column('customer', sa.Column('default_role', sa.String(), server_default='customer', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'default_role')
    op.drop_column('customer', 'phone_number')
    op.create_table('vendor',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='vendor_pkey'),
    sa.UniqueConstraint('email', name='vendor_email_key')
    )
    # ### end Alembic commands ###
