"""empty message

Revision ID: 32227fb6b6fa
Revises: 42d85c765a37
Create Date: 2013-09-18 15:52:44.561180

"""

# revision identifiers, used by Alembic.
revision = '32227fb6b6fa'
down_revision = '42d85c765a37'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table(u'user_group')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'user_group',
    sa.Column(u'user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint(u'user_id')
    )
    op.drop_table('posts')
    ### end Alembic commands ###
