from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT, BOOLEAN
from sqlalchemy.sql import func
from flask_login import UserMixin
#  a crypto library that came with Flask
from werkzeug.security import generate_password_hash, check_password_hash


class OrderItem(db.Model):
    __tablename__ = "order_items"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('orders.id')), nullable=False)
    product_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('products.id')), nullable=False)
    price = Column(DECIMAL, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="items")

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "price": self.price
        }
