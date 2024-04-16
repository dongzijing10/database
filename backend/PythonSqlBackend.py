import models 
import SqlOperation
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#uvicorn PythonSqlBackend:app --reload

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
async def GetData(user: models.User):    
    return {"message": f"Hello, {user.userName}!"}

@app.post("/GetInfo/")
async def GetInfo(info:models.tableInfo):
    return SqlOperation.GetInfo(info)

@app.post("/InsertCategory/")
async def InsertCategory(info:models.category):
    return SqlOperation.InsertCategory(info)

@app.post("/InsertCustomers/")
async def InsertCustomers(info:models.customers):
    return SqlOperation.InsertCustomer(info)

@app.post("/InsertOrderDetail/")
async def InsertOrderDetail(info:models.orderdetail):
    return SqlOperation.InsertOrderDetail(info)

@app.post("/InsertOrder/")
async def InsertOrder(info:models.orders):
    return SqlOperation.InsertOrder(info)

@app.post("/InsertPici/")
async def InsertPici(info:models.pici):
    return SqlOperation.InsertPici(info)

@app.post("/InsertProducts/")
async def InsertProducts(info:models.products):
    return SqlOperation.InsertProducts(info)

@app.post("/InsertProinfo/")
async def InsertProinfo(info:models.category):
    return SqlOperation.InsertCategory(info)

@app.post("/InsertRule/")
async def InsertRule(info:models.rule):
    return SqlOperation.InsertRules(info)

@app.post("/InsertShippers/")
async def InsertShippers(info:models.shippers):
    return SqlOperation.InsertShippers(info)

@app.post("/InsertSuppliers/")
async def InsertSuppliers(info:models.suppliers):
    return SqlOperation.InsertSuppliers(info)

@app.post("/Remove")
async def Remove(info:models.tableInfo):
    return SqlOperation.RemoveInfo(info)

@app.post("/GetProductsOfCategory/")
async def GetProductsOfCategory(CategoryID:int):
    return SqlOperation.GetProductsOfCategory(CategoryID)

@app.get("/GetAllProductsOfCategory/")
async def GetAllProductsOfCategory():
    return SqlOperation.GetAllProductsOfCategory()

@app.post("/GetPicturesofProducts/")
async def  GetPicturesofProducts(CategoryID:int):
    return SqlOperation. GetPicturesofProducts(CategoryID)

@app.post("/CountProductsOforder")
async def CountProductsOforder(orderID:int):
    return SqlOperation.CountProductOfOrder(orderID)

@app.get("/CountProductsNumOfAreaAndCustomers")
async def CountOrderNumOfAreaAndCustomers():
    return SqlOperation.CountOrderNumOfAreaAndCustomers()

@app.get("/CountOrderNumOfArea/")
async def CountOrderNumOfArea():
    return SqlOperation.CountOrderNumOfArea()

@app.get("/CountOrderNumOfSeason/")
async def CountOrderNumOfSeason():
    return SqlOperation.CountOrderNumOfSeason()

@app.get("/PriceOfProductsOfSuppliers/")
async def PriceOfProductsOfSuppliers():
    return SqlOperation.PriceOfProductsOfSuppliers()\
    
@app.get("/TotalMoneyOfSuppliers/")
async def TotalMoneyOfSuppliers():
    return SqlOperation.TotalMoneyOfSuppliers()

@app.get("/CountOrdersOfShippers/")
async def CountOrdersOfShippers():
    return SqlOperation.CountOrdersOfShippers()

@app.post("/CountOrdersOfSuppliers/")
async def CountOrdersOfSuppliers(categoryID:int):
    return SqlOperation.CountOrdersOfSuppliers(categoryID)


         