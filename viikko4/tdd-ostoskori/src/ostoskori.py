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
        price = 0

        for ostos in self._ostokset:
            price += ostos.hinta()

        return price

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))


    def poista_tuote(self, poistettava: Tuote):
        deletable_ostos = None
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                if ostos.lukumaara() == 1: 
                    deletable_ostos = ostos
                ostos.muuta_lukumaaraa(-1)
        if deletable_ostos is not None:
            self._ostokset.remove(deletable_ostos)

    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
