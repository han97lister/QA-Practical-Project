import unittest
import requests

from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from service4.app import app

class TestBase( TestCase ) :
    def create_app(self):
        return app

class TestApp( TestBase ) :

    def test_ticket_won_200(self):

        response = self.client.post(
            url_for('prize'),
            data='GHI09672',
            follow_redirects=True
        )
        self.assertIn( b'Congratulations, You have won 200', response.data ) 
    
    def test_ticket_won_100(self):

        response = self.client.post(
            url_for('prize'),
            data='ABC24680',
           follow_redirects=True
        )
        self.assertIn( b"Congratulations, You have won 100", response.data )
    
    def test_ticket_won_nothing(self):

        response = self.client.post(
            url_for('prize'),
            data='DEF09672',
           follow_redirects=True
        )
        self.assertIn( b"Nothing, please try again", response.data )
    