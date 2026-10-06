import ääni
def tulosta_viikatemies():
    print("          ⢀⣴⡆")
    print("     ⢀⣶⣆⢀⠔⠁ ⣷")
    print("     ⠚⣿⣿⣷⡄  ⢸")
    print("     ⣠⣺⣿⣿⡇  ⠸")
    print("    ⡸⣿⣿⣿⣿⡇")
    print("   ⡔⠁⢸⣿⣿⣿⣿")
    print("  ⠌   ⣿⣿⣿⣿")
    print(" ⡌    ⢸⣿⣿⣿⡇")
    print("⠈     ⢸⣿⣿⣿⡇")
    print("      ⣾⣿⣿⣿⣷")
    print("      ⣿⣿⣿⣿⣿⣷⣄")
    print("      ⠛⠛⠛⠛⠛⠛⠉")
def rahat_lopussa():
    tulosta_viikatemies()
    print("hän sanoo: onko kukkaro kevyt?")
    for i in range(3):
        ääni.toista_ääni(300,500)
    print("rahat vähissä!")
def täysin_loppu():
    tulosta_viikatemies()
    print("liian myöhastä!")
    for i in range(5):
        ääni.toista_ääni(400,100)
    print("viikate mies tuli koska raha negatiivinen: peli päättyi")