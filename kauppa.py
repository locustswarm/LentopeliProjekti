import lentoasema_haku_2
import random
import RahaLoppu
import grafiikka

def meneKauppaan(kayttaja):

    pelaajan_raha = lentoasema_haku_2.raha_tallahetkella(kayttaja)
    pelaajan_hp = lentoasema_haku_2.hae_pelaaja_HP(kayttaja)

    print("")
    grafiikka.tulosta_kauppias()

    print(f"^\n[Tervetuloa kauppaani!]")
    while True:
        pelaajan_raha = lentoasema_haku_2.raha_tallahetkella(kayttaja)
        pelaajan_hp = lentoasema_haku_2.hae_pelaaja_HP(kayttaja)
        grafiikka.tulosta_pilotti()
        print(f"HP: {pelaajan_hp}\nRahat: {pelaajan_raha} kr")
        print("1 - Osta\n2 - Poistu")
        player_kauppa_action = input("")
        if player_kauppa_action == "2":
            break
        elif player_kauppa_action == "1":
            rng_maksu4fun = random.randint(500, 1000)
            rng_hp4fun = random.randint(500, 1000)
            player_ostos = input(f"Haluatko ostaa {rng_hp4fun} hp:ta hinta on {rng_maksu4fun} euroa \nKyllä tai ei\n")
            if player_ostos.lower() == "kyllä":
                if pelaajan_raha - rng_maksu4fun < 0:
                    RahaLoppu.täysin_loppu()
                    grafiikka.tulosta_pilotti_kuoli()
                    lentoasema_haku_2.kuole(kayttaja)

                    break
                else:
                    lentoasema_haku_2.kayta_rahaa(rng_maksu4fun, kayttaja)
                    lentoasema_haku_2.saa_HP(rng_hp4fun, kayttaja)
                    print("Kaikki hyvin!")
            else:
                continue
        else:
            print("Virhe syötteessä\n")
    print("--------------------")
#keskeneräinen alku