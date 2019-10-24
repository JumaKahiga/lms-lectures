import factory

from app.models.person_model import Lecture, Review
from app.tests.factories.base_factory import session, fake
from app.tests.factories.person_factory import UserFactory


class LectureFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Lecture
        sqlalchemy_session = session

    id = fake.random_int()
    thumbnail_url = fake.url()
    type = fake.name()
    excerpt = fake.sentence()
    pdf_download_url = fake.url()
    slug = fake.name()
    tags = [fake.name()]
    author = factory.SubFactory(UserFactory)
    content = fake.text()
    title = fake.name()


class ReviewFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Review
        sqlalchemy_session = session

    id = fake.random_int()
    user = factory.SubFactory(UserFactory)
    text = fake.text()
    rating = fake.random_int()
    reviewed_lecture = factory.SubFactory(LectureFactory)
