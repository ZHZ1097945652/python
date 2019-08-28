"""db tables

Revision ID: b56984bd562c
Revises: 0a9f283b7ca4
Create Date: 2019-08-26 18:28:38.585723

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b56984bd562c'
down_revision = '0a9f283b7ca4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ih_area_info', 'name',
               existing_type=mysql.CHAR(length=10),
               nullable=False)
    op.alter_column('ih_facility_info', 'name',
               existing_type=mysql.CHAR(charset='utf8', length=10),
               nullable=False)
    op.alter_column('ih_house_image', 'url',
               existing_type=mysql.VARCHAR(charset='utf8', length=256),
               nullable=False)
    op.alter_column('ih_house_info', 'title',
               existing_type=mysql.VARCHAR(charset='utf8', length=64),
               nullable=False)
    op.add_column('ih_order_info', sa.Column('trade_no', sa.String(length=80), nullable=True))
    op.alter_column('ih_user_profile', 'mobile',
               existing_type=mysql.VARCHAR(charset='utf8', length=11),
               nullable=False)
    op.alter_column('ih_user_profile', 'name',
               existing_type=mysql.VARCHAR(charset='utf8', length=32),
               nullable=False)
    op.alter_column('ih_user_profile', 'password_hash',
               existing_type=mysql.VARCHAR(charset='utf8', length=128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ih_user_profile', 'password_hash',
               existing_type=mysql.VARCHAR(charset='utf8', length=128),
               nullable=True)
    op.alter_column('ih_user_profile', 'name',
               existing_type=mysql.VARCHAR(charset='utf8', length=32),
               nullable=True)
    op.alter_column('ih_user_profile', 'mobile',
               existing_type=mysql.VARCHAR(charset='utf8', length=11),
               nullable=True)
    op.drop_column('ih_order_info', 'trade_no')
    op.alter_column('ih_house_info', 'title',
               existing_type=mysql.VARCHAR(charset='utf8', length=64),
               nullable=True)
    op.alter_column('ih_house_image', 'url',
               existing_type=mysql.VARCHAR(charset='utf8', length=256),
               nullable=True)
    op.alter_column('ih_facility_info', 'name',
               existing_type=mysql.CHAR(charset='utf8', length=10),
               nullable=True)
    op.alter_column('ih_area_info', 'name',
               existing_type=mysql.CHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###
