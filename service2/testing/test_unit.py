from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase( TestCase ):
    def create_app(self):
        return app

class TestApp( TestBase ):

    def test_letters(self):
        uppercase = [b"ABC", b"DEF", b"GHI", b"JKL", b"MNO"]
        response = self.client.get( url_for('letters') )
        self.assertEqual( response.status_code, 200 )
        self.assertIn( response.data, uppercase )