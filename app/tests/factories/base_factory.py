import os

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.getenv('DATABASE_URL'))
session = scoped_session(sessionmaker(bind=engine))

fake = Faker()
