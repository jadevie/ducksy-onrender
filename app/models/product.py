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


class Product(db.Model):
    __tablename__ = "products"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)

    shop_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(TEXT)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    shop = relationship("User", back_populates="products")
    product_images = relationship("ProductImage", back_populates="product")
    reviews = relationship("Review", back_populates="product")

    def to_dict(self):
        return {
            "id": self.id,
            "shop_id": self.shop_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "preview_image": self.product_images[0].url if len(self.product_images) else None
        }