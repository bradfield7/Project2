from application import app, db
from flask import Flask, request, render_template
from application.models import babies
import requests
  
  
  
@app.route('/', methods=['GET']) 
def generator():
  league_name=requests.get("http://league-generator:5000/league")
  baby_name=requests.get("http://name-generator:5000/name")
  club_name=requests.post("http://club-generator:5000/club", json = {"baby_name": baby_name.json()["name"], "league_name": league_name.json()["league_name"]})
  show5 = babies.query.order_by(babies.id.desc()).limit(5).all()
  db.session.add(babies(baby_name=baby_name.json()["name"], league_name=league_name.json()["league_name"], club_name=club_name.text))
  db.session.commit()

  return render_template('home.html', baby=baby_name.json()["name"], league=league_name.json()["league_name"], club=club_name.text, show5 = show5)


#baby = 
  
  #
  
  
  #, show5 = show5)