import bossfight
import lentoasema_haku_2


def nextLocation():
    print("--------------------")
    asemat = lentoasema_haku_2.hae_lentoasemat("1", "FI")
    countries = dict(asemat)
    while True:
        player_location = input("Minne matka?\nSyötä ICAO koodi: ")
        for value in countries.values():
            if player_location == value:
                bossi = lentoasema_haku_2.onkoBoss(value)
                bossfight.bossfight(value, bossi)
        break