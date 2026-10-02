import lentoasema_haku_2
import random
import RahaLoppu

def meneKauppaan():
    pelaajan_raha = lentoasema_haku_2.raha_tallahetkella()

    print(f"--------------------\nTervetuloa kauppaani! Sinulla on {pelaajan_raha} euroa")
    while True:
        print("1 - Osta\n2 - Poistu")
        player_kauppa_action = input("")
        if player_kauppa_action == "2":
            break
        elif player_kauppa_action == "1":
            rng_maksu4fun = random.randint(500, 1000)
            player_ostos = input(f"Haluatko ostaa hp:ta hinta on {rng_maksu4fun} euroa \nKyllä tai ei\n")
            if player_ostos.lower() == "kyllä":
                if pelaajan_raha - rng_maksu4fun < 0:
                    varma = input("Oletko varma? Tästä voi olla seurauksia\n Kyllä tai ei\n")
                    if varma.lower() == "kyllä":
                        RahaLoppu.täysin_loppu()
                        lentoasema_haku_2.kuole()
                else:
                    lentoasema_haku_2.kayta_rahaa(rng_maksu4fun)
                    lentoasema_haku_2.saa_HP()
                    print("Kaikki hyvin!")
            else:
                continue
        else:
            print("Virhe syötteessä\n")
    print("--------------------")
#keskeneräinen alku