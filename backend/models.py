from pydantic import BaseModel
from typing import Optional
import datetime 

# Optional[str] = None

class tableInfo(BaseModel):
    tableName: str
    id: int|str

class category(BaseModel):
    id: int|str
    cname: str
    explain: str
    setup: datetime.date
    update: datetime.date
    picture: int

class customers(BaseModel):
    cID: str
    cname: str
    pname: str
    pjob: str
    caddress: str
    city: str
    area: str
    postcode: str
    country: str
    phone: str
    fax: str

class orderdetail(BaseModel):
    orderid: int 
    productid: int
    num: int
    remark: str

class orders(BaseModel):
    ID: int
    customerID: str
    employeeID: int
    orderdate: datetime.date
    starttime: datetime.date
    arrivaltime: datetime.date
    confirmtime: datetime.date
    cost: int
    name: str
    addr: str
    city: str
    area: str
    postcode: str
    country: str
    paymethod: str
    insurance: str

class pici(BaseModel):
    ID: int

class products(BaseModel):
    ID: int
    name: str
    num: str
    price: str
    inventory: int
    ordernum: int
    reordernum: int
    supplystate: bool

class proinfo(BaseModel):
    piciID: int
    productID: int 
    prodate: datetime.date
    expirationdate: datetime.date

class rule(BaseModel):
    id: int
    weight: int
    cost: str
    cri: str

class shippers(BaseModel):
    sID: int
    sname: str
    phone: str
    tool: str

class suppliers(BaseModel):
    ID: int
    name: str
    pname: str
    pjob: str
    address: str
    city: str
    area: str
    postcode: str
    country: str
    phone: str
    fax: str
    homepage: str

class insertInfo(BaseModel):
    tableName: str
    categoryInput: category   #嵌套定义类，将外面的类引用到类内部，在内部也可以嵌套，但其他的函数引用内部类时麻烦
    customersInput: customers
    orderdetailInput: orderdetail
    ordersInput: orders
    piciInput: pici
    productsInput: products
    proinfoInput: proinfo
    ruleInput: rule
    shippersInput: shippers
    suppliersInput: suppliers
    




