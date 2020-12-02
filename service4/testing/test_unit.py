import unittest
import requests

from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from service4.app import app

class TestBase( TestCase ) :
    def create_app(self):
        return app

class TestApp( TestBase ) :

    def test_get_ticket(self):

        response = self.client.get( url_for('prize') )
        self.assertEqual( response.status_code, 200 )
        self.assertIn( b'ticket', response.data ) 
    
   # def test_post_prize(self):

    #    response = self.client.post( url_for('prize') )
    #    self.assertEqual( response.status_code, 200 )
    #    self.assertIn( b'DEF09672', response.data )
    #    self.assertIn( b'Nothing, please try again', response.data )
    
    def test_get_ticket(self):
        with patch( 'requests.post' ) as g:
            g.return_value.text = "GHI09672"

            response = self.client.post(url_for('prize'))
            self.assertIn(b'Congratulations, You have won £200', response.data)
            self.assertEqual(response.status_code, 200)