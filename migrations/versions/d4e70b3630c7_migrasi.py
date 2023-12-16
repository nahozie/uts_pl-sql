""" migrasi

Revision ID: d4e70b3630c7
Revises: 
Create Date: 2023-12-16 22:29:41.070247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e70b3630c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('encrypted_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('users2')
    op.drop_table('employees')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('employee_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('hire_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('employee_id', name='employees_pkey'),
    sa.UniqueConstraint('email', name='employees_email_key')
    )
    op.create_table('users2',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users2_pkey'),
    sa.UniqueConstraint('username', name='users2_username_key')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
