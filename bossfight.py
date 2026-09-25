import random
from main import player_hp

def bossfight(location):
    global player_hp
    bosses = {"EFHK":True, "EFIV":False, "EFJO":True}
    bossHP = 5

    for key, value in bosses.items():
        if key == location and value == True:
            print("The boss approaches you must defeat him! In rock paper scissors...")
            while player_hp > 0:
                print(f"The boss currently has {bossHP}")
                player_action = int(input("1 - rock\n2 - paper\n3 - scissors"))
                boss_action = random.randint(1,3)
                if player_action == 1 and boss_action == 2:
                    bossHP -= 1
                    print(f"The boss loses one life\nhe currently has {bossHP}")
                elif player_action == 2 and boss_action == 3:
                    bossHP -= 1
                    print(f"The boss loses one life\nhe currently has {bossHP}")
                elif player_action == 3 and boss_action == 1:
                    bossHP -= 1
                    print(f"The boss loses one life\nhe currently has {bossHP}")
                elif player_action == boss_action:
                    print("Try again")
                else:
                    player_hp = player_hp - 1
                    print(f"You lose one life\nyou currently have {player_hp}")
        elif key == location and value == False:
            print("you get money!!!\n 10 kr")