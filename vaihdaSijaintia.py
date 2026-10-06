import bossfight
import lentoasema_haku_2


def nextLocation(kayttaja):
    print("--------------------")
    asemat = lentoasema_haku_2.hae_lentoasemat("1", "FI")
    countries = dict(asemat)
    while True:
        sijainti = lentoasema_haku_2.hae_sijainti_nimellä(kayttaja)
        print(f"sinun nykyinen sijainti on {sijainti}")
        print("etsitään asemat...")
        asemat_lähellä = lentoasema_haku_2.hae_lähin_asema(sijainti)
        for i in range(3):
            print(f"{asemat_lähellä[ i + 1 ][0]: .2f}km kaukana | nimi: {asemat_lähellä[ i + 1 ][1]} | ICAO koodi: {asemat_lähellä[ i + 1 ][2]}")
        kohde = input("Minne matka?\nSyötä ICAO koodi: ")
        if kohde in countries.values():
            print(f"ollaan menossa kohteeseen {kohde}")
        else:
            print("kokeile uudelleen, kohde ei saatavilla / olemassa.")
        break