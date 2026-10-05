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