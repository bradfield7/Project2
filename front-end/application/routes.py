from application import app, db
from flask import Flask, request, render_template
from application.models import babies
import requests
  
  
  
@app.route('/', methods=['GET']) 
def generator():
  league_name=requests.get("http://league-generator:5000/league")
  baby_name=requests.get("http://name-generator:5000/name")
  club_name = requests.post("http://club-generator:5000/club", json={"league_name":league_name, "baby_name":baby_name})
  return render_template('home.html', baby=baby_name.text, league=league_name.text, club=club_name.text)

  if league_name == 'League One' or league_name == 'League Two':
    print(f'Your baby {baby_name} is going to support {club_name} from {league_name}!')
  else:
    print(f'Your baby {baby_name} is going to support {club_name} from the {league_name}!')