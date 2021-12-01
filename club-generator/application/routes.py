from application import app
from flask import Flask, request, Response, jsonify
import random
import requests

@app.route('/club', methods=['GET', 'POST'])
def generate_club():
    league_name=request.get_json()["league_name"]
    baby_name=request.get_json()["baby_name"]

#prem
    if baby_name == "Travis" or "Oliver" and league_name == "Premier League":
        club_name = "Liverpool"

    if baby_name == "Brad" or "Emma" and league_name == "Premier League":
        club_name = "Chelsea"
    
    if baby_name == "Ethan" or "Noah" and league_name == "Premier League":
        club_name = "Manchester City"
    
    if baby_name == "Liam" and league_name == "Premier League":
        club_name = "West Ham"
    
    if baby_name == "Amelia" and league_name == "Premier League":
        club_name = "Arsenal"
    
    if baby_name == "Olivia" and league_name == "Premier League":
        club_name = "Wolves"
    
    if baby_name == "Elijah" and league_name == "Premier League":
        club_name = "Spurs"
    
    if baby_name == "Ava" and league_name == "Premier League":
        club_name = "Manchester United"
    
    if baby_name == "Lucas" and league_name == "Premier League":
        club_name = "Brighton"
    
    if baby_name == "Levi" and league_name == "Premier League":
        club_name = "Leicester"
    
    if baby_name == "Sophia" and league_name == "Premier League":
        club_name = "Crystal Palace"
    
    if baby_name == "Charlotte" and league_name == "Premier League":
        club_name = "Brentford"
    
    if baby_name == "Mason" and league_name == "Premier League":
        club_name = "Aston Villa"
    
    if baby_name == "Isabella" and league_name == "Premier League":
        club_name = "Everton"
    
    if baby_name == "Asher" and league_name == "Premier League":
        club_name = "Southampton"
    
    if baby_name == "Mia" and league_name == "Premier League":
        club_name = "Watford"

    if baby_name == "Ryan" or "Grant" and league_name == "Premier League":
        club_name = "Leeds"
    
    if baby_name == "James" and league_name == "Premier League":
        club_name = "Burnley"
    
    if baby_name == "Luna" and league_name == "Premier League":
        club_name = "Norwich"
    
    if baby_name == "Harper" and league_name == "Premier League":
        club_name = "Newcastle"

#championship
    if baby_name == "Liam" and league_name == "Championship":
        club_name = "Fulham"

    if baby_name == "Noah" and league_name == "Championship":
        club_name = "Bournemouth"

    if baby_name == "Oliver" and league_name == "Championship":
        club_name = "QPR"

    if baby_name == "Elijah" and league_name == "Championship":
        club_name = "West Brom"

    if baby_name == "Lucas" and league_name == "Championship":
        club_name = "Blackburn"

    if baby_name == "Levi" and league_name == "Championship":
        club_name = "Coventry"

    if baby_name == "Mason" and league_name == "Championship":
        club_name = "Stoke"

    if baby_name == "Asher" and league_name == "Championship":
        club_name = "Huddersfield"

    if baby_name == "James" and league_name == "Championship":
        club_name = "Swansea"

    if baby_name == "Ethan" and league_name == "Championship":
        club_name = "Millwall"

    if baby_name == "Grant" and league_name == "Championship":
        club_name = "Blackpool"

    if baby_name == "Travis" and league_name == "Championship":
        club_name = "Middlesbrough"

    if baby_name == "Brad" and league_name == "Championship":
        club_name = "Sheffield United"

    if baby_name == "Ryan" and league_name == "Championship":
        club_name = "Birmingham"

    if baby_name == "Olivia" and league_name == "Championship":
        club_name = "Luton"

    if baby_name == "Emma" and league_name == "Championship":
        club_name = "Nottingham Forest"

    if baby_name == "Ava" and league_name == "Championship":
        club_name = "Preston"

    if baby_name == "Sophia" and league_name == "Championship":
        club_name = "Bristol City"

    if baby_name == "Charlotte" and league_name == "Championship":
        club_name = "Hull City"

    if baby_name == "Isabella" and league_name == "Championship":
        club_name = "Cardiff"

    if baby_name == "Mia" and league_name == "Championship":
        club_name = "Reading"

    if baby_name == "Luna" and league_name == "Championship":
        club_name = "Peterborough"

    if baby_name == "Harper" and league_name == "Championship":
        club_name = "Barnsley"

    if baby_name == "Amelia" and league_name == "Championship":
        club_name = "Derby"
    
