import kauppa
import vaihdaSijaintia
import lentoasema_haku_2
import peli

väärin = True
while väärin:
    try:
        valinta = input("1 - Kirjaudu\n 2 - Luo käyttäjä")
        if valinta == "1":
            kayttaja = peli.etsi_kayttaja()
            print(kayttaja)
            väärin = False
        elif valinta == "2":
            kayttaja = peli.luo_kayttaja()
            print(kayttaja)
            väärin = False
    except:
        väärin = True

player_hp = lentoasema_haku_2.hae_pelaaja_HP()

while player_hp > 0:
    player_action = input("1 - Vaihda sijaintia\n2 - Mene kauppaan\n3 - Lopeta peli\n")

    if player_action == "1":
        vaihdaSijaintia.nextLocation()
    if player_action == "2":
        kauppa.meneKauppaan()
    if player_action == "3":
        break