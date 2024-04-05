import sql_operation
from models import Info
from fastapi import FastAPI
from pydantic import BaseModel

#uvicorn pysqlbackend:app --reload
app = FastAPI()

@app.post("/getInfo/")
def getInfo(info:Info):
    return sql_operation.getInfo(info)



         