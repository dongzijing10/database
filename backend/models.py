from pydantic import BaseModel
from typing import Optional


class tableInfo(BaseModel):
    tableName: str
    id: int|str


class category(BaseModel):
    id: int|str
    cname: str
    explain: str
    setup: str
    update: str
    pname:str
    pjob: str
    cadd: str
    city: str
    
class updateInfo(BaseModel):
    tablename: str
    categoryInput: category   #嵌套定义类，将外面的类引用到类内部，在内部也可以嵌套，但其他的函数引用内部类时麻烦

    # class customers():

info:updateInfo




