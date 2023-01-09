"""create products_categories join table

Revision ID: 4fcf428a4e76
Revises: 08957bb0dc5c
Create Date: 2022-12-11 11:13:23.102561

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
# revision identifiers, used by Alembic.
revision = '4fcf428a4e76'
down_revision = '08957bb0dc5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_categories',
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['category_id'], ['categories.id'], name='fk_products_category_category_id'),
                    sa.ForeignKeyConstraint(
                        ['product_id'], ['products.id'], name='fk_products_category_product_id'),
                    sa.PrimaryKeyConstraint('product_id', 'category_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products_categories')
    # ### end Alembic commands ###
