from sqlalchemy import Column, Boolean, String, Integer, DateTime, Float
from db import Base

class recommenderDAO(Base):
    __tablename__ = 'recommender'
    id = Column(Integer, primary_key=True)
    adult = Column(Boolean)
    budget = Column(Integer)
    original_language = Column(String)
    original_title = Column(String)
    overview = Column(String)
    popularity = Column(Float)
    release_date = Column(DateTime)
    revenue = Column(Float)
    runtime = Column(Integer)
    status = Column(String)
    title = Column(String)
    vote_average = Column(Float)
    vote_count = Column(Integer)

#TODO upload data into DAO
