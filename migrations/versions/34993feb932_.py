"""empty message

Revision ID: 34993feb932
Revises: 2ea3890d8e37
Create Date: 2014-01-02 22:52:33.643914

"""

# revision identifiers, used by Alembic.
revision = '34993feb932'
down_revision = '2ea3890d8e37'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('greetings', sa.Column('is_friend_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('greetings', 'is_friend_at')
    ### end Alembic commands ###
