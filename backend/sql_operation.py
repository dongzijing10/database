import pymssql
import models 


connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'kechengsheji',
    as_dict = True
)
cursor = connect.cursor()

def getInfo(info:models.tableInfo):
    if(info.tableName == 'category'):
        cursor.execute('select * from category where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'customers'):
        cursor.execute('select * from customers where ID = %s',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'orderdetail'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'orders'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'products'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'proinfo'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'shippers'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'suppliers'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))


def categoryInput(info:models.category):
    cursor.execute('insert into category(ID,cname,explain) values(%d,%s,%s)',
                   (info.id,info.cname,info.explain))
    connect.commit()
    # cursor.execute('select * from category where ID = %d',info.id)    
    # for row in cursor:
    #     return('row = %s' % (row,))

def customersInput(info:models.customers):#(cID,cname,pname,pjob,cadd,city,area,postcode,country,phone,fax) 
    cursor.execute('insert into customers(cID,cname,pname,pjob,cadd,city,area,postcode,country,phone,fax) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (info.cID,info.cname,info.pname,info.pjob,info.cadd,info.city,info.area,info.postcode,info.country,info.phone,info.fax))
    connect.commit()

def orderdetailInput(info:models.orderdetail):
    cursor.execute('insert into orderdetail values(%d,%d,%d,%s)',
                   (info.orderid,info.productid,info.num,info.remark))
    connect.commit()

def ordersInput(info:models.orders):
    cursor.execute('insert into orders(ID,orderdate,starttime,arrivaltime,confirmtime,cost,name,addr,city,area,postcode,paymethon,insurance) values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)',
                   (info.ID,info.orderdate,info.starttime,info.arrivaltime,info.confirmtime,info.cost,info.name,info.addr,info.city,info.area,info.postcode,info.paymethod,info.insurance))
    connect.commit()

def productsInput(info:models.products):
    cursor.execute('insert into products(ID,name,num,price,inventory,ordernum,reordernum,supplystate) values(%d,%s,%s,%d,%d,%d,%d,%s)',
                   (info.ID,info.price,info.inventory,info.ordernum,info.reordernum,info.supplystate))
    connect.commit()

def proinfoInput(info:models.proinfo):
    cursor.execute('insert into proinfo(ID,productID,prodate,expiration) values(%d,%d,%s,%s)',
                   (info.ID,info.productID,info.prodate,info.expirationdate))
    connect.commit()

def shippersInput(info:models.shippers):
    cursor.execute('insert into shippers(sID,sname,phone,tool) values(%d,%s,%s,%s)',
                   (info.sID,info.sname,info.phone,info.tool))
    connect.commit()

def suppliersInput(info:models.suppliers):
    cursor.execute('insert into suppliers(ID,name,pname,pjob,address,city,area,postcode,country,phone,fax,homepage) values(%d,%s,%s)',
                   (info.ID,info.name,info.pname,info.pjob,info.address,info.city,info.area,info.postcode,info.country,info.phone,info.fax,info.homepage))
    connect.commit()

def Order_update(info:models.orders):
    cursor.executr('update orders set cost = %d where ID = %d',(info.cost,info.ID))
    cursor.commit()

# cursor.close()    
# connect.close()     



