import unittest
import requests


class CodeExecutionTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'

    def test_code_execution_success(self):
        url = f'{self.base_url}/execute'
        data = {'code': 'print("Hello, World!")', 'timeout': 5}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 'Hello, World!'})

    def test_code_execution_timeout(self):
        url = f'{self.base_url}/execute'
        data = {'code': 'import time\n\ntime.sleep(10)', 'timeout': 5}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'message': 'Execution timed out.'})

    def test_invalid_input(self):
        url = f'{self.base_url}/execute'
        data = {'code': '', 'timeout': -1}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': {'code': ['This field is required.'], 'timeout': ['Number must be between 1 and 30.']}})


if __name__ == '__main__':
    unittest.main()