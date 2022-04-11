class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.previous_tulos = None

    def miinus(self, arvo):
        self.previous_tulos = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.previous_tulos = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.previous_tulos = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.previous_tulos = self.tulos
        self.tulos = arvo
