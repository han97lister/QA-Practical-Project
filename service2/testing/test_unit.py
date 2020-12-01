from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase( TestCase ):
    def create_app(self):
        return app

class TestApp( TestBase ):

    def test_letters(self):
        response = self.client.get( url_for('letters') )
        self.assertEqual( response.status_code, 200 )
        #self.assertIn( b'uppercase', response.data )