def hae_lentoasemat(valinta, maatunnus):
    import mysql.connector
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='lentopeli',
        user='root',
        password='Rotting_dir?1984',
        autocommit=True
    )

    DBkursori = yhteys.cursor()
    if valinta=="1":
        sql_kysely = f"select name, ident, iso_country, type from airport where iso_country='{maatunnus}' order by type"


    elif valinta=="2":
        icao_koodi =input("anna icao-koodi: ")
        sql_kysely=f"select name, ident, iso_country, type from airport where ident='{icao_koodi}'"


    else:
        return "Virheellinen valinta"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos

#valinta = input("(1) hae lentokentät maatunuksella \n (2) hae icao koodilla \n valintasi: ")

#print(hae_lentoasemat(valinta))





