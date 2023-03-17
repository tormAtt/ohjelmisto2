import requests
import json

pKunta = input("Anna paikkakunnan nimi: ")

pyynto = f"http://api.openweathermap.org/data/2.5/weather?q={pKunta}&units=metric&APPID=6061547615588e25d10e0648ce5e849b"
#print(pyynto)
vastaus = requests.get(pyynto).json()

#print(vastaus)
print("Säätila: " + vastaus["weather"][0]["description"] + ", lämpötila: " + str(vastaus["main"]["temp"]) + " celsius astetta")