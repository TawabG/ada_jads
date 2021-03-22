from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref

from db import Base


class CartDAO(Base):
    __tablename__ = 'cart3'
    id = Column(Integer, primary_key=True)
    customer_id = Column(String)
    product_id = Column(Integer)
    # ForeignKey(product.id))
    product_name = Column(String)
    product_quantity = Column(Integer)
    added_time = Column(DateTime)

    def __init__(self, customer_id, product_id, product_name, product_quantity, added_time):
        self.customer_id = customer_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.added_time = added_time