import os

import factory
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models.person_model import Admin, User, Person


engine = create_engine(os.getenv('DATABASE_URL'))
session = scoped_session(sessionmaker(bind=engine))

fake = Faker()


class AdminFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Admin
        sqlalchemy_session = session

    id = fake.random_int()
    name = fake.user_name()
    email = fake.email()
    password_hash = Person().set_password(fake.password())
    is_admin = True


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = session

    id = fake.random_int()
    name = fake.user_name()
    email = fake.email()
    password_hash = Person().set_password(fake.password())
    is_author = False
    bio = fake.text()
    company = fake.name()
    avatar_url = fake.url()
    social_urls = fake.url()
