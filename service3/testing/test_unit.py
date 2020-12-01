from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random

from service3.app import app

class TestBase( TestCase ) :
    def create_app(self):
        return app

class TestApp( TestBase ) :

    def test_get_number(self):

        num = [b"13579", b"24680", b"48582", b"09672", b"34167"]
        number = random.choices(num)

        response = self.client.get( url_for('get_number') )
        self.assertEqual( response.status_code, 200 )
        self.assertIn( response.data, number )