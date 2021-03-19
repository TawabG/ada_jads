from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from cartdaos.status_dao import StatusDAO
from db import Base


class CartDAO(Base):
    __tablename__ = 'cart1'
    id = Column(Integer, primary_key=True)
    customer_id = Column(String)
    product_id = Column(String)
    added_time = Column(DateTime)
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("cart", uselist=False))

    def __init__(self, customer_id, product_id, added_time, status):
        self.customer_id = customer_id
        self.product_id = product_id
        self.added_time = added_time
        self.status = status
