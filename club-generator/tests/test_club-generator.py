from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):
     def test_clubgen(self):
       response = self.client.post(url_for("generate_club"), json={"baby_name": "Brad","league_name": "League One"})
       self.assertEqual(response.status_code, 200)
       self.assertIn(b"Sunderland", response.data)