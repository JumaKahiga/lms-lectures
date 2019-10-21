import factory

from app.models.person_model import Admin, User, Person
from app.tests.factories.base_factory import session, fake


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
