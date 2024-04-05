from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#uvicorn main:app --reload
app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/username")
def hello_username(username:str):
    return "hello " + username

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/items")
async def create_item(item: Item):
    print(1)
    return item

@app.post("/items")
async def create_item(item: Item):
    print(2)
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.description + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

    #little change