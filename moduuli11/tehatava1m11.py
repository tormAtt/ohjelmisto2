class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def GetNimi(self):
        return self.nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print("Nimi: " + str(super().GetNimi()) + ", kirjoittaja: " + str(self.kirjoittaja) + ", sivumäärä: " + str(self.sivumaara))
class Lehti(Julkaisu):
    def __init__(self, nimi, paaToimittaja):
        self.paaToimittaja = paaToimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print("Nimi: " + str(super().GetNimi()) + ", päätoimittaja: " + str(self.paaToimittaja))


a = Lehti("Aku Ankka", "Aki Hyyppä")
b = Kirja("Hytti n:0 6", "Rosa Liksom", 200)
a.tulosta_tiedot()
b.tulosta_tiedot()