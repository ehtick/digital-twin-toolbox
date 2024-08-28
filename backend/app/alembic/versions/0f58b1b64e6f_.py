"""empty message

Revision ID: 0f58b1b64e6f
Revises: 
Create Date: 2024-08-28 09:55:47.229904

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0f58b1b64e6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('full_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('asset',
    sa.Column('filename', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('content_type', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('content_size', sa.Integer(), nullable=True),
    sa.Column('asset_type', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('extension', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('geometry_type', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('upload_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('upload_status', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('upload_result', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('owner_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pipeline',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('asset_id', sa.Uuid(), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('task_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('task_status', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('task_result', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('owner_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pipeline')
    op.drop_table('asset')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
