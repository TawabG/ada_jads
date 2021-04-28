from sqlalchemy import Column, String, Integer, Numeric, DateTime

from db import Base

class ProductDAO(Base):
    __tablename__ = 'cart0'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_quantity = Column(String)
    unit_price = Column(Numeric)
    added_time = Column(DateTime)

    def __init__(self, product_name, product_quantity, unit_price, added_time):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.unit_price = unit_price
        self.added_time = added_time
