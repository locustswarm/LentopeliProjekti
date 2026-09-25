import kauppa
import vaihdaSijaintia

player_hp = 5 #vaihda numero tietokannasta otettavaan lukuun

while player_hp > 0:
    player_action = input("1 - Vaihda sijaintia\n2 - Mene kauppaan\n3 - Lopeta peli\n")

    if player_action == "1":
        vaihdaSijaintia.nextLocation()
    if player_action == "2":
        kauppa.meneKauppaan()
    if player_action == "3":
        break