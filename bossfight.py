import random
def bossfight(location, hp):
    väärin = True
    player_hp = hp
    bosses = {"EFHK":True, "EFIV":False, "EFJO":True}
    bossHP = 5

    for key, value in bosses.items():
        if key == location and value == True:
            print("Pahis lähestyy sinua. Sinun pitää päihittää hänet! kivi sakset paperissa...")
            while player_hp > 0 and bossHP > 0:
                print(f"Pahiksella on {bossHP} elämää")
                print(f"Sinulla on {player_hp} elämää")
                while väärin:
                    try:
                        player_action = int(input("1 - kivi\n2 - paperi\n3 - sakset\n"))
                        väärin = False
                    except:
                        väärin = True
                boss_action = random.randint(1,3)
                if player_action == 1 and boss_action == 2:
                    bossHP = bossHP - 1
                    print(f"Pahis menetti yhden elämän")
                elif player_action == 2 and boss_action == 3:
                    bossHP = bossHP - 1
                    print(f"Pahis menetti yhden elämän")
                elif player_action == 3 and boss_action == 1:
                    bossHP = bossHP - 1
                    print(f"Pahis menetti yhden elämän")
                elif player_action == boss_action:
                    print("Yritä uudelleen! Molemmilla sama valinta")
                else:
                    player_hp = player_hp - 1
                    print(f"Sinä menetit yhden elämän")
                väärin = True
        elif key == location and value == False:
            print("Massivista! Sait 1000 kruunua")