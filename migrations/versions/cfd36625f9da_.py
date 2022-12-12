"""empty message

Revision ID: cfd36625f9da
Revises: 7f4911e5ffda
Create Date: 2022-12-07 16:48:17.296485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfd36625f9da'
down_revision = '7f4911e5ffda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('ability', sa.String(length=30), nullable=True),
    sa.Column('base_experience', sa.Integer(), nullable=True),
    sa.Column('sprite', sa.String(), nullable=True),
    sa.Column('attack_base_stat', sa.Integer(), nullable=True),
    sa.Column('hp_base_stat', sa.Integer(), nullable=True),
    sa.Column('defense_base_stat', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_pokemon')
    # ### end Alembic commands ###