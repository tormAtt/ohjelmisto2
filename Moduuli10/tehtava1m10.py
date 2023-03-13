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

hissi = Hissi(1, 10)
hissi.siirryKerrokseen(10)
hissi.siirryKerrokseen(0)