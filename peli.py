#Ohjelma kättäjän etsimiseen ja luontiin

import sqlYhteys

DBkursori = sqlYhteys.yhteys.cursor()

def etsi_kayttaja():
    nyky_kayttaja = []
    while True:
        kayttajanimi=input("Anna etsimäsi käyttäjän nimi: ")
        sql_kysely=f"select gamertag, id from game where gamertag='{kayttajanimi}';"
        DBkursori.execute(sql_kysely)
        tulos = DBkursori.fetchall()

        if len(tulos)==0:
            print("Käyttäjää ei löytynyt")

        else:
            print(f"Löydettiin käyttäjä: {kayttajanimi}")

            valinta=input("Haluatko pelata tällä käyttäjällä?\nKyllä (1)\nEn (2)\nValintasi:")
            if valinta == "1":
                nyky_kayttaja.append(tulos[0][0])
                nyky_kayttaja.append(tulos[0][1])
                print(f"Käyttänimesi on {nyky_kayttaja[0]} ja sen ID on {nyky_kayttaja[1]}")
                return tulos[0][0]
            else:
                print("Kirjaudu uudelleen")

def luo_kayttaja():
    nyky_kayttaja = []
    while True:
        kayttajanimi = input("Anna käyttäjällesi nimi: ")
        if kayttajanimi=="" or kayttajanimi==" ":
            print("Käyttäjänimi ei voi olla tyhjä")

        elif kayttajanimi!="" or kayttajanimi!=" ":
            sql_kysely=f"select gamertag from game;"
            DBkursori.execute(sql_kysely)
            tulos = DBkursori.fetchall()

            kayttaja_olemassa=0
            for rivi in tulos:

                if kayttajanimi.lower() == rivi[0].lower():
                    kayttaja_olemassa = 1
                    print(f"Käyttäjänimi {kayttajanimi} on jo olemassa. Kokeile toista nimeä")

            if kayttaja_olemassa == 0:
                sql_kysely=f"insert into game(co2_consumed, co2_budget, gamertag, location, moneys) values(0, 10000, '{kayttajanimi}', 'EFHF', 404);"
                DBkursori.execute(sql_kysely)

                sql_kysely = f"select gamertag, id from game where gamertag='{kayttajanimi}';"
                DBkursori.execute(sql_kysely)
                tulos = DBkursori.fetchall()
                nyky_kayttaja.append(tulos[0][0])
                nyky_kayttaja.append(tulos[0][1])
                print(f"Kaikki ok! Voit kirjautua sisään\nKäyttänimesi on {nyky_kayttaja[0]} ja sen ID on {nyky_kayttaja[1]}")
                return tulos[0][0]
