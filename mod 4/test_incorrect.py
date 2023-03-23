import unittest

from flask_rabotaem4 import *

class TestEmail(unittest.TestCase): 
    def test_email_incorrect(self):
        clin = app.test_client()
        bia = clin.post('/', data = {
            "email" : "biba.ru",
            "phone" : 1234567891011,
            "name" : "Артик Зверев1",
            "address":"Деревня1",           
            "index": 620221,
            "comment": "двор1"
        })
        print()
        
        

                      