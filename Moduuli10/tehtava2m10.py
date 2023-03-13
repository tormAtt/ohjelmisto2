class Hissi:
    def __init__(self, alinK, ylinK):
        self.alinK = alinK
        self.ylinK = ylinK
        self.nykyinenK = alinK

    def kerrosYlos(self):
        self.nykyinenK += 1
        print(self.nykyinenK)

    def kerrosAlas(self):
        self.nykyinenK -= 1
        print(self.nykyinenK)
    def siirryKerrokseen(self, kerros):
        if self.nykyinenK > kerros:
            while self.nykyinenK > kerros:
                if self.nykyinenK == self.alinK:
                    break;
                else:
                    self.kerrosAlas()
        elif self.nykyinenK < kerros:
            while self.nykyinenK < kerros:
                if self.nykyinenK == self.ylinK:
                    break;
                else:
                    self.kerrosYlos()

class Talo:
    def __init__(self, alinK, ylinK, hissiMaara):
        self.alinK = alinK
        self.ylinK = ylinK
        self.hissit = []
        i = 0
        for i in range(hissiMaara):
            hissi = Hissi(self.alinK, self.ylinK)
            self.hissit.append(hissi)

    def ajaHissia(self, hissiNumero, kohdeKerros):
        hissiNumero -= 1
        if hissiNumero >= 0 and hissiNumero < len(self.hissit):
            self.hissit[hissiNumero].siirryKerrokseen(kohdeKerros)
        else:
            print("Hissiä ei löytynyt.")

talo = Talo(1, 10, 3)
talo.ajaHissia(1, 10)
