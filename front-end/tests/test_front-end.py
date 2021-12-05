from flask import url_for
from flask_testing import TestCase
import requests_mock
import pytest
from application import app, db
from application.models import babies

class TestBase(TestCase):
    def create_app(self):

        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                DEBUG=True,
                )
        return app

    def setUp(self):
        db.create_all()
        sample = babies(baby_name="Brad", league_name= "League One", club_name= "Sunderland")
        db.session.add(sample)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
  
    def test_gen(self):
        with requests_mock.Mocker() as m:
            m.get("http://name-generator:5000/name", json={"name":"Travis"})
            m.get("http://league-generator:5000/league", json={"league_name":"Premier League"})
            m.post("http://club-generator:5000/club", text="Liverpool")
            response = self.client.get(url_for('generator'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Brad', response.data)
            self.assertIn(b'Travis', response.data)
