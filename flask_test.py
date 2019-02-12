import os
import unittest
import requests
import json
from jsonschema import validate

url = "http://localhost:5000"
auth = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDc1Mjk5OTQsIm5iZiI6MTU0NzUy" \
       "OTk5NCwianRpIjoiMjMyZDIwODktYTg0ZS00NDY0LTk4MTYtNGQ2ZGExOGUyY2JmIiwiZXhwIjoxNTQ3NTMw" \
       "ODk0LCJpZGVudGl0eSI6MiwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MiLCJ1c2VyX2NsYWltcyI6eyJpc" \
       "19hZG1pbiI6ZmFsc2V9fQ.jVHKq3LFGel3dlxa8ku67auUILOqPFpZYI_9Jem75AE"
def isItLogin():
    #valid login
    #login again
    pass
store_schema = open("store_schema.json").read().rstrip()
class FlaskTest(unittest.TestCase):

    def setup(self):
        pass

    def test_00_register_NEW_USER(self):
        try:
            payload = json.dumps({"username": "rm", "password": "1234"})
            headers = {"content-type": "application/json"}
            response = requests.request("POST", os.path.join(url, 'register'), data=payload, headers=headers)

            self.assertEqual(response.status_code, 200, "test_00_register_NEW_USER")

        except Exception as e:
            print(e.args)

    def test_01_login_POSITIVE(self):
        try:
            payload = json.dumps({"username": "rm", "password": "1234"})
            headers = {"content-type": "application/json"}
            response = requests.request("POST", os.path.join(url, 'login'), data=payload, headers=headers)
            self.assertEqual(response.status_code, 200, "test_01_login_POSITIVE")
        except Exception as e:
            print(e.args)

    @isItLogin
    def test_02_register_DUPLICATE_USER(self):
        try:
            payload = json.dumps({"username": "rm", "password": "1234"})
            headers = {"content-type": "application/json"}
            response = requests.request("POST", os.path.join(url, 'register'), data=payload, headers=headers)
            self.assertTrue(False)
            self.assertEqual(response.status_code, 200, "test_02_register_DUPLICATE_USER")
        except Exception as e:
            print(e.args)

    def test_03_getStores(self):
        try:
            headers = {"content-type": "application/json"}
            response = requests.request("GET", os.path.join(url, 'stores'), headers=headers)
            self.assertEqual(response.status_code, 200, "test_03_getStores")
            validate({"name": "newstore",
                      "items": [
                          {
                              "id": 1,
                              "name": "piano",
                              "price": 17.99,
                              "store_id": 1
                          }
                      ]}, json.loads(store_schema))
        except Exception as e:
            print(e.args)

    def test_04_NEW_STORE(self):
        try:
            payload = json.dumps({"name": "newStore"})
            headers = {"content-type": "application/json", "Authorization": auth}
            response = requests.request("POST", os.path.join(url, 'store'), data=payload, headers=headers)
            self.assertEqual(response.status_code, 404, "test_04_NEW_STORE")
        except Exception as e:
            print(e.args)

    def test_05_NEW_ITEM(self):
        try:
            payload = json.dumps({"price": "20.00", "store_id": "1"})
            headers = {"content-type": "application/json", "Authorization": auth}
            response = requests.request("PUT", os.path.join(url, 'register'), data=payload, headers=headers)
            self.assertEqual(response.status_code, 404, "test_05_NEW_ITEM")

        except Exception as e:
            print(e.args)
