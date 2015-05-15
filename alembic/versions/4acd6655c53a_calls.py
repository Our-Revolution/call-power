"""Create calls table

Revision ID: 4acd6655c53a
Revises: 2ca033d14a4
Create Date: 2015-05-06 21:33:14.425230

"""

# revision identifiers, used by Alembic.
revision = '4acd6655c53a'
down_revision = '2ca033d14a4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('campaign_id', sa.Integer(), nullable=True),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.Column('phone_hash', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('call_id', sa.String(length=40), nullable=True),
    sa.Column('status', sa.String(length=25), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign_campaign.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['campaign_target.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calls')
    ### end Alembic commands ###