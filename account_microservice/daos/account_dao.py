from sqlalchemy import Column, String, Integer, DateTime
from db import Base

class AccountDAO(Base):
    __tablename__ = 'accounts'
    #TODO  Maybe automatically generate primary key instead of int?
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_email = Column(String)
    customer_password = Column(String)
    creation_time = Column(DateTime)

    #Indika says init is optional?
    def __init__(self, customer_name, customer_address, customer_email, customer_password, creation_time):
        #self.customer_id = customer_id #Don't know if this is needed, Indika doesn't use it.
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_email = customer_email
        self.customer_password = customer_password
        self.creation_time = creation_time

