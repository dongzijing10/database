import cursor
from fastapi import FastAPI
from pydantic import BaseModel

#uvicorn pysqlbackend:app --reload
app = FastAPI()

class info(BaseModel):
    role:str
    id:int

@app.get("/selsect/")
def select(info:info):
    print("进入函数")
    cursor.select(info.role,info.id)

         