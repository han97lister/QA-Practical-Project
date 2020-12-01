from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from service3.app import app

class TestBase( TestCase ) :
    def create_app(self):
        return app

class TestApp( TestBase ) :

    def test_get_number(self):
        response = self.client.get( url_for('get_number') )
        self.assertEqual( response.status_code, 200 )
        #self.assertIn( b'number', response.data )