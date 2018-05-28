"""followers

Revision ID: 07270f03ebde
Revises: b65fb71ed283
Create Date: 2018-05-27 20:07:58.056330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07270f03ebde'
down_revision = 'b65fb71ed283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
