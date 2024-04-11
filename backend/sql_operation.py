import pymssql
import models 


connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'DatabaseCourseDesign',
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

def insertInfo(info:models.insertInfo):
    if(info.tableName == "category"):
        cursor.execute('insert into category(ID,cname,explain,setup,updatetime) values(%d,%s,%s,%s,%s)',
                   (info.categoryInput.id,info.categoryInput.cname,info.categoryInput.explain,info.categoryInput.setup,info.categoryInput.update))
        connect.commit()
    # cursor.execute('select * from category where ID = %d',info.id)    
    # for row in cursor:
    #     return('row = %s' % (row,))
    elif(info.tableName == 'customers'):#(cID,cname,pname,pjob,cadd,city,area,postcode,country,phone,fax) 
        cursor.execute('insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (info.customersInput.cID,info.customersInput.cname,info.customersInput.pname,info.customersInput.pjob,info.customersInput.caddress,info.customersInput.city,
                    info.customersInput.area,info.customersInput.postcode,info.customersInput.country,info.customersInput.phone,info.customersInput.fax))
        connect.commit()
    elif(info.tableName == 'orderdetail'):#(orderID,productID,num,remark)
        cursor.execute('insert into orderdetail values(%d,%d,%d,%s)',
                   (info.orderdetailInput.orderid,info.orderdetailInput.productid,info.orderdetailInput.num,info.orderdetailInput.remark))
        connect.commit()
    elif(info.tableName == 'orders'):#(ID,orderdate,starttime,arrivaltime,confirmtime,cost,name,addr,city,area,postcode,paymethon,insurance)
        cursor.execute('insert into orders values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)',
                   (info.ordersInput.ID,info.ordersInput.customerID,info.ordersInput.employeeID,info.ordersInput.orderdate,info.ordersInput.starttime,info.ordersInput.arrivaltime,info.ordersInput.confirmtime,
                    info.ordersInput.cost,info.ordersInput.name,info.ordersInput.addr,info.ordersInput.city,info.ordersInput.area,info.ordersInput.postcode,info.ordersInput.country,info.ordersInput.paymethod,info.ordersInput.insurance))
        connect.commit()
    elif(info.tableName=='pici'):
        cursor.execute('insert into pici values(%d)',(info.piciInput.ID))
    elif(info.tableName == 'products'):#(ID,name,num,price,inventory,ordernum,reordernum,supplystate)
        cursor.execute('insert into products values(%d,%s,%s,%d,%d,%d,%d,%s)',
                   (info.productsInput.ID,info.productsInput.name,info.productsInput.num,info.productsInput.price,
                    info.productsInput.inventory,info.productsInput.ordernum,info.productsInput.reordernum,info.productsInput.supplystate))
        connect.commit()
    elif(info.tableName == 'proinfo'):#(ID,productID,prodate,expiration)
        cursor.execute('insert into proinfo values(%d,%d,%s,%s)',
                   (info.proinfoInput.piciID,info.proinfoInput.productID,
                    info.proinfoInput.prodate,info.proinfoInput.expirationdate))
        connect.commit()
    elif(info.tableName == 'rules'):#(ruleID,weight,cost,criterion)
        cursor.execute('insert into rules values(%d,%d,%d,%d)',
                   (info.ruleInput.id,info.ruleInput.weight,info.ruleInput.cost,info.ruleInput.cri))
        connect.commit()
    elif(info.tableName == 'shippers'):#(sID,sname,phone,tool)
        cursor.execute('insert into shippers values(%d,%s,%s,%s)',
                   (info.sID,info.sname,info.phone,info.tool))
        connect.commit()

    elif(info.tableName == 'suppliers'):#(ID,name,pname,pjob,address,city,area,postcode,country,phone,fax,homepage)
        cursor.execute('insert into suppliers values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (info.suppliersInput.ID,info.suppliersInput.name,info.suppliersInput.pname,info.suppliersInput.pjob,info.suppliersInput.address,
                    info.suppliersInput.city,info.suppliersInput.area,info.suppliersInput.postcode,info.suppliersInput.country,
                    info.suppliersInput.phone,info.suppliersInput.fax,info.suppliersInput.homepage))
        connect.commit()

def removeInfo(info):
    
def update(info:models.orders):
    cursor.executr('update orders set cost = %d where ID = %d',(info.cost,info.ID))
    connect.commit()

# cursor.close()    
# connect.close()     



