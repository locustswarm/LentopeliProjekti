import lentoasema_haku_2
import random

def meneKauppaan():
    print("--------------------")
    while True:
        print("1 - Osta\n2 - Poistu")
        player_kauppa_action = input("")
        if player_kauppa_action == "2":
            break
        elif player_kauppa_action == "1":
            rng_maksu4fun = random.random(500, 1000)
            player_ostos = input(f"Haluatko ostaa hp:ta hinta on {rng_maksu4fun} euroa \nKyllä tai ei\n")
            if player_ostos.lower() == "kyllä":
                pelaajan_raha = lentoasema_haku_2.raha_tallahetkella()
                if pelaajan_raha - rng_maksu4fun < 0:
                    varma = input("Oletko varma? Tästä voi olla seurauksia\n Kyllä tai ei")
                    if varma.lower() == "kyllä":
                        continue
            else:
                lentoasema_haku_2.kayta_rahaa(rng_maksu4fun)

            else:
                continue
        else:
            print("Virhe syötteessä\n")
    print("--------------------")
#keskeneräinen alku