#League one
    if baby_name == "Olivia" and league_name == "League One":
        club_name = "Rotherham"

    if baby_name == "Amelia" and league_name == "League One":
        club_name = "Wigan"

    if baby_name == "Ava" and league_name == "League One":
        club_name = "Wycombe"

    if baby_name == "Sophia" and league_name == "League One":
        club_name = "Plymouth"

    if baby_name == "Brad" and league_name == "League One":
        club_name = "Sunderland"

    if baby_name == "Charlotte" and league_name == "League One":
        club_name = "MK Dons"

    if baby_name == "Isabella" and league_name == "League One":
        club_name = "Sheffield Wednesday"

    if baby_name == "Mia" and league_name == "League One":
        club_name = "Oxford United"

    if baby_name == "Luna" and league_name == "League One":
        club_name = "Portsmouth"

    if baby_name == "Harper" and league_name == "League One":
        club_name = "Burton Albion"

    if baby_name == "Liam" and league_name == "League One":
        club_name = "Ipswich"

    if baby_name == "Noah" and league_name == "League One":
        club_name = "Cheltenham"

    if baby_name == "Oliver" and league_name == "League One":
        club_name = "Bolton"

    if baby_name == "Elijah" and league_name == "League One":
        club_name = "Accrington Stanley"

    if baby_name == "Lucas" and league_name == "League One":
        club_name = "Charlton"

    if baby_name == "Levi" and league_name == "League One":
        club_name = "Cambridge United"

    if baby_name == "Mason" and league_name == "League One":
        club_name = "AFC Wimbledon"

    if baby_name == "Asher" and league_name == "League One":
        club_name = "Lincoln City"

    if baby_name == "James" and league_name == "League One":
        club_name = "Shrewsbury"

    if baby_name == "Ethan" and league_name == "League One":
        club_name = "Morecambe"

    if baby_name == "Travis" and league_name == "League One":
        club_name = "Gillingham"

    if baby_name == "Ryan" and league_name == "League One":
        club_name = "Fleetwood"

    if baby_name == "Grant" and league_name == "League One":
        club_name = "Doncaster Rovers"

    if baby_name == "Emma" and league_name == "League One":
        club_name = "Crewe Alexandra"
    
#League two
    if baby_name == "Grant" and league_name == "League Two":
        club_name = "Forest Green"

    if baby_name == "Ryan" and league_name == "League Two":
        club_name = "Northampton"

    if baby_name == "Travis" and league_name == "League Two":
        club_name = "Exeter City"

    if baby_name == "Brad" and league_name == "League Two":
        club_name = "Swindon"

    if baby_name == "Ethan" and league_name == "League Two":
        club_name = "Port Vale"

    if baby_name == "James" and league_name == "League Two":
        club_name = "Sutton United"

    if baby_name == "Asher" and league_name == "League Two":
        club_name = "Harrogate Town"

    if baby_name == "Mason" and league_name == "League Two":
        club_name = "Leyton Orient"

    if baby_name == "Levi" and league_name == "League Two":
        club_name = "Newport County"

    if baby_name == "Lucas" and league_name == "League Two":
        club_name = "Tranmere"

    if baby_name == "Elijah" and league_name == "League Two":
        club_name = "Salford City"

    if baby_name == "Oliver" and league_name == "League Two":
        club_name = "Bradford"

    if baby_name == "Noah" and league_name == "League Two":
        club_name = "Rochdale"

    if baby_name == "Liam" and league_name == "League Two":
        club_name = "Walsall"

    if baby_name == "Harper" and league_name == "League Two":
        club_name = "Mansfield"

    if baby_name == "Luna" and league_name == "League Two":
        club_name = "Bristol Rovers"

    if baby_name == "Mia" and league_name == "League Two":
        club_name = "Hartlepool"

    if baby_name == "Isabella" and league_name == "League Two":
        club_name = "Colchester"

    if baby_name == "Charlotte" and league_name == "League Two":
        club_name = "Crawley Town"

    if baby_name == "Sophia" and league_name == "League Two":
        club_name = "Barrow"

    if baby_name == "Ava" and league_name == "League Two":
        club_name = "Stevenage"

    if baby_name == "Amelia" and league_name == "League Two":
        club_name = "Carlisle"

    if baby_name == "Emma" and league_name == "League Two":
        club_name = "Oldham"

    if baby_name == "Olivia" and league_name == "League Two":
        club_name = "Scunthorpe"
    




    return Response(club_name, mimetype='text/plain')