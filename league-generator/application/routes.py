from application import app
from flask import Flask, request, Response, jsonify
import random

@app.route('/league', methods=['GET'])
def generate_name():
    words = [
        "Premier League", "Championship", "League One", "League Two"
    ]
    choice = random.choice(words)
    league_name = { "league" : choice}
    return Response(league_name, mimetype='text/plain')
