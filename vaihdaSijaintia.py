import bossfight
import lentoasema_haku_2
import grafiikka
import ääni

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
            ääni.toista_ääni(300, 300)
        kohde = input("Minne matka?\nSyötä ICAO koodi: ")
        if kohde in countries.values():
            print(f"ollaan menossa kohteeseen {kohde}")
            lentoasema_haku_2.vaihda_pelaajan_sijaintia(kayttaja, kohde) #<---- sijainnin vaihto
            hp-=4
            lentoasema_haku_2.meneta_pelaaja_HP(kayttaja)
            if lentoasema_haku_2.onkoBoss(kohde):
                bossfight.bossfight(sijainti,"large_airport",hp, kayttaja)
                ääni.toista_ääni(300, 300)
                grafiikka.tulosta_pahis_tuhottu()
                print("pahis kuoli")
                kayttaja_id=lentoasema_haku_2.hae_pelaajan_ID(kayttaja)
                lentoasema_haku_2.tuhoalentokentta(kohde, kayttaja_id)
                print("Massivista! Sait 1000 kruunua")
                lentoasema_haku_2.saa_rahaa(kayttaja)
                break
        else:
            ääni.toista_ääni(300, 300)
            print("kokeile uudelleen, kohde ei saatavilla / olemassa.")
        break
