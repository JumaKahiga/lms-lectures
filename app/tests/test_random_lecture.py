import os
import json
import pytest
from faker import Faker

from app.tests.test_base import BaseTest

fake = Faker()


class TestRandomLectureView(BaseTest):
    def setUp(self):
        super(TestRandomLectureView, self).setUp()

        if os.getenv('ENVIRONMENT') == 'testing':
            pytest.skip("seed data not loaded on Travis CI")

    def test_fetch_random_lecture(self):
        response = self.client.get('/')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIn('author', data['lecture'])

    def test_random_lecture_not_repeated(self):
        response_1 = self.client.get('/')
        response_2 = self.client.get('/')

        data_1 = json.loads(response_1.data.decode())
        data_2 = json.loads(response_2.data.decode())

        self.assertNotEqual(data_1['lecture']['id'], data_2['lecture']['id'])
