from application import app
from flask import Flask, request, Response, jsonify
import random
import requests

prem = {
        "Olivia":"Wolves",
        "Emma":"Chelsea",
        "Amelia":"Arsenal",
        "Ava":"Manchester United",
        "Sophia":"Crystal Palace",
        "Charlotte":"Brentford",
        "Isabella":"Everton",
        "Mia":"Watford",
        "Luna":"Norwich",
        "Harper":"Newcastle",
        "Liam":"West Ham",
        "Noah":"Manchester City",
        "Oliver":"Liverpool",
        "Elijah":"Spurs",
        "Lucas":"Brighton",
        "Levi":"Leicester",
        "Mason":"Aston Villa",
        "Asher":"Southampton",
        "James":"Burnley",
        "Ethan":"Manchester City",
        "Brad":"Chelsea",
        "Travis":"Liverpool",
        "Ryan":"Leeds",
        "Grant":"Leeds"
    }


champs = {
        "Olivia":"Luton",
        "Emma":"Nottingham Forest",
        "Amelia":"Derby",
        "Ava":"Preston",
        "Sophia":"Bristol City",
        "Charlotte":"Hull City",
        "Isabella":"Cardiff",
        "Mia":"Reading",
        "Luna":"Peterborough",
        "Harper":"Barnsley",
        "Liam":"Fulham",
        "Noah":"Bournemouth",
        "Oliver":"QPR",
        "Elijah":"West Brom",
        "Lucas":"Blackburn",
        "Levi":"Coventry",
        "Mason":"Stoke",
        "Asher":"Huddersfield",
        "James":"Swansea",
        "Ethan":"Millwall",
        "Brad":"Sheffield United",
        "Travis":"Middlesbrough",
        "Ryan":"Birmingham",
        "Grant":"Blackburn"
}

one = { "Olivia":"Rotheram",
        "Emma":"Crewe Alexandra",
        "Amelia":"Wigan",
        "Ava":"Wycombe",
        "Sophia":"Plymouth",
        "Charlotte":"MK Dons",
        "Isabella":"Sheffield Wednesday",
        "Mia":"Oxford United",
        "Luna":"Portsmouth",
        "Harper":"Burton Albion",
        "Liam":"Ipswich",
        "Noah":"Cheltenham",
        "Oliver":"Bolton",
        "Elijah":"Accrington Stanley",
        "Lucas":"Charlton",
        "Levi":"Cambridge United",
        "Mason":"AFC Wimbledon",
        "Asher":"Lincoln City",
        "James":"Shrewsbury",
        "Ethan":"Morecambe",
        "Brad":"Sunderland",
        "Travis":"Gillingham",
        "Ryan":"Fleetwood",
        "Grant":"Doncaster Rovers"
}


two = {  "Olivia":"Scunthorpe",
        "Emma":"Oldham",
        "Amelia":"Carlisle",
        "Ava":"Stevenage",
        "Sophia":"Barrow",
        "Charlotte":"Crawley Town",
        "Isabella":"Colchester",
        "Mia":"Hartlepool",
        "Luna":"Bristol Rovers",
        "Harper":"Mansfield",
        "Liam":"Walsall",
        "Noah":"Rochdale",
        "Oliver":"Bradford",
        "Elijah":"Salford City",
        "Lucas":"Tranmere",
        "Levi":"Newport County",
        "Mason":"Leyton Orient",
        "Asher":"Harrogate Town",
        "James":"Sutton United",
        "Ethan":"Port Vale",
        "Brad":"Swindon",
        "Travis":"Exeter City",
        "Ryan":"Northampton",
        "Grant":"Forest Green"
}

@app.route('/club', methods=['GET', 'POST'])
def generate_club():
    league_name=request.get_json()["league_name"]
    baby_name=request.get_json()["baby_name"]
    leagues_list = {"Premier League": prem, "Championship": champs, "League One": one, "League Two": two}

    league = leagues_list[league_name]

    club_name = league[baby_name]
    
    return Response(club_name, mimetype="text/plain")