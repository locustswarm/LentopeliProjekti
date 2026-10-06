import bossfight
import lentoasema_haku_2


def nextLocation(kayttaja,hp):
    print("--------------------")
    tulostus = 0
    asemat = lentoasema_haku_2.hae_lentoasemat("1")
    countries = dict(asemat)
    while True:
        sijainti = lentoasema_haku_2.hae_sijainti_nimellä(kayttaja)
        print(f"sinun nykyinen sijainti on {sijainti}")
        print("etsitään asemat...")
        asemat_lähellä = lentoasema_haku_2.hae_lähin_asema(sijainti)
        while True:
            if asemat_lähellä[tulostus][0] > hp:
                break
            tulostus += 1
            print(f"{asemat_lähellä[ tulostus + 1 ][0]: .2f}km kaukana | nimi: {asemat_lähellä[ tulostus + 1 ][1]} | ICAO koodi: {asemat_lähellä[ tulostus + 1 ][2]}")
        kohde = input("Minne matka?\nSyötä ICAO koodi: ")
        if kohde in countries.values():
            print(f"ollaan menossa kohteeseen {kohde}")

            if lentoasema_haku_2.onkoBoss(kohde):
                bossfight.bossfight(sijainti,"large_airport",hp, kayttaja)
                print("pahis kuoli")
                break
        else:
            print("kokeile uudelleen, kohde ei saatavilla / olemassa.")
        break