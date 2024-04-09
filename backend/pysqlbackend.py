import sql_operation
import models 
from fastapi import FastAPI

#uvicorn pysqlbackend:app --reload
app = FastAPI()

@app.post("/getInfo/")
def getInfo(info:models.tableInfo):
    return sql_operation.getInfo(info)

@app.post("/update/")
def update(info:models.insertInfo):
    if(info.tableName == "category"):
        return sql_operation.categoryInput(info.categoryInput)
    elif(info.tableName == 'customers'):
        return sql_operation.putInData(info.customersInput)
    elif(info.tableName == 'orderdetail'):
        return sql_operation.putInData(info.orderdetailInput)
    elif(info.tableName == 'orders'):
        return sql_operation.putInData(info.ordersInput)
    elif(info.tableName == 'products'):
        return sql_operation.putInData(info.productsInput)
    elif(info.tableName == 'proinfo'):
        return sql_operation.putInData(info.proinfoInput)
    elif(info.tableName == 'shippers'):
        return sql_operation.putInData(info.shippersInput)
    elif(info.tableName == 'suppliers'):
        return sql_operation.putInData(info.suppliersInput)




         