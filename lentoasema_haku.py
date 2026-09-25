import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='juuri',
         autocommit=True
         )


DBkursori = yhteys.cursor()
while True:
    lentokentta_haku=int(input("(1) hae lentokentät maatunuksella \n (2) hae icao koodilla \n (3)poistu hausta \n valintasi: "))

    if lentokentta_haku==1:
        maatunnus = input("anna maatunnus: ")
        sql_kysely = f"select name, ident, iso_country, type from airport where iso_country='{maatunnus}' order by type"


    elif lentokentta_haku==2:
        icao_koodi =input("anna icao-koodi: ")
        sql_kysely=f"select name, ident, iso_country, type from airport where ident='{icao_koodi}'"

    elif lentokentta_haku==3:
        break
    else:
        print("Virheellinen valinta")
        continue

    DBkursori.execute(sql_kysely)

    #Tuloksen haku
    tulos=DBkursori.fetchall()

    for rivi in tulos:
        print(f"Lentokentän nimi: {rivi[0]}")
        print(f"Lentokentän icao-koodi: {rivi[1]}")
        print(f"Lentokentän maatunnus: {rivi[2]}")
        print(f"Lentokentän tyyppi: {rivi[3]}")
        print("")
    print("")
