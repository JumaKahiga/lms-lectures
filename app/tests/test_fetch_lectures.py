import os

import json
import pytest

from faker import Faker

from app.tests.test_base import BaseTest

fake = Faker()


class TestFetchLectureView(BaseTest):
    def setUp(self):
        super(TestFetchLectureView, self).setUp()

    @pytest.mark.skipif(os.getenv('ENVIRONMENT') == 'testing', reason='seed data not loaded on Travis CI') # noqa
    def test_fetch_all_default_1(self):
        response = self.client.get('/lectures/0/0')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, data['current_page'])
        self.assertEqual(20, len(data['lectures']))
        self.assertIn('total_lectures', data)

    @pytest.mark.skipif(os.getenv('ENVIRONMENT') == 'development', reason='seed data not loaded on Travis CI') # noqa
    def test_fetch_all_default_2(self):
        response = self.client.get('/lectures/0/0')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, data['current_page'])
        self.assertEqual(0, len(data['lectures']))
        self.assertIn('total_lectures', data)

    def test_fetch_with_page_only(self):
        current_page = fake.random_int()
        response = self.client.get(f'/lectures/{current_page}/0')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(current_page, data['current_page'])

    def test_fetch_with_invalid_page_type(self):
        current_page = fake.word()
        response = self.client.get(f'/lectures/{current_page}/0')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data[
            'error'], 'only integers allowed for page numbers')

    def test_fetch_with_invalid_item_type(self):
        items_per_page = fake.word()
        response = self.client.get(f'/lectures/0/{items_per_page}')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data[
            'error'], 'only integers allowed for page numbers')


class TestFetchTopTenLectures(BaseTest):
    def setUp(self):
        super(TestFetchTopTenLectures, self).setUp()

    @pytest.mark.skipif(os.getenv('ENVIRONMENT') == 'testing', reason='seed data not loaded on Travis CI') # noqa
    def test_top_ten_lectures(self):
        response = self.client.get('/lectures/top-10')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIn('lectures', data)

    @pytest.mark.skipif(os.getenv('ENVIRONMENT') == 'development', reason='seed data not loaded on Travis CI') # noqa
    def test_top_ten_lectures_when_db_empty(self):
        response = self.client.get('/lectures/top-10')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertIn('error', data)
