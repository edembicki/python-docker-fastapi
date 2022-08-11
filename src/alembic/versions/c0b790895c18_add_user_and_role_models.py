"""ADD: User and Role models

Revision ID: c0b790895c18
Revises:
Create Date: 2021-07-22 17:04:51.912484

"""
from alembic import op
import sqlalchemy as sa
from core.role import ROLE

# revision identifiers, used by Alembic.
revision = 'c0b790895c18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    role_table = op.create_table(
        'rol',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=25), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=True),
        sa.Column('rol_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['rol_id'], ['rol.id'], onupdate='CASCADE', ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.bulk_insert(
        role_table,
        [
            {'id': 1, 'name': ROLE.ADMIN.value},
            {'id': 2, 'name': ROLE.BASIC.value}
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('rol')
    # ### end Alembic commands ###