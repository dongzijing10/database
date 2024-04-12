import sql_operation
import models 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Any


# app = FastAPI()

# origins = [
#     "http://localhost:8080",  # Allow your local website
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#uvicorn pysqlbackend:app --reload

from pydantic import BaseModel
class User(BaseModel):    
    userName: str    
    Id: int
app = FastAPI()
origins = [ 
    "*",  # Allow all origins
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
@app.post("/api/data")
async def get_data(user: User):    
    return {"message": f"Hello, {user.userName}!"}

@app.post("/getInfo/")
async def getInfo(info:models.tableInfo):
    return sql_operation.getInfo(info)

@app.post("/insertcategory/")
async def insert(info:models.category):
    return sql_operation.insertcategory(info)

@app.post("/insertcustomers/")
async def insert(info:models.customers):
    return sql_operation.insertcustomers(info)

@app.post("/insertorderdetail/")
async def insert(info:models.orderdetail):
    return sql_operation.insertorderdetail(info)

@app.post("/insertorder/")
async def insert(info:models.orders):
    return sql_operation.insertorder(info)

@app.post("/insertpici/")
async def insert(info:models.pici):
    return sql_operation.insertpici(info)

@app.post("/insertproducts/")
async def insert(info:models.products):
    return sql_operation.insertproducts(info)

@app.post("/insertproinfo/")
async def insert(info:models.category):
    return sql_operation.insertcategory(info)

@app.post("/insertrule/")
async def insert(info:models.rule):
    return sql_operation.insertrules(info)

@app.post("/insertshippers/")
async def insert(info:models.shippers):
    return sql_operation.insertshippers(info)

@app.post("/insertsuppliers/")
async def insert(info:models.suppliers):
    return sql_operation.insertsuppliers(info)

@app.post("/delete")
async def remove(info:models.tableInfo):
    return sql_operation.removeInfo(info)

@app.post("/countorderproducts")
async def countorder(info:models.countorderproduct):
    return sql_operation.count_order_product(info)





         