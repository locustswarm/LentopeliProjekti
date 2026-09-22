player_kauppa_action = input("")

while True:
    print("Osta\nPoistu")
    if player_kauppa_action.lower() == "poistu":
        break
    elif player_kauppa_action.lower() == "osta":
        player_ostos = input("Haluatko ostaa hp:ta hinta on 5 euroa \nKyllä tai ei")
        if player_ostos.lower() == "kyllä":
            #lisää hp pelaajan statseihin tietokantaan
            continue
        else:
            continue
    else:
        print("Virhe syötteessä")


#keskeneräinen alku