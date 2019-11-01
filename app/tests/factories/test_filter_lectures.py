import os

import json
import pytest

from faker import Faker

from app.models.person_model import User
from app.tests.test_base import BaseTest

fake = Faker()


class TestFilterLectures(BaseTest):
    def setUp(self):
        super(TestFilterLectures, self).setUp()

    @pytest.mark.skipif(os.getenv('ENVIRONMENT') == 'testing', reason='seed data not loaded on Travis CI') # noqa
    def test_fetch_lecture_by_author(self):
        user = User.query.filter(User.name.isnot(None)).first()
        response = self.client.get('lectures/filter/{}'.format(user.name))
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIn('lectures', data)

    def test_fetch_author_not_found(self):
        author_name = fake.name()
        response = self.client.get('lectures/filter/{}'.format(author_name))
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data['message'], f'no lecture found with {author_name} as author')
