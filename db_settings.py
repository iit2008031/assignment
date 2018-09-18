import os

from importlib import import_module
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

env = os.getenv('ENVIRONMENT', 'local')
config = import_module('config.%s' % env)

DB_STRING = config.DB_STRING
engine = create_engine(DB_STRING, pool_pre_ping=True)
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
