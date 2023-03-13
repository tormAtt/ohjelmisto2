import random
from tabulate import tabulate
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

i = 0

for i in range(10):
    hNopeus = random.randint(100, 200)
    auto = Auto("ABC-" + str(i+1), hNopeus)
    autot.append(auto)
loppunut = False
while loppunut == False:
    for a in autot:
        nMuutos = random.randint(-10, 15)
        a.kiihdyta(nMuutos)
        a.kulje(1)
        if a.kuljettuMatka >= 10000:
            loppunut = True
else:
    head = ["Rekisteritunnus", "Huippunopeus", "Nykyinen nopeus", "Kuljettu matka"]
    mydata = []
    for a in autot:
        mydata.append([a.rTunnus, a.huippuNopeus, a.nykyinenNopeus, a.kuljettuMatka])
    print(tabulate(mydata, headers=head, tablefmt="grid"))

#for a in autot:
    #print(a.rTunnus + ", " + str(a.huippuNopeus))

