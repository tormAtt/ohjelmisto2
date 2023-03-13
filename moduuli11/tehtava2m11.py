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

class Sahkoauto(Auto):
    def __init__(self, rTunnus, huippuNopeus, akkuKapasiteetti):
        super().__init__(rTunnus, huippuNopeus)
        self.akkuKapasiteetti = akkuKapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rTunnus, huippuNopeus, bensaTankki):
        super().__init__(rTunnus, huippuNopeus)
        self.bensaTankki = bensaTankki

sahkoAuto = Sahkoauto("ABC-15", 180, 52.5)
polttoAuto = Polttomoottoriauto("ACD-123", 165, 32.3)

tunnit = 0
while True:
    sahkoAuto.kiihdyta(50)
    sahkoAuto.kulje(1)

    polttoAuto.kiihdyta(100)
    polttoAuto.kulje(1)

    print("Rekisteritunnus: " + str(sahkoAuto.rTunnus) + ", nykyinen nopeus: " + str(sahkoAuto.nykyinenNopeus) + " km/h, kuljettu matka:: " + str(sahkoAuto.kuljettuMatka) + " km, akun kapasiteetti:" + str(sahkoAuto.akkuKapasiteetti) + " kWh")
    print("Rekisteritunnus: " + str(polttoAuto.rTunnus) + ", nykyinen nopeus: " + str(polttoAuto.nykyinenNopeus) + "km/h , kuljettu matka: " + str(polttoAuto.kuljettuMatka) + " km, bensatankki:" + str(polttoAuto.bensaTankki) + " l")
    tunnit += 1
    if tunnit == 3:
        break