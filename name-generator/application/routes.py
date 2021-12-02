from application import app
from flask import Flask, request, Response, jsonify
import random

@app.route('/name', methods=['GET'])
def generate_name():
    words = [
        "Olivia", "Emma", "Amelia", "Ava", "Sophia", "Charlotte", "Isabella", "Mia", "Luna", "Harper",
         "Liam", "Noah", "Oliver", "Elijah", "Lucas", "Levi", "Mason", "Asher", "James", "Ethan", "Brad", "Travis", "Ryan", "Grant"
    ]

    choice = random.choice(words)
    baby_name = { "name" : choice}
    return jsonify(baby_name)