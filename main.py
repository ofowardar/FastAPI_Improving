from fastapi import FastAPI, HTTPException
from schemas import IkametValue, Band

#API Kullanımı için bir ana App oluşturarak FastAPI kütüphanesindeki nesneyi örneklememiz gerekiyor.
app = FastAPI()

#ENUM'lar kullanılarak enum içindeki değer dışında entity girilirse tarama yapmadan hata döndürüyor ki bu da sistem performansını olumlu etkiler.

BANDS = [
    {'id':1 , 'name': 'Ömer Faruk Özvardar','İkamet' : "Aydın",'albums': [
        {'title':"Kıvırcık Ali",'release_date':'2026-07-21'}
    ]},
    {'id':2 , 'name': 'Nimet Nur Özvardar','İkamet' : "İstanbul"},
    {'id':3 , 'name': 'Zeynep Zeybek','İkamet' : "İstanbul",'albums': [{'title':'Lana Del Rey','release_date':'2026-12-10'}]},
    {'id':4 , 'name': 'Şahap Uğur Özvardar','İkamet' : "İzmir"},
    {'id':5 , 'name': 'Özlem Özvardar','İkamet' : "İzmir"}
]

# @app.get("/bands")
# def bands() -> list[dict]:
#     return BANDS

# @app.get("/bands")
# def bands() -> list[Band]: #Burada bir dict yerine sabit modelimiz olan "Band" pydantic modelini kullandık.
#     return [
#         Band(**b) for b in BANDS 
#     ]

# QUERY Parameters ekleyerek bu endpointi bu hale getireceğiz.:

@app.get('/bands')
def bands(
    ikamet: IkametValue | None = None,
    has_albums: bool = False

          ) -> list[Band]:
    
    band_list = [Band(**b) for b in BANDS]


    if ikamet: # Eğer None Değilse
        band_list= [b for b in band_list if b.İkamet.lower() == ikamet.value.lower()]
        
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) > 0]
    return band_list
# !! Burada get_by_ikamet gibi bir durum yapmak yerine 127.0.0.1:8000/bands?ikamet=İstanbul diyerek hem tüm bandları alabiliyoruz hem de filtrelemeyi sorgu cümleleriyle yapabiliyoruz.
# Buraya birden çok parametre ekleyebiliriz ve parametreleri url de ampersant (&) işareti ile ayırıyoruz. 127.0.0.1:8000/bands?ikamet=İstanbul&has_album=True
#http://127.0.0.1:8000/bands?has_albums=True&ikamet=Aydın Şeklinde::


@app.get("/") 
def root_check() -> dict[str,str]:
    return {'Hello':'RootCheck'}


@app.get("/about")
def about() -> str:
    return 'Bu bir portföy sitesidir.'

#Bir girdi ile endpoint bu şekilde oluşturulur.
# @app.get("/bands/{band_id}")
# def getbandbyid(band_id:int):
#     finded_row = []
#     for a in BANDS:
#         if a['id'] == band_id:
#             finded_row = a
#             return finded_row
    
#     return {"Exception": "Non found band!"}

#Pydantic ile düzenlenmiş hali
@app.get("/bands/{band_id}", response_model=Band)
def getbandbyid(band_id:int) -> Band:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return Band(**band)

#Entity gerektiren endpointte enum kullanımı.
@app.get("/bands/bands_byCity/{band_city}")
def bands_byCity(band_city:IkametValue) -> list[Band]:
    return [
        Band(**b) for b in BANDS if b['İkamet'].lower() == band_city.value.lower()
    ]

