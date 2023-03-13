import random
from tabulate import tabulate
class Kilpailu:
    def __init__ (self, nimi, pituus, autoLista):
        self.nimi = nimi
        self.pituus = pituus
        self.autoLista = autoLista

    def tunti_kuluu(self):
        for a in self.autoLista:
            nMuutos = random.randint(-10, 15)
            a.kiihdyta(nMuutos)
            a.kulje(1)

    def tulosta_tilanne(self):
        head = ["Rekisteritunnus", "Huippunopeus", "Nykyinen nopeus", "Kuljettu matka"]
        mydata = []
        for a in self.autoLista:
            mydata.append([a.rTunnus, a.huippuNopeus, a.nykyinenNopeus, a.kuljettuMatka])
        print(tabulate(mydata, headers=head, tablefmt="grid"))

    def kilpailu_ohi(self):
        for a in self.autoLista:
            if a.kuljettuMatka >= self.pituus:
                return True
        return False

class Auto:
    def __init__(self, rTunnus, huippuNopeus, nykyinenNopeus=0, kuljettuMatka=0):
        self.rTunnus = rTunnus
        self.huippuNopeus = huippuNopeus
        self.nykyinenNopeus = nykyinenNopeus
        self.kuljettuMatka = kuljettuMatka

    def kiihdyta(self, nMuutos):
        self.nykyinenNopeus += nMuutos
        if self.nykyinenNopeus < 0:
            self.nykyinenNopeus = 0
        elif self.nykyinenNopeus > self.huippuNopeus:
            self.nykyinenNopeus = self.huippuNopeus

    def kulje(self, tuntiMaara):
        self.kuljettuMatka += self.nykyinenNopeus * tuntiMaara

autot = []

for i in range(10):
    hNopeus = random.randint(100, 200)
    auto = Auto("ABC-" + str(i+1), hNopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while True:
    kilpailu.tunti_kuluu()
    tunnit += 1
    if kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()
        break
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
