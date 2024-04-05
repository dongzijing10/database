import pymssql
from fastapi import FastAPI
#uvicorn pysqlbackend:app --reload
app = FastAPI()

connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'kechengsheji',
    as_dict = True
)
cursor = connect.cursor()

@app.get("/selsect/{role}/{id}")
def select(role:str,id:int):
    cursor = connect.cursor()
    cursor.execute('select cname from category where ID = %d','1')    
    for row in cursor:
        return('row = %s' % (row,))
    
# @app.get()
# def insert()
         