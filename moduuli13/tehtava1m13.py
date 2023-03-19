from flask import Flask
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')

def alkuluku(luku):
    try:
        luku = int(luku)
        onko = True
        if luku <= 1:
            vastaus = {
                "Number": luku,
                "isPrime": False
            }
            return vastaus
        elif luku > 1:
            for i in range (2, luku):
                if luku % i == 0:
                    onko = False
        if onko == True:
            vastaus = {
                "Number": luku,
                "isPrime": True
            }
            return vastaus
        else:
            vastaus = {
                "Number": luku,
                "isPrime": False
            }
            return vastaus
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen merkki"
        }
        return vastaus

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)