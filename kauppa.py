def meneKauppaan():
    print("--------------------")
    while True:
        print("1 - Osta\n2 - Poistu")
        player_kauppa_action = input("")
        if player_kauppa_action == "2":
            break
        elif player_kauppa_action == "1":
            player_ostos = input("Haluatko ostaa hp:ta hinta on 5 euroa \nKyllä tai ei\n")
            if player_ostos.lower() == "kyllä":
                #lisää hp pelaajan statseihin tietokantaan
                continue
            else:
                continue
        else:
            print("Virhe syötteessä\n")
    print("--------------------")
#keskeneräinen alku