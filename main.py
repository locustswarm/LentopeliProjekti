#import bossfight
import kauppa
#import vaidaSijaintia

player_hp = 5 #vaihda numero tietokannasta otettavaan lukuun

while player_hp > 0:
    player_action = input("1 - Vaihda sijaintia\n2 - Mene kauppaan \n")

    if player_action == "1":
        #vaidaSijaintia()
        continue
    if player_action == "2":
        kauppa.meneKauppaan()