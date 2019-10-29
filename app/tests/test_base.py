import unittest

from app import create_app


class BaseTest(unittest.TestCase):
    """
    A base class for tests that will do the setup and teardown
    """

    def setUp(self):
        self.app = create_app(config="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(self)

    def tearDown(self):
        self.app_context.pop()


if __name__ == '__main__':
    unittest.main()
