"""empty message

Revision ID: d9fb47e1c90
Revises: None
Create Date: 2013-09-13 14:45:14.365261

"""

# revision identifiers, used by Alembic.
revision = 'd9fb47e1c90'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_group',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_group')
    ### end Alembic commands ###
