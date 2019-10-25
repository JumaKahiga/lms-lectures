from faker import Faker

from app.models.person_model import Person
from app.tests.factories.person_factory import (
    AdminFactory, UserFactory)
from app.tests.test_base import BaseTest

fake = Faker()


class TestPersonModel(BaseTest):
    def setUp(self):
        super(TestPersonModel, self).setUp()
        self.password = fake.password()
        self.person = Person()
        self.person.set_password(self.password)

    def test_authenticate(self):
        self.assertEqual(
            self.person.authenticate_password(self.password), True)


class TestAdminModel(BaseTest):
    def setUp(self):
        super(TestAdminModel, self).setUp()
        self.admin = AdminFactory()

    def test_if_admin(self):
        self.assertEqual(self.admin.is_admin, True)


class TestUserModel(BaseTest):
    def setUp(self):
        super(TestUserModel, self).setUp()
        self.user = UserFactory()

    def test_if_default_user(self):
        self.assertEqual(self.user.is_author, False)
