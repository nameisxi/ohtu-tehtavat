from kps import KPS
from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    # def pelaa(self):
    #     tuomari = Tuomari()
    #     tekoaly = TekoalyParannettu(10)

    #     ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
    #     tokan_siirto = tekoaly.anna_siirto()

    #     print(f"Tietokone valitsi: {tokan_siirto}")

    #     while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
    #         tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    #         print(tuomari)

    #         ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
    #         tokan_siirto = tekoaly.anna_siirto()

    #         print(f"Tietokone valitsi: {tokan_siirto}")
    #         tekoaly.aseta_siirto(ekan_siirto)

    #     print("Kiitos!")
    #     print(tuomari)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
