from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship, backref
from db import Base


class ProductDAO(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    adult = Column(Boolean)
    budget = Column(Integer)
    original_language = Column(String)
    overview = Column(String) #Essential for recommender
    release_date = Column(String)
    revenue = Column(Float)
    runtime = Column(Integer)
    title = Column(String) #Essential for recommender
    #TODO Add other relevant fields for our products.

    def __init__(self, adult, budget, original_language, overview, release_date, revenue, runtime, title):
        self.adult = adult
        self.budget = budget
        self.original_language = original_language
        self.overview = overview
        self.release_date = release_date
        self.revenue = revenue
        self.runtime = runtime
        self.title = title




