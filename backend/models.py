from pydantic import BaseModel


class Info(BaseModel):
    role:str
    id:int