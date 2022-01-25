import requests
import unittest

from unittest.mock import Mock, patch


class TestSortPet(unittest.TestCase):
    @patch("requests.get")
    def test_get_apí_root_path(self, mocked_request):
        mocked_request.return_value = Mock(status_code=200)
        response = requests.get("http://localhost:5000/api/v1/")

        self.assertEqual(response.status_code, 200)

    @patch("requests.post")
    def test_post_apí_root_path(self, mocked_request):
        mocked_request.return_value = Mock(status_code=200)
        response = requests.post("http://localhost:5000/api/v1/")

        self.assertEqual(response.status_code, 200)

    @patch("requests.post")
    def test_post_without_fields_apí_root_path(self, mocked_request):
        mocked_request.return_value = Mock(status_code=400)
        response = requests.post("http://localhost:5000/api/v1/")
        self.assertEqual(response.status_code, 400)
