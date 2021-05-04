import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

if "DB_URL" is os.environ:
    db_url = os.environ['DB_URL']
else:
    db_url = 'sqlite:///account.db'

engine = create_engine(db_url)
if not database_exists(engine.url):
    create_database(engine.url)

# https://docs.sqlalchemy.org/en/13/orm/session.html
Session = sessionmaker(bind=engine)
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html
#We can use Declarative base to implement our data access objects (daos). Need to extend from this class, and create tables etc.
Base = declarative_base()

