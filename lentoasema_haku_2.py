import sqlYhteys
from geopy import distance
def hae_kordinaatti_sijainnilla(mesta):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely = f"select latitude_deg , longitude_deg from airport where ident='{mesta}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos
def hae_lähin_asema(meidän_paikka):
    lähin = []
    etäisyys = 0
    kordinaatti_meidän = hae_kordinaatti_sijainnilla(meidän_paikka)
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select latitude_deg, longitude_deg, name, ident from airport"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    for tulo in tulos:
        etäisyys = distance.distance(kordinaatti_meidän,(tulo[0],tulo[1])).km
        seuraava = [etäisyys,tulo[2],tulo[3]]
        lähin.append(seuraava)
    return sorted(lähin, key=lambda x: x[0])
def hae_sijainti_nimellä(nimi):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely = f"select location from game where gamertag='{nimi}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos[0][0]
def hae_lentoasemat(valinta):
    yhteys = sqlYhteys.yhteys

    DBkursori = yhteys.cursor()
    if valinta=="1":
        sql_kysely = f"select name, ident from airport order by type"


    elif valinta=="2":
        icao_koodi =input("anna icao-koodi: ")
        sql_kysely=f"select name, ident, iso_country, type from airport where ident='{icao_koodi}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos

def hae_pelaaja_HP(kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select co2_budget, co2_consumed from game WHERE gamertag='{kayttaja}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    hp = tulos[0][0] - tulos[0][1]
    return hp

def meneta_pelaaja_HP(kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET co2_consumed = co2_consumed + 4 WHERE gamertag = '{kayttaja}'"
    DBkursori.execute(sql_kysely)

def kuole(kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET co2_consumed = co2_consumed + co2_budget WHERE gamertag = '{kayttaja}'"
    DBkursori.execute(sql_kysely)

def saa_HP(hp, kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET co2_budget = co2_budget + {hp} WHERE gamertag = '{kayttaja}'"
    DBkursori.execute(sql_kysely)

def saa_rahaa(kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET moneys = moneys + 1000 WHERE gamertag = '{kayttaja}'"
    DBkursori.execute(sql_kysely)

def kayta_rahaa(raha, kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"UPDATE game SET moneys = moneys - {raha} WHERE gamertag = '{kayttaja}'"
    DBkursori.execute(sql_kysely)

def raha_tallahetkella(kayttaja):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely = f"select moneys from game WHERE gamertag= '{kayttaja}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos[0][0]
def onkolentokenttaTuhottu(icao, user_id):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select airport_ident from airport_cleared where airport_ident = '{icao}'and game_id='{user_id}'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos[0][0]

def tuhoalentokentta(icao, user_id):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"INSERT INTO airport_cleared VALUES ({user_id},'{icao}');"
    DBkursori.execute(sql_kysely)

def onkoBoss(sijainti):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select * from airport where ident = '{sijainti}' and type='large_airport'"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return len(tulos)
def vaihda_pelaajan_sijaintia(nimi,uusi_mesta):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"update game set location = '{uusi_mesta}' where gamertag = '{nimi}'"
    DBkursori.execute(sql_kysely)

def hae_pelaajan_ID(nimi):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"select id from game where gamertag = '{nimi}';"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos[0][0]

def hae_tuhotut(nimi):
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely = f"select count(airport_ident) from airport_cleared where game_id in(select id from game where gamertag='{nimi}');"
    DBkursori.execute(sql_kysely)
    tulos = DBkursori.fetchall()
    return tulos[0][0]
