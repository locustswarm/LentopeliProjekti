import random
import lentoasema_haku_2
import grafiikka
import ääni
def bossfight(location, type,hp, kayttaja):
    väärin = True
    player_hp = hp
    nimet=["beromgleb","Jyrki_mutta_pahis", "Gibby", "Zormox", "Jeremy"]
    bossName=nimet[random.randint(0,len(nimet)-1)]
    bossHP = 5
    kps = ["kiven","paperin","sakset"]
    kayttaja_id=lentoasema_haku_2.kayttaja_id = lentoasema_haku_2.hae_pelaajan_ID(kayttaja)

    if type == "large_airport":
        ääni.toista_ääni(300,300)
        print("Pahis lähestyy sinua. Sinun pitää päihittää hänet! kivi sakset paperissa...\n ")
        while bossHP > 0:
            if player_hp <= 0:
                lentoasema_haku_2.kuole(kayttaja)
                print("ded")
                exit()
            boss_hold5=random.randint(1,11)
            print(f"Pahiksen nimi: {bossName}")
            if boss_hold5==7:
                grafiikka.tulosta_pahis_hold5()
            else:
                grafiikka.tulosta_pahis()
            print(f"Pahiksen elinvoima {bossHP} HP")
            print(f"Käyttäjänimi: {kayttaja}")
            grafiikka.tulosta_pilotti()
            print(f"Pelaajan elinvoima: {player_hp} HP")
            while väärin:
                try:
                    player_action = int(input("0 - kivi\n1 - paperi\n2 - sakset\n"))
                    if player_action > 2 or  player_action < 0:
                        raise Exception()
                    väärin = False
                except:
                    väärin = True
            boss_action = random.randint(0,2)
            ääni.toista_ääni(300, 300)
            print(f"Pahis: Valitsin {kps[boss_action]}")
            lopputulos = (boss_action - player_action + 3) % 3
            if lopputulos == 0:
                ääni.toista_ääni(300, 300)
                print("Yritä uudelleen! Molemmilla sama valinta")
            elif lopputulos == 1:
                lentoasema_haku_2.meneta_pelaaja_HP(kayttaja)
                player_hp = player_hp - 4
                print(f"Sinä menetit Neljä elämää")
            elif lopputulos == 2:
                bossHP = bossHP - 1
                print(f"Pahis menetti yhden elämän")
            väärin = True
    elif type != "large_airport" and type != None:
        ääni.toista_ääni(300, 300)
        print("Massivista! Sait 1000 kruunua")
        lentoasema_haku_2.saa_rahaa()
    else:
        print("Pahis jonka voisi haasta kivi, sakset, paperi otteluun on kukistettu")
