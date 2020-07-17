import unittest
from unittest import mock
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import client

class ClientTestCase(unittest.TestCase):
    def test_success_request(self):
        with mock.patch('lib.client.requests.get') as patcher:
            patcher.return_value = "200"
            self.assertEqual(client.send_request())