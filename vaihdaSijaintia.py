import bossfight

def nextLocation(hp):
    print("--------------------")
    countries = {"Helsinki":"EFHK", "Ivalo":"EFIV", "Joensuu":"EFJO"} #tee sql query "countries"
    while True:
        player_location = input("Minne matka?\nSyötä ICAO koodi: ")
        for value in countries.values():
            if player_location == value:
                bossfight.bossfight(value,hp)
            if hp == 0:
                break