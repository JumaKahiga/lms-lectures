import json
from faker import Faker

from app.tests.test_base import BaseTest

fake = Faker()


class TestLoginView(BaseTest):
    def setUp(self):
        super(TestLoginView, self).setUp()

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

    def test_admin_login_successfully(self):
        self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')

        response = self.client.post(
            'admin/login',
            data=json.dumps(self.admin),
            content_type='application/json')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data.get('message'), 'login successful')
        self.assertIn('access_token', data.get('tokens'))

    def test_user_login_successfully(self):
        self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')

        response = self.client.post(
            'user/login',
            data=json.dumps(self.user),
            content_type='application/json')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data.get('message'), 'login successful')
        self.assertIn('access_token', data.get('tokens'))

    def test_admin_email_not_found(self):
        response = self.client.post(
            'admin/login',
            data=json.dumps(self.admin),
            content_type='application/json')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            data.get(
                'error'),
            f'user with the email {self.admin.get("email")} does not exist')

    def test_user_email_not_found(self):
        response = self.client.post(
            'user/login',
            data=json.dumps(self.user),
            content_type='application/json')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            data.get(
                'error'),
            f'user with the email {self.user.get("email")} does not exist')

    def test_admin_wrong_password(self):
        self.client.post(
            '/admin/register',
            data=json.dumps(self.admin),
            content_type='application/json')

        self.admin['password'] = fake.password()

        response = self.client.post(
            '/admin/login',
            data=json.dumps(self.admin),
            content_type='application/json')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get('error'), 'password and email did not match')

    def test_user_wrong_password(self):
        self.client.post(
            '/user/register',
            data=json.dumps(self.user),
            content_type='application/json')

        self.user['password'] = fake.password()

        response = self.client.post(
            '/user/login',
            data=json.dumps(self.user),
            content_type='application/json')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get('error'), 'password and email did not match')
