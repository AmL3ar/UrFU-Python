import unittest
from datetime import datetime

from flask_rabotaem3 import app

week = ("понедельника","вторника","среды","четверга","пятницы","субботы","воскресенья")

class TestHelloWordWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'
    
    def get_weekday(self):
        today = datetime.datetime.today().weekday()
        return week[today]
    
    def test_can_get_correct_username_with_weekdate(self):
        username = "Саша"
        weekday = self.get_weekday()
        res = self.app.get(self.base_url + username)
        res_str = res.data.decode()
        self.assertTrue(weekday in res_str)