

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lukumaara):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lukumaara == 0:
            self.ljono[0] = n
            self.alkioiden_lukumaara += 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lukumaara] = n
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

            if self.alkioiden_lukumaara % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n):
        kohta = -1

        for i in range(0, self.alkioiden_lukumaara):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lukumaara - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        elif self.alkioiden_lukumaara == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lukumaara - 1])
            tuotos = tuotos + "}"
            return tuotos
