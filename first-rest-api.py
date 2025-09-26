
import mysql.connector
from flask import Flask, jsonify, render_template_string

# Connessione al database MySQL
# Assicurati che il database e le credenziali siano corretti.
mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123",
    database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

# Inizializzazione dell'applicazione Flask
app = Flask(__name__)

# Definizione della route principale.
@app.route("/")
def hello():
    return "<h1>Hello, World! Questo è un server per il database di Clash Royale.</h1>"

# Route 'air_transport' per visualizzare le unità con trasporto 'Air'.
@app.route("/air_transport")
def air_transport():
    try:
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport='Air'")
        myresult = mycursor.fetchall()
        # Converte il risultato in una lista di dizionari per un output JSON corretto.
        # Ottieni i nomi delle colonne dal cursore
        columns = [col[0] for col in mycursor.description]
        result = [dict(zip(columns, row)) for row in myresult]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route 'epic_units' per visualizzare le unità con rarità 'Epic'.
@app.route("/epic_units")
def epic_units():
    try:
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity='Epic'")
        myresult = mycursor.fetchall()
        # Converte il risultato in una lista di dizionari.
        columns = [col[0] for col in mycursor.description]
        result = [dict(zip(columns, row)) for row in myresult]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Nuova route: 'heavy_units' per visualizzare le unità con costo di elisir superiore a 5.
@app.route("/heavy_units")
def heavy_units():
    try:
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE ElixirCost > 5")
        myresult = mycursor.fetchall()
        # Converte il risultato in una lista di dizionari.
        columns = [col[0] for col in mycursor.description]
        result = [dict(zip(columns, row)) for row in myresult]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Nuova route: 'spell_units' per visualizzare le unità di tipo 'Spell'.
@app.route("/spell_units")
def spell_units():
    try:
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Type='Spell'")
        myresult = mycursor.fetchall()
        # Converte il risultato in una lista di dizionari.
        columns = [col[0] for col in mycursor.description]
        result = [dict(zip(columns, row)) for row in myresult]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route modificata per visualizzare tutti i dati in una tabella HTML.
@app.route("/getAllDataInHtml")
def getAllData():
    try:
        mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
        myresult = mycursor.fetchall()
        
        # Genera il contenuto della tabella HTML
        html_table = "<style>table, th, td {border: 1px solid black; border-collapse: collapse; padding: 8px; text-align: left;}</style>"
        html_table += "<table>"
        
        # Intestazioni delle colonne
        columns = [col[0] for col in mycursor.description]
        html_table += "<thead><tr>"
        for col_name in columns:
            html_table += f"<th>{col_name}</th>"
        html_table += "</tr></thead>"
        
        # Righe dei dati
        html_table += "<tbody>"
        for row in myresult:
            html_table += "<tr>"
            for cell in row:
                html_table += f"<td>{cell}</td>"
            html_table += "</tr>"
        html_table += "</tbody>"
        
        html_table += "</table>"
        
        return render_template_string("<h1>Tutte le Unità di Clash Royale</h1>" + html_table)
    except Exception as e:
        return f"<h1>Si è verificato un errore: {e}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

