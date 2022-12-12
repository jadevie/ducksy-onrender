"""On delete cascade for user

Revision ID: 8831b7a5f48f
Revises: 4fcf428a4e76
Create Date: 2022-12-12 10:38:05.235212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8831b7a5f48f'
down_revision = '4fcf428a4e76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_detail_order_id', type_='foreignkey')
        batch_op.drop_constraint('fk_order_detail_seller_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_detail_order_id', 'orders', ['order_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('fk_order_detail_seller_id', 'users', ['seller_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_buyer_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_buyer_id', 'users', ['buyer_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_seller_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_product_seller_id', 'users', ['seller_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_review_buyer_id', type_='foreignkey')
        batch_op.drop_constraint('fk_review_seller_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_review_buyer_id', 'users', ['buyer_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('fk_review_seller_id', 'users', ['seller_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_review_seller_id', type_='foreignkey')
        batch_op.drop_constraint('fk_review_buyer_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_review_seller_id', 'users', ['seller_id'], ['id'])
        batch_op.create_foreign_key('fk_review_buyer_id', 'users', ['buyer_id'], ['id'])

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_seller_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_product_seller_id', 'users', ['seller_id'], ['id'])

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_buyer_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_buyer_id', 'users', ['buyer_id'], ['id'])

    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_detail_seller_id', type_='foreignkey')
        batch_op.drop_constraint('fk_order_detail_order_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_detail_seller_id', 'users', ['seller_id'], ['id'])
        batch_op.create_foreign_key('fk_order_detail_order_id', 'orders', ['order_id'], ['id'])

    # ### end Alembic commands ###
