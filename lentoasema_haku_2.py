import sqlYhteys
from geopy import distance
def hae_lähin_asema(meidän_paikka):
    lähin = []
    etäisyys = 0
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select latitude_deg, longitude_deg, name from airport"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    for tulo in tulos:
        etäisyys = distance.distance(meidän_paikka,(tulo[0],tulo[1])).km
        seuraava = [etäisyys,tulo[2]]
        lähin.append(seuraava)
    return sorted(lähin, key=lambda x: x[0])

def hae_lentoasemat(valinta, maatunnus):
    yhteys = sqlYhteys.yhteys

    DBkursori = yhteys.cursor()
    if valinta=="1":
        sql_kysely = f"select name, ident from airport where iso_country='{maatunnus}' order by type"


    elif valinta=="2":
        icao_koodi =input("anna icao-koodi: ")
        sql_kysely=f"select name, ident, iso_country, type from airport where ident='{icao_koodi}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos

def hae_pelaaja_HP():
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select co2_budget, co2_consumed from game"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    hp = tulos[0][0] - tulos[0][1]
    return hp

def meneta_pelaaja_HP():
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET co2_consumed = co2_consumed + 1 WHERE gamertag = 'jyrki'"
    DBkursori.execute(sql_kysely)

def kuole():
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET co2_consumed = co2_consumed + co2_budget WHERE gamertag = 'jyrki'"
    DBkursori.execute(sql_kysely)

def saa_HP():
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET co2_budget = co2_budget + 5 WHERE gamertag = 'jyrki'"
    DBkursori.execute(sql_kysely)

def saa_rahaa():
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET moneys = moneys + 1000 WHERE gamertag = 'jyrki'"
    DBkursori.execute(sql_kysely)

def kayta_rahaa(raha):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET moneys = moneys - {raha} WHERE gamertag = 'jyrki'"
    DBkursori.execute(sql_kysely)

def raha_tallahetkella():
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely = f"select moneys from game"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos[0][0]