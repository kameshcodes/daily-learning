from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()

@app.get("/")
async def index(name):  
    return "Hello, This is {}, revising Fastapi....\nPlese order your food\nCheck Cuisines".format(name)


# food_items = {
#     "indian":["Dosa", "Idli"],
#     "italian": ["Pasta", "Pizza"]
# }

# valid_cusines=food_items.keys()

# @app.get("/get_items/{cuisines}")
# async def get_items(cuisines):
#     if cuisines not in valid_cusines:
#         return f"Supported Cusinies are {valid_cusines}"
    
#     return food_items[cuisines]

class AvailableCuisines(str, Enum):
    indian = "indian"
    italian = "italian"
    south = "south"

food_items = {
    "south":["Dosa", "Idli", "sambhar"],
    "italian": ["Pasta", "Pizza"],
    "indian": ["Panner", "Puri"]
}

valid_cusines=food_items.keys()


@app.get("/get_item/{cuisines}")
async def get_item(cuisines):
    return food_items[cuisines]


if __name__=="__main__":
    uvicorn.run(app, port = 8002)