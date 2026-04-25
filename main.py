from fastapi import FastAPI
from enum import Enum

#API Kullanımı için bir ana App oluşturarak FastAPI kütüphanesindeki nesneyi örneklememiz gerekiyor.
app = FastAPI()

#ENUM'lar kullanılarak enum içindeki değer dışında entity girilirse tarama yapmadan hata döndürüyor ki bu da sistem performansını olumlu etkiler.
class IkametValue(Enum):
    ISTANBUL = "İstanbul"
    IZMIR = "İzmir"

BANDS = [
    {'id':1 , 'name': 'Ömer Faruk Özvardar','İkamet' : "Aydın"},
    {'id':2 , 'name': 'Nimet Nur Özvardar','İkamet' : "İstanbul"},
    {'id':3 , 'name': 'Zeynep Zeybek','İkamet' : "İstanbul"},
    {'id':4 , 'name': 'Şahap Uğur Özvardar','İkamet' : "İzmir"},
    {'id':5 , 'name': 'Özlem Özvardar','İkamet' : "İzmir"}
]

@app.get("/bands")
def bands() -> list[dict]:
    return BANDS

@app.get("/") 
def root_check() -> dict[str,str]:
    return {'Hello':'RootCheck'}


@app.get("/about")
def about() -> str:
    return 'Bu bir portföy sitesidir.'

#Bir girdi ile endpoint bu şekilde oluşturulur.
@app.get("/bands/{band_id}")
def getbandbyid(band_id:int):
    finded_row = []
    for a in BANDS:
        if a['id'] == band_id:
            finded_row = a
            return finded_row
    
    return {"Exception": "Non found band!"}
            

#Entity gerektiren endpointte enum kullanımı.
@app.get("/bands/bands_byCity/{band_city}")
def bands_byCity(band_city:IkametValue) -> list[dict]:
    return [
        b for b in BANDS if b['İkamet'].lower() == band_city.value.lower()
    ]

