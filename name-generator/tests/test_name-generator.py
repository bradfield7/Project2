from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):
     def test_namegen(self):
       with patch('random.choice') as r:
           r.return_value = "Brad"
           response = self.client.get(url_for('generate_name'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'Brad', response.data)