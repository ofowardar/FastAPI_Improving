from enum import Enum
from pydantic import BaseModel
from datetime import date

class IkametValue(Enum):
    ISTANBUL = "İstanbul"
    IZMIR = "İzmir"



#Pydantic kullanmamızın en büyük avantajı tür kontrolünü endpointte sağlamamızdır. Bir bilgide tür doğrulamasını sağlar.(id yerine abc yazsa basemodelden türetilen model olmasa kontrol sağlanmaz.)
# class Band(BaseModel):
#     #{'id':1 , 'name': 'Ömer Faruk Özvardar','İkamet' : "Aydın"},
#     id:int
#     name:str
#     İkamet:str

class Album(BaseModel):
    title:str
    release_date: date

class Band(BaseModel):
    #{'id':1 , 'name': 'Ömer Faruk Özvardar','İkamet' : "Aydın"},
    id:int
    name:str
    İkamet:str                                                              # Burada iç içe modelleri gösteriyorum.
    albums: list[Album] = [] #Default değerini de boş liste yaptım.