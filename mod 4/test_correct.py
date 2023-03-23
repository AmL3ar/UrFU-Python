import unittest

from flask_rabotaem4 import *

class TestEmail(unittest.TestCase):  

    def test_email_correct(self):
        clin = app.test_client()
        bia = clin.post('/', data = {
            "email" : "biba@mail.ru",
            "phone" : 12345678910,
            "name" : "Артик Зверев",
            "address":"Деревня",            
            "index": 62022,
            "comment": "двор"
        })
        print(bia.data)          
