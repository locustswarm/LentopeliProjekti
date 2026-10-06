#Ohjelma kättäjän etsimiseen ja luontiin

import sqlYhteys
DBkursori = sqlYhteys.yhteys.cursor()

nyky_kayttaja=[]
    #Lista johon tallenetaan käyttäjän pelinimi ja ID

def etsi_kayttaja():
    kayttajanimi=input("Anna etsimäsi käyttäjän nimi: ")
    sql_kysely=f"select gamertag, id from game where gamertag='{kayttajanimi}';"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()

    if len(tulos)==0:
        return "Käyttäjää ei löytynyt"

    else:
        print(f"Löydettiin käyttäjä: {kayttajanimi}")

        valinta=input("Haluatko pelata tällä käyttäjällä?  Kyllä (1)\n En (2)\nValintasi:")
        if valinta == "1":
            nyky_kayttaja.append(tulos[0][0])
                #lisätään käyttäjä nimi listaan
            nyky_kayttaja.append(tulos[0][1])
                #lisätään id listaan
            return f"Käyttäsi ja sen ID: {nyky_kayttaja}"
        else:
            return "Palataan päävalikkoon"

def luo_kayttaja():
    kayttajanimi = input("Anna käyttäjällesi nimi: ")
    if kayttajanimi=="" or kayttajanimi==" ":
        return("Käyttäjänimi ei voi olla tyhjä")
            #Tällä estetään tyhjät käyttäjänimet

    sql_kysely=f"select gamertag from game;"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()

    kayttaja_olemassa=0
    #Ohjelma varmaan toimii myös ilman tätä muuttujaa
    for rivi in tulos:

        if kayttajanimi.lower() == rivi[0].lower():
            kayttaja_olemassa = 1
            return f"Käyttäjänimi {kayttajanimi} on jo olemassa. Kokeile toista nimeä"

    if kayttaja_olemassa == 0:
        sql_kysely=f"insert into game(co2_consumed, co2_budget, gamertag, location, moneys) values(0, 10000, '{kayttajanimi}', 'EFHF', 404);"
        DBkursori.execute(sql_kysely)
        #Käyttäjän luoti
        sql_kysely = f"insert into boss (boss_hp, boss_fight, likes_apples, name) values(100, 0, 'Yeah', '{kayttajanimi}');";
        DBkursori.execute(sql_kysely)
        #Käyttäjälle pahiksen luonti (Pahiksen nimi on sama kuin käyttäjällä jotta yhteyden luonti olisi helpompaa)
        yhteys_pahikseen = []
        # Lista johon lisätään pahiksen ja pelaajan id (Yhteyden luontia varten)
        sql_kysely=f"select id from game where gamertag='{kayttajanimi}';"
            #haetaa käyttäjä id
        DBkursori.execute(sql_kysely)
        tulos = DBkursori.fetchall()

        yhteys_pahikseen.append(tulos[0][0])
            #Lisätään käyttäjän id listaan
        sql_kysely = f"select id from boss where name='{kayttajanimi}';"
            #Haetaan pahis id
        DBkursori.execute(sql_kysely)

        tulos = DBkursori.fetchall()
        yhteys_pahikseen.append(tulos[0][0])
        # Lisätään pahis id listaan
        sql_kysely=f"insert into boss_reached values ({yhteys_pahikseen[0]}, {yhteys_pahikseen[1]});"
        DBkursori.execute(sql_kysely)

        sql_kysely = f"select gamertag, id from game where gamertag='{kayttajanimi}';"
        DBkursori.execute(sql_kysely)
        tulos = DBkursori.fetchall()

        nyky_kayttaja.append(tulos[0][0])
        # lisätään käyttäjä nimi listaan
        nyky_kayttaja.append(tulos[0][1])
        # lisätään id listaan
        return f"Käyttäjäsi ja sen ID: {nyky_kayttaja}"
