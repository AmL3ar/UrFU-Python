import unittest

from tests_work.flask_rabotaem4 import app



class TestVAlidatorAddress(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_validator_correct_address(self):
        response = self.app.post("/registration", data = {"email": "art@mail.ru",
                                                          "phone": "9521480579",
                                                          "name": "Artem",
                                                          "address": "oblast",
                                                          "index": "620222",
                                                          "comment": "tut"})
        self.assertEqual(response.status_code, 200)

    def test_validator_address_incorrect(self):
        response = self.app.post("/registration", data={"email": "rt@mail.ru",
                                                        "phone": "95214805799",
                                                        "name": "Artem",
                                                        "address": "",
                                                        "index": "620222",
                                                        "comment": "tut"})
        self.assertEqual(response.status_code, 400)


