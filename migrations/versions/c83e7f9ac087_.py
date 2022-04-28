"""empty message

Revision ID: c83e7f9ac087
Revises: 15791a4b1d49
Create Date: 2022-04-28 19:43:14.426499

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c83e7f9ac087'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('population', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('passengers', sa.String(length=250), nullable=True),
    sa.Column('cargo_capacity', sa.String(length=250), nullable=True),
    sa.Column('consumibles', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Favorite_user', sa.Integer(), nullable=True),
    sa.Column('Favorite_planets', sa.Integer(), nullable=True),
    sa.Column('Favorite_characters', sa.Integer(), nullable=True),
    sa.Column('Favorite_vehicles', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Favorite_characters'], ['character.id'], ),
    sa.ForeignKeyConstraint(['Favorite_planets'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['Favorite_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['Favorite_vehicles'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('username', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=250), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=250), nullable=True))
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.drop_index('email', table_name='user')
    op.drop_index('email_2', table_name='user')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.create_index('email_2', 'user', ['email'], unique=False)
    op.create_index('email', 'user', ['email'], unique=False)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'name')
    op.drop_column('user', 'username')
    op.drop_table('favorite')
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
