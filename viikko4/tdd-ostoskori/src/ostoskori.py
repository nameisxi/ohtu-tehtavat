from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        count = 0

        for ostos in self._ostokset:
            count += ostos.lukumaara()
        
        return count

    def hinta(self):
        return 0

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
