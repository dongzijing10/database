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
    return sql_operation.insertInfo(info)






         