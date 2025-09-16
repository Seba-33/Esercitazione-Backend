
# Import the Flask module that has been installed.
from flask import Flask
from flask import send_file
from flask import jsonify
from markupsafe import escape

import json
import random

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)



# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"
    
# Annotation that allows the function to be hit at the specific URL (/books).
@app.route("/nba")
def nba():
    return send_file('nba.json')

@app.route("/random") 
def rnd():
# Checks to see if the name of the package is the run as the main package.
    f = open('nba.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return data['nba'][random.randrange(0,9)] #estrarre una riga a caso dal vettore data

@app.route('/nome/<name>')
def nom(name):
    with open('nba.json') as f:  # Usa il context manager per gestire il file
        data = json.load(f)
    # Se il file contiene una chiave 'nba', accedi a quella lista
    if 'nba' in data:
        players = data['nba']
    else:
        players = data
    for nba in players:
        if nba.get('name') == name:
            return jsonify(nba)  # Restituisce una risposta JSON valida
    return jsonify({'error': 'Giocatore non trovato'}), 404  # Gestione caso non trovato

@app.route('/eta/<int:age>')
def eta(age):
    f = open('nba.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    # show the post with the given id, the id is an integer
    return f'Eta {age}'

@app.route('/Altezza/<height>')
def altezza(height):
    f = open('nba.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    # show the subpath after /path/
    return f'Altezza {height}'

if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()



