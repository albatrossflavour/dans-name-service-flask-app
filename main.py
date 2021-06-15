import random
from flask import Flask

app = Flask(__name__)

name = [
        "Ringo",
        "Danny Boy",
        "Ringmaster",
        "Dan the man",
        "New guy",
        "Danno",
        "He who books people",
        "Book him Danno",
        "Not Paul, George or John",
        "That guy from Transurban",
        "Dan with the van",
        "d4n0",
        "01100100 01100001 01101110",
        "The ring bearer",
        "Ring-a-ding-ding",
        "Frodo",
        "DR",
        "DRing",
        "Oh Danny Boy",
        "Dan"
        ]

@app.route("/")
def index():
    return random.choice(name)
