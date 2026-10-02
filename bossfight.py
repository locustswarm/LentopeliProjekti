import random
import lentoasema_haku_2

def bossfight(location):
    väärin = True
    player_hp = lentoasema_haku_2.hae_pelaaja_HP()
    bosses = {"EFHK":True, "EFIV":False, "EFJO":True}
    bossHP = 5
    kps = ["kiven","paperin","sakset"]

    for key, value in bosses.items():
        if key == location and value == True:
            print("Pahis lähestyy sinua. Sinun pitää päihittää hänet! kivi sakset paperissa...")
            while player_hp > 0 and bossHP > 0:
                print(f"Pahiksella on {bossHP} elämää")
                print(f"Sinulla on {player_hp} elämää")
                while väärin:
                    try:
                        player_action = int(input("0 - kivi\n1 - paperi\n2 - sakset\n"))
                        if player_action > 2 or  player_action < 0:
                            raise Exception()
                        väärin = False
                    except:
                        väärin = True
                boss_action = random.randint(0,2)
                print(f"Pahis: Valitsin {kps[boss_action]}")
                lopputulos = (boss_action - player_action + 3) % 3
                if lopputulos == 0:
                    print("Yritä uudelleen! Molemmilla sama valinta")
                elif lopputulos == 1:
                    lentoasema_haku_2.meneta_pelaaja_HP()
                    player_hp = player_hp - 1
                    print(f"Sinä menetit yhden elämän")
                elif lopputulos == 2:
                    bossHP = bossHP - 1
                    print(f"Pahis menetti yhden elämän")
                väärin = True
        elif key == location and value == False:
            print("Massivista! Sait 1000 kruunua")