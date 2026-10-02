import kauppa
import vaihdaSijaintia
import lentoasema_haku_2

player_hp = lentoasema_haku_2.hae_pelaaja_HP()

while player_hp > 0:
    player_action = input("1 - Vaihda sijaintia\n2 - Mene kauppaan\n3 - Lopeta peli\n")

    if player_action == "1":
        vaihdaSijaintia.nextLocation()
    if player_action == "2":
        kauppa.meneKauppaan()
    if player_action == "3":
        break