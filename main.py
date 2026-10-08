import kauppa
import vaihdaSijaintia
import lentoasema_haku_2
import peli
import grafiikka

väärin = True
while väärin:
    try:
        valinta = input("1 - Kirjaudu\n2 - Luo käyttäjä\n")
        if valinta == "1":
            kayttaja = peli.etsi_kayttaja()
            väärin = False
        elif valinta == "2":
            kayttaja = peli.luo_kayttaja()
    except:
        väärin = True

tuhotut_vaatimus=2
#Valloitettujen lentokenttien vaatimus
player_hp = lentoasema_haku_2.hae_pelaaja_HP(kayttaja)
if player_hp<=0:
    grafiikka.tulosta_pilotti_kuoli()
    print(f"{kayttaja} on kuollut, Et voi enää pelata tällä käyttäjällä :(")
while player_hp > 0:
    player_hp = lentoasema_haku_2.hae_pelaaja_HP(kayttaja)
    print(f"Käyttäjanimi: {kayttaja}")
    grafiikka.tulosta_pilotti()
    print(f"Pelaajan elinvoima/polttoaine: {player_hp}\n HP")
    tuhotut=lentoasema_haku_2.hae_tuhotut(kayttaja)
    print(f"Valloitetut lentoknentät: {tuhotut}")
    if tuhotut==tuhotut_vaatimus:
        print("voitit :D      v(^O^)/")
        grafiikka.tulosta_pilotti_voitti()
        exit()
    player_action = input("1 - Vaihda sijaintia\n2 - Mene kauppaan\n3 - Lopeta peli\n")

    if player_action == "1":
        vaihdaSijaintia.nextLocation(kayttaja,player_hp)
    if player_action == "2":
        kauppa.meneKauppaan(kayttaja)
    if player_action == "3":
        break