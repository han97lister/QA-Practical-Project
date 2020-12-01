from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from service1.app import app

class TestBase( TestCase ) :
    def create_app(self):
        return app

class TestResponse( TestBase ) :

    #test for get and post request
    def test_ticket_shows(self):
        with patch( "requests.get" ) as g:
            with patch( "requests.post" ) as p:
                g.return_value.text = "ABC13579"
                p.return_value.text = "Nothing, please try again"

                response = self.client.get(url_for("index"))
                self.assertIn( b'ABC13579', response.data )
                self.assertIn( b'Nothing, please try again', response.data )