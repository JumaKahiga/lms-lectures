import unittest
from app import create_app


class BaseTest(unittest.TestCase):
    """
    A base class for tests that will do the setup and teardown
    """

    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client(self)

    def tearDown(self):
        pass


class TestView(BaseTest):
    def test_init_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
