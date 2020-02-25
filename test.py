import os
import unittest
from app import app
from flask import Flask

myapp = Flask(__name__)

class MyTestClass(unittest.TestCase): 
    
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    @classmethod
    def tearDownClass(cls):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 