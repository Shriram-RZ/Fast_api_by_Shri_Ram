#FastAPI Setup
from fastapi import FastAPI

app = FastAPI()

users_db = {
    1: {"id": 1, "name": "Luffy"},
    2: {"id": 2, "name": "Zoro"},
    3: {"id": 3, "name": "Nami"},
    4: {"id": 4, "name": "Sanji"},
    5: {"id": 5, "name": "Usopp"},
    6: {"id": 6, "name": "Robin"},
    7: {"id": 7, "name": "Franky"},
    8: {"id": 8, "name": "Brook"},
    9: {"id": 9, "name": "Chopper"},
    10: {"id": 10, "name": "Jinbe"},
    11: {"id": 11, "name": "Ace"},
    12: {"id": 12, "name": "Shanks"},
    13: {"id": 13, "name": "Buggy"},
    14: {"id": 14, "name": "Doflamingo"},
    15: {"id": 15, "name": "Mihawk"},
    16: {"id": 16, "name": "Law"},
    17: {"id": 17, "name": "Kid"},
    18: {"id": 18, "name": "Killer"},
    19: {"id": 19, "name": "Kaido"},
    20: {"id": 20, "name": "Big Mom"},
    21: {"id": 21, "name": "Rayleigh"},
    22: {"id": 22, "name": "Whitebeard"},
    23: {"id": 23, "name": "Blackbeard"},
    24: {"id": 24, "name": "Garp"},
    25: {"id": 25, "name": "Sengoku"},
    26: {"id": 26, "name": "Fujitora"},
    27: {"id": 27, "name": "Kizaru"},
    28: {"id": 28, "name": "Aokiji"},
    29: {"id": 29, "name": "Akainu"},
    30: {"id": 30, "name": "Smoker"},
    31: {"id": 31, "name": "Coby"},
    32: {"id": 32, "name": "Drake"},
    33: {"id": 33, "name": "Hawkins"},
    34: {"id": 34, "name": "Apoo"},
    35: {"id": 35, "name": "Bon Clay"},
    36: {"id": 36, "name": "Crocodile"},
    37: {"id": 37, "name": "Enel"},
    38: {"id": 38, "name": "Kuma"},
    39: {"id": 39, "name": "Ivankov"},
    40: {"id": 40, "name": "Reiju"},
    41: {"id": 41, "name": "Ichiji"},
    42: {"id": 42, "name": "Niji"},
    43: {"id": 43, "name": "Yonji"},
    44: {"id": 44, "name": "Caesar"},
    45: {"id": 45, "name": "Katakuri"},
    46: {"id": 46, "name": "Perospero"},
    47: {"id": 47, "name": "Cracker"},
    48: {"id": 48, "name": "Oven"},
    49: {"id": 49, "name": "Daifuku"},
    50: {"id": 50, "name": "Marco"},
    51: {"id": 51, "name": "Jozu"},
    52: {"id": 52, "name": "Vista"},
    53: {"id": 53, "name": "King"},
    54: {"id": 54, "name": "Queen"},
    55: {"id": 55, "name": "Jack"},
    56: {"id": 56, "name": "Shiryu"},
    57: {"id": 57, "name": "Lafitte"},
    58: {"id": 58, "name": "Van Augur"},
    59: {"id": 59, "name": "Doc Q"},
    60: {"id": 60, "name": "Burgess"},
    61: {"id": 61, "name": "Devon"},
    62: {"id": 62, "name": "Pizarro"},
    63: {"id": 63, "name": "Wolf"},
    64: {"id": 64, "name": "Sanjuan"},
    65: {"id": 65, "name": "Kuro"},
    66: {"id": 66, "name": "Arlong"},
    67: {"id": 67, "name": "Hody"},
    68: {"id": 68, "name": "Zephyr"},
    69: {"id": 69, "name": "Shiki"},
    70: {"id": 70, "name": "Tesoro"},
    71: {"id": 71, "name": "Urouge"},
    72: {"id": 72, "name": "Bellamy"},
    73: {"id": 73, "name": "Kyros"},
    74: {"id": 74, "name": "Sabo"},
    75: {"id": 75, "name": "Koala"},
    76: {"id": 76, "name": "Hack"},
    77: {"id": 77, "name": "Barto"},
    78: {"id": 78, "name": "Cavendish"},
    79: {"id": 79, "name": "Sai"},
    80: {"id": 80, "name": "Leo"},
    81: {"id": 81, "name": "Hajrudin"},
    82: {"id": 82, "name": "Orlumbus"},
    83: {"id": 83, "name": "Ideo"},
    84: {"id": 84, "name": "Gambia"},
    85: {"id": 85, "name": "Stussy"},
    86: {"id": 86, "name": "Morgans"},
    87: {"id": 87, "name": "Duval"},
    88: {"id": 88, "name": "Sentomaru"},
    89: {"id": 89, "name": "Hina"},
    90: {"id": 90, "name": "Tashigi"},
    91: {"id": 91, "name": "Vergo"},
    92: {"id": 92, "name": "Monet"},
    93: {"id": 93, "name": "Dellinger"},
    94: {"id": 94, "name": "Pekoms"},
    95: {"id": 95, "name": "Tamago"},
    96: {"id": 96, "name": "Pedro"},
    97: {"id": 97, "name": "Carrot"},
    98: {"id": 98, "name": "Wanda"},
    99: {"id": 99, "name": "Bepo"},
    100: {"id": 100, "name": "Corazon"},
}

item_db = ["ITEM_1","ITEM_2","ITEM_3","ITEM_4"]



#FastAPI Setup : Basic Web App
@app.get("/")
async def root():
    return {"Message" : f"Hi Luffy"}

#FastAPI Setup : Path Parameters
@app.get("/api/{name}")
async def name(name):
    return {"Message" : name}

#FastAPI Setup : Accessing data from Route by ID
@app.get("/name/{id}")
async def getuser_byid(id:int):
    user = users_db.get(id)
    return user

@app.get("/items/")
async def get_items(item_id : int):
    item = item_db[item_id]
    return {"Item_Name" : item}


