"""empty message

Revision ID: 1fa35857409f
Revises: 65381b8249b2
Create Date: 2022-03-18 13:42:10.584113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fa35857409f'
down_revision = '65381b8249b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_table', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user_table', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'user_table', ['email'])
    op.create_unique_constraint(None, 'user_table', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_table', type_='unique')
    op.drop_constraint(None, 'user_table', type_='unique')
    op.alter_column('user_table', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user_table', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
