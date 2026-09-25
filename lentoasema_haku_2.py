def hae_lentoasemat(valinta, maatunnus):
    import mysql.connector
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='lentopeli',
        user='root',
        password='juuri',
        autocommit=True
    )

    DBkursori = yhteys.cursor()
    if valinta=="1":
        sql_kysely = f"select name, ident from airport where iso_country='{maatunnus}' order by type"


    elif valinta=="2":
        icao_koodi =input("anna icao-koodi: ")
        sql_kysely=f"select name, ident, iso_country, type from airport where ident='{icao_koodi}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos

