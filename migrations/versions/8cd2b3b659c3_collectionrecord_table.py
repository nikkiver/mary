"""collectionrecord table

Revision ID: 8cd2b3b659c3
Revises: 
Create Date: 2019-07-27 09:41:50.819507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8cd2b3b659c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collectionrecord',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('collectiondate', sa.DateTime(), nullable=True),
    sa.Column('standard', sa.String(length=10), nullable=True),
    sa.Column('teacherinitials', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_collectionrecord_collectiondate'), 'collectionrecord', ['collectiondate'], unique=False)
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('initials', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('pno', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teacher_name'), 'teacher', ['name'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('defaulter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admno', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collectionrecord.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('defaulter')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_teacher_name'), table_name='teacher')
    op.drop_table('teacher')
    op.drop_table('subject')
    op.drop_index(op.f('ix_collectionrecord_collectiondate'), table_name='collectionrecord')
    op.drop_table('collectionrecord')
    # ### end Alembic commands ###