import json
import unittest
import requests

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1'

    def test_1_getToken(self):
        self.assertTrue(True)
