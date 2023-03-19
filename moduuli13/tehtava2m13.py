from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="1234",
    autocommit=True
)

app = Flask(__name__)
@app.route("/kenttä/<icao>")
def haeLentoKentta(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            vastaus = {
                "ICAO": icao,
                "Name": rivi[0],
                "Municipality": rivi[1]
            }
        jsonvast = json.dumps(vastaus)
        return Response(response=jsonvast, mimetype="application/json")
    else:
        vastaus = {
            "ICAO": icao,
            "Virhe": "lentokenttää ei löytynyt"
        }
        jsonvast = json.dumps(vastaus)
        return Response(response=jsonvast, mimetype="application/json")

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)