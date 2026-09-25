import bossfight

def nextLocation():
    print("--------------------")
    countries = {"Helsinki":"EFHK", "Ivalo":"EFIV", "Joensuu":"EFJO"} #tee sql query "countries"
    while True:
        player_location = input("Minne matka?\nSyötä ICAO koodi: ")
        for value in countries.values():
            if player_location == value:
                bossfight.bossfight(value)
        print("Sijainti ei ole saatavilla")