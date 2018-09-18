import os
from importlib import import_module

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# getting Environemnt type
env = os.getenv('ENVIRONMENT', 'local')

# Loading config file on the basis Environemnt
config = import_module('config.%s' % env)


DB_STRING = config.DB_STRING

# Creating db Engine and session for Sqlalchemy
engine = create_engine(DB_STRING, pool_pre_ping=True)
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
