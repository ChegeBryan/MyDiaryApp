""""
test_api.py contains the various test cases for the api endpoints

"""
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

    def test_post_entry_content_type_is_json(self):
        """
        Tests if the content type of the header is returned
        is in json format
        """
        response = self.client.post(
            'api/v1/entries',
            json=self.entry,
            content_type='application/javascript'
        )

        self.assertTrue(response['status'] == 'failed')
        self.assertTrue(response['message'] == 'content-type must be application/json')
        self.assertEqual(response.statu_code, 401)

    def test_api_create_entry(self):
        """
        Test api can create entry (POST request)
        successful status code 201
        """
        response = self.client.post(
            '/api/v1/entries',
            json=self.entry
        )
        self.assertEqual(response.status_code, 201)

    def test_api_can_get_all_entries(self):
        """
        Tests api endpoint can get all the entries (GET request)
        successful status code 200
        """
        response = self.client.post(
            '/api/v1/entries',
            json=self.entry
        )
        self.assertEqual(response.status_code, 201)
        all_response = self.client.get(
            '/api/v1/entries',
            json=self.entry
        )
        self.assertEqual(all_response.status_code, 200)

    def test_api_can_get_entry_by_id(self):
        """
        Tests api can get a single entry by id (GET request)
        Successful status code 200
        """
        response = self.client.post(
            '/api/v1/entries',
            json=self.entry
        )
        self.assertEqual(response.status_code, 201)
        id_response = self.client.get(
            '/api/v1/entries/1',
            json=self.entry
        )
        self.assertEqual(id_response.status_code, 200)

    def test_api_can_update_an_entry(self):
        """
        Tests api can update a particular entry (PUT request)
        Success status code 201
        """
        response = self.client.post(
            '/api/v1/entries',
            json=self.entry
        )
        self.assertEqual(response.status_code, 201)
        response = self.client.put(
            '/api/v1/entries/1',
            json={
                'title': 'just edit',
                'journal': 'thats not what really happened'
            }
        )
        self.assertEqual(response.status_code, 201)