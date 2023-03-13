class Auto:
    def __init__(self, rTunnus, huippuNopeus, nykyinenNopeus=0, kuljettuMatka=0):
        self.rTunnus = rTunnus
        self.huippuNopeus = huippuNopeus
        self.nykyinenNopeus = nykyinenNopeus
        self.kuljettuMatka = kuljettuMatka

auto = Auto("ABC-123", 142)
print("Auton rekisteritunnus: " + auto.rTunnus + ", auton huippunopeus: " + str(auto.huippuNopeus) + " km/h, auton nykyinen nopeus: " + str(auto.nykyinenNopeus) + " km/h, auton kuljettu matka: " + str(auto.kuljettuMatka) + " km.")