import random
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'dans-name-service',
})

db = firestore.client()

names_ref = db.collection(u'names')
docs = names_ref.stream()
name = []

for doc in docs:
    line = doc.to_dict()
    name.append(line['name'])

app = Flask(__name__)

@app.route("/")
def index():
    return random.choice(name)
