from kps import KPS


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        pelimuodot = {
            'a': KPS.luo_kaksinpeli(),
            'b': KPS.luo_helppo_yksinpeli(),
            'c': KPS.luo_vaikea_yksinpeli()
        }

        vastaus = input()

        if vastaus[:-1] in pelimuodot.keys():
            peli = pelimuodot[vastaus[:-1]]
            peli.pelaa()


if __name__ == "__main__":
    main()
