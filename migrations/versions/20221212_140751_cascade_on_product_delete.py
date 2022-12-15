"""Cascade on product delete

Revision ID: fb12da79d47b
Revises: 8831b7a5f48f
Create Date: 2022-12-12 14:07:51.293298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb12da79d47b'
down_revision = '8831b7a5f48f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('product_images', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_image_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_product_image_product_id', 'products', ['product_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_review_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_review_product_id', 'products', ['product_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_review_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_review_product_id', 'products', ['product_id'], ['id'])

    with op.batch_alter_table('product_images', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_image_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_product_image_product_id', 'products', ['product_id'], ['id'])

    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###