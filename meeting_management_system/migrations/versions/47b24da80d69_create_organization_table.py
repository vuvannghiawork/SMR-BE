"""Create Organization Table

Revision ID: 47b24da80d69
Revises: fb3db9bbb9e1
Create Date: 2025-03-03 18:28:08.375539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47b24da80d69'
down_revision: Union[str, None] = 'fb3db9bbb9e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('meta_data', sa.JSON(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('NOW()::timestamp'), nullable=False),
    sa.Column('modified', sa.DateTime(), server_default=sa.text('NOW()::timestamp'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organizations_id'), 'organizations', ['id'], unique=False)
    op.create_index(op.f('ix_organizations_name'), 'organizations', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_organizations_name'), table_name='organizations')
    op.drop_index(op.f('ix_organizations_id'), table_name='organizations')
    op.drop_table('organizations')
    # ### end Alembic commands ###
