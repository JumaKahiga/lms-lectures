import json
from faker import Faker

from app import create_app
from app.models.person_model import Person
from app.tests.factories.person_factory import (
    AdminFactory, UserFactory)
from app.tests.test_base import BaseTest

fake = Faker()


class TestRegistrationView(BaseTest):
    def setUp(self):
        super(TestRegistrationView, self).setUp()

        self.admin = {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password()
            }

        self.user = {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password(),
            "bio": fake.text()
            }

    def test_admin_creation(self):
        response = self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            data.get('message'), 'Admin registered successfully')
        self.assertIn(self.admin.get('email'), data.get('data'))

    def test_user_creation(self):
        response = self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            data.get('message'), 'User registered successfully')
        self.assertIn(self.user.get('email'), data.get('data'))

    def test_invalid_admin_name(self):
        self.admin['name'] = fake.random_int()
        response = self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data.get('error'), 'invalid characters used for name')

    def test_invalid_user_name(self):
        self.user['name'] = fake.random_int()
        response = self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data.get('error'), 'invalid characters used for name')

    def test_invalid_admin_email(self):
        self.admin['email'] = fake.name()
        response = self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data.get('error'), 'invalid email')

    def test_invalid_user_email(self):
        self.user['email'] = fake.name()
        response = self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data.get('error'), 'invalid email')

    def test_existent_admin_email(self):
        self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')
        response = self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data.get('error'),
            f'an admin with the email {self.admin.get("email")} already exists')

    def test_existent_user_email(self):
        self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')
        response = self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data.get('error'),
            f'a user with the email {self.user.get("email")} already exists')
