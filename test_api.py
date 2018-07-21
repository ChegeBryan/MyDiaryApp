import unittest
from app import app
from instance.config import config_environment


class EntryTestCase(unittest.TestCase):
    """
    Class fot entries endpoints cases
    """

    def setUp(self):
        """
        Define the entry variables and initialize the app
        """
        self.app = app
        self.app.config.from_object(config_environment['testing'])
        self.client = self.app.test_client()
        self.entry = {
            'id': 1,
            'title': 'Just flask',
            'journal': 'using flask to develop api endpoints'
        }

    def tearDown(self):
        pass