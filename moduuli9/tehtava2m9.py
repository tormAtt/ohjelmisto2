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

auto = Auto("ABC-123", 142)
print("Auton rekisteritunnus: " + auto.rTunnus + ", auton huippunopeus: " + str(auto.huippuNopeus) + " km/h, auton nykyinen nopeus: " + str(auto.nykyinenNopeus) + " km/h, auton kuljettu matka: " + str(auto.kuljettuMatka) + " km.")
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.nykyinenNopeus)

auto.kiihdyta(-200)
print(auto.nykyinenNopeus)