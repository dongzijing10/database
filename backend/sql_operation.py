import pymssql
import models 


connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'test',
    as_dict = True
)
cursor = connect.cursor()

def getInfo(info:models.tableInfo):
    if(info.tableName == 'category'):
        cursor.execute('select * from category where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'customers'):
        cursor.execute('select * from customers where cID = %s',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'orderdetail'):
        cursor.execute('select * from customers where orderID = %d and productID = %d',info.id,info.id1)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'orders'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'pici'):
        cursor.execute('select * from pici where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'products'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'proinfo'):
        cursor.execute('select * from customers where piciID = %d and productID= %d',info.id,info.id1)    
        for row in cursor:
            return('row = %s' % (row,))
    elif(info.tableName == 'rules'):
        cursor.execute('select * from rules where ruleID = %d',info.id)    
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

def insertcategory(info:models.category):
    cursor.execute('insert into category(ID,cname,explain,setup,updatetime) values(%d,%s,%s,%s,%s)',
                   (info.id,info.cname,info.explain,info.setup,info.update))
    connect.commit()

def insertcustomer(info:models.customers):#(cID,cname,pname,pjob,cadd,city,area,postcode,country,phone,fax,) 
    cursor.execute('insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s)',
                   (info.cID,info.cname,info.pname,info.pjob,info.caddress,info.city,info.area,info.postcode,info.country,info.phone,info.fax,info.id,info.password))
    connect.commit()

def insertorderdetail(info:models.orderdetail):#(orderID,productID,num,remark)
    cursor.execute('insert into orderdetail values(%d,%d,%d,%s)',
                   (info.orderid,info.productid,info.num,info.remark))
    connect.commit()

def insertorder(info:models.orders):#(ID,orderdate,starttime,arrivaltime,confirmtime,cost,name,addr,city,area,postcode,paymethon,insurance)
    cursor.execute('insert into orders values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)',
                   (info.ID,info.customerID,info.employeeID,info.orderdate,info.starttime,info.arrivaltime,info.confirmtime,
                    info.cost,info.name,info.addr,info.city,info.area,info.postcode,info.country,info.paymethod,info.insurance))
    connect.commit()

def insertpici(info:models.pici):
    cursor.execute('insert into pici values(%d)',(info.piciInput.ID))
    connect.commit()

def insertproducts(info:models.products):#(ID,name,num,price,inventory,ordernum,reordernum,supplystate)
    cursor.execute('insert into products values(%d,%s,%s,%d,%d,%d,%d,%s)',
                   (info.ID,info.name,info.num,info.price,info.inventory,info.ordernum,info.reordernum,info.supplystate))
    connect.commit()

def insertproinfo(info:models.proinfo):#(ID,productID,prodate,expiration)
    cursor.execute('insert into proinfo values(%d,%d,%s,%s)',
                   (info.piciID,info.productID,info.prodate,info.expirationdate))
    connect.commit()

def insertrules(info:models.rule):#(ruleID,weight,cost,criterion)
    cursor.execute('insert into rules values(%d,%d,%d,%d)',
                   (info.ruleInput.id,info.ruleInput.weight,info.ruleInput.cost,info.ruleInput.cri))
    connect.commit()

def insertshippers(info:models.shippers):#(sID,sname,phone,tool)
    cursor.execute('insert into shippers values(%d,%s,%s,%s)',
                   (info.sID,info.sname,info.phone,info.tool))
    connect.commit()

def insertsuppliers(info:models.suppliers):#(ID,name,pname,pjob,address,city,area,postcode,country,phone,fax,homepage)
    cursor.execute('insert into suppliers values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (info.ID,info.name,info.pname,info.pjob,info.address,info.city,info.area,info.postcode,info.country,info.phone,info.fax,info.homepage))
    connect.commit()

def removeInfo(info:models.tableInfo):
    if(info.tableName == 'category'):
        cursor.execute('delete from category where ID = %d',info.id)
        connect.commit()
    elif(info.tableName == 'customers'):
        cursor.execute('delete from customers where cID = %s',info.id)    
        connect.commit()    
    elif(info.tableName == 'orderdetail'):
        cursor.execute('delete from customers where orderID = %d and productID = %d',info.id,info.id1)
        connect.commit()    
    elif(info.tableName == 'orders'):
        cursor.execute('delete from customers where ID = %d',info.id)    
        connect.commit()        
    elif(info.tableName == 'pici'):
        cursor.execute('delete from pici where ID = %d',info.id)    
    elif(info.tableName == 'products'):
        cursor.execute('delete from customers where ID = %d',info.id)    
        connect.commit()        
    elif(info.tableName == 'proinfo'):
        cursor.execute('delete from customers where piciID = %d and productID= %d',info.id,info.id1)    
        connect.commit()        
    elif(info.tableName == 'rules'):
        cursor.execute('delete from rules where ruleID = %d',info.id)    
        connect.commit()        
    elif(info.tableName == 'shippers'):
        cursor.execute('delete from customers where ID = %d',info.id)    
        connect.commit()        
    elif(info.tableName == 'suppliers'):
        cursor.execute('delete from customers where ID = %d',info.id)    
        connect.commit()       

def count_order_product(info:models.countorderproduct):
    cursor.execute('SELECT * FROM products JOIN orderdetail ON products.ID = orderdetail.productID  where orderdetail.orderID = %d',info.orderid)
    for row in cursor:
            return('row = %s' % (row,))

def count_order_area():
    return 0
# cursor.close()    
# connect.close()     



