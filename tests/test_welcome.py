import unittest
from app import app


class TestWelcome(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_landing_page(self):
    # When
        response = self.app.get('/')
    # Then
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, b'Welcome to the RESTful API Server for DreamHome!')
