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

auto = Auto("ABC-123", 142)
auto.kiihdyta(60)
auto.kulje(1.5)
auto.kulje(2)
print(str(auto.kuljettuMatka) + " km")