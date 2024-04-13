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

def GetInfo(info:models.tableInfo):
    if(info.tableName == 'category'):
        cursor.execute('select * from category where ID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'customers'):
        cursor.execute('select * from customers where cID = %s',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'orderdetail'):
        cursor.execute('select * from customers where orderID = %d and productID = %d',info.id,info.id1)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'orders'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'pici'):
        cursor.execute('select * from pici where ID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'products'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'proinfo'):
        cursor.execute('select * from customers where piciID = %d and productID= %d',info.id,info.id1)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'rules'):
        cursor.execute('select * from rules where ruleID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'shippers'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))
    elif(info.tableName == 'suppliers'):
        cursor.execute('select * from customers where ID = %d',info.id)    
        for row in cursor:
            return('%s' % (row,))

def InsertCategory(info:models.category):
    cursor.execute('insert into category(ID,cname,explain,setup,updatetime) values(%d,%s,%s,%s,%s)',
                   (info.id,info.cname,info.explain,info.setup,info.update))
    connect.commit()

def InsertCustomer(info:models.customers):#(cID,cname,pname,pjob,cadd,city,area,postcode,country,phone,fax,) 
    cursor.execute('insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s)',
                   (info.cID,info.cname,info.pname,info.pjob,info.caddress,info.city,info.area,info.postcode,info.country,info.phone,info.fax,info.id,info.password))
    connect.commit()

def InsertOrderDetail(info:models.orderdetail):#(orderID,productID,num,remark)
    cursor.execute('insert into orderdetail values(%d,%d,%d,%s)',
                   (info.orderid,info.productid,info.num,info.remark))
    connect.commit()

def InsertOrder(info:models.orders):#(ID,orderdate,starttime,arrivaltime,confirmtime,cost,name,addr,city,area,postcode,paymethon,insurance)
    cursor.execute('insert into orders values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)',
                   (info.ID,info.customerID,info.employeeID,info.orderdate,info.starttime,info.arrivaltime,info.confirmtime,
                    info.cost,info.name,info.addr,info.city,info.area,info.postcode,info.country,info.paymethod,info.insurance))
    connect.commit()

def InsertPici(info:models.pici):
    cursor.execute('insert into pici values(%d)',(info.piciInput.ID))
    connect.commit()

def InsertProducts(info:models.products):#(ID,name,num,price,inventory,ordernum,reordernum,supplystate)
    cursor.execute('insert into products values(%d,%s,%s,%d,%d,%d,%d,%s)',
                   (info.ID,info.name,info.num,info.price,info.inventory,info.ordernum,info.reordernum,info.supplystate))
    connect.commit()

def InsertProinfo(info:models.proinfo):#(ID,productID,prodate,expiration)
    cursor.execute('insert into proinfo values(%d,%d,%s,%s)',
                   (info.piciID,info.productID,info.prodate,info.expirationdate))
    connect.commit()

def InsertRules(info:models.rule):#(ruleID,weight,cost,criterion)
    cursor.execute('insert into rules values(%d,%d,%d,%d)',
                   (info.ruleInput.id,info.ruleInput.weight,info.ruleInput.cost,info.ruleInput.cri))
    connect.commit()

def InsertShippers(info:models.shippers):#(sID,sname,phone,tool)
    cursor.execute('insert into shippers values(%d,%s,%s,%s)',
                   (info.sID,info.sname,info.phone,info.tool))
    connect.commit()

def InsertSuppliers(info:models.suppliers):#(ID,name,pname,pjob,address,city,area,postcode,country,phone,fax,homepage)
    cursor.execute('insert into suppliers values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                   (info.ID,info.name,info.pname,info.pjob,info.address,info.city,info.area,info.postcode,info.country,info.phone,info.fax,info.homepage))
    connect.commit()

def RemoveInfo(info:models.tableInfo):
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

def CountProductOfOrder(info:int):
    cursor.execute('''
        SELECT orderdetail.orderID,orders.orderdate,orders.oname,orders.addr,sum(products.price*orderdetail.num) as totalcost
            FROM products
            JOIN orderdetail ON products.ID = orderdetail.productID  
			JOIN orders ON orders.ID = orderdetail.orderID
                where orderdetail.orderID = %d
		        group by orderdetail.orderID, orders.orderdate,orders.oname,orders.addr
        ''',info)
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def CountOrderNumOfAreaAndCustomers():
    cursor.execute('''
         SELECT orders.area, customers.cname,  SUM(orderdetail.num) AS total_num  
            FROM orders  
            JOIN orderdetail ON orders.ID = orderdetail.orderID
			JOIN customers ON orders.cid=customers.cID
			GROUP BY customers.cname,orders.area
        ''')
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def CountOrderNumOfArea():
    cursor.execute('''
         SELECT orders.area, SUM(orderdetail.num) AS total_num  
            FROM orders  
            JOIN orderdetail ON orders.ID = orderdetail.orderID
			GROUP BY orders.area
        ''')
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def CountOrderNumOfSeason():
    cursor.execute('''
        SELECT  
            CASE  
            WHEN DATEPART(MONTH, orders.orderdate) IN (12, 1, 2) THEN 'winter'  
            WHEN DATEPART(MONTH, orders.orderdate) IN (3, 4, 5) THEN 'spring'  
            WHEN DATEPART(MONTH, orders.orderdate) IN (6, 7, 8) THEN 'summer'  
            WHEN DATEPART(MONTH, orders.orderdate) IN (9, 10, 11) THEN 'autumn'  
            ELSE '未知季节'  
        END AS season,  
        SUM(orderdetail.num) AS total_quantity  
        FROM  orders   
        JOIN  orderdetail  ON orders.id = orderdetail.orderid  
        GROUP BY  
            CASE  
            WHEN DATEPART(MONTH, orders.orderdate) IN (12, 1, 2) THEN 'winter'  
            WHEN DATEPART(MONTH, orders.orderdate) IN (3, 4, 5) THEN 'spring'  
            WHEN DATEPART(MONTH, orders.orderdate) IN (6, 7, 8) THEN 'summer'  
            WHEN DATEPART(MONTH, orders.orderdate) IN (9, 10, 11) THEN 'autumn'  
            ELSE '未知季节'  
        END;
        ''')
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def PriceOfProductsOfSuppliers():
    cursor.execute('''
        SELECT suppliers.ID AS supplier_id,  suppliers.sname,  products.ID AS product_id, products.cname, products.price AS product_price  
        FROM suppliers   
        JOIN products  ON suppliers.ID= products.sid  
        ORDER BY  suppliers.ID ASC, products.ID ASC;
    ''') 
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def TotalMoneyOfSuppliers():
    cursor.execute('''
        SELECT suppliers.ID, suppliers.sname, SUM(products.price * orderdetail.num) AS total_amount_per_supplier  
        FROM suppliers   
        JOIN  products  ON suppliers.ID = products.sid  
        JOIN  orderdetail ON products.ID = orderdetail.productID
        GROUP BY  suppliers.ID,suppliers.sname
        order by suppliers.ID ASC
    ''')
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def CountOrdersOfShippers():
    cursor.execute('''
        SELECT  shippers.ID,shippers.sname,COUNT(orders.id) AS total_orders 
        FROM shippers   
        LEFT JOIN  orders  ON shippers.id = orders.employeeid  
        GROUP BY  shippers.ID, shippers.sname  
        ORDER BY  total_orders DESC;
    ''')
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple

def CountOrdersOfSuppliers(info:int):
    cursor.execute('''
        SELECT category.ID, category.cname, suppliers.ID, suppliers.sname, SUM(orderdetail.num) AS total_quantity_supplied 
        FROM  category   
        JOIN  products  ON category.ID = products.cID  
        JOIN  orderdetail  ON products.id = orderdetail.productid  
        JOIN  orders  ON orderdetail.orderid = orders.id 
        JOIN  suppliers  ON products.sid = suppliers.id  
            WHERE category.ID = %d
        GROUP BY category.ID, category.cname, suppliers.id, suppliers.sname 
        ORDER BY category.ID, suppliers.id;
    ''',info)
    totaltuple=()
    newtuple=()
    for row in cursor:
        newtuple=(row,)
        totaltuple=newtuple+totaltuple
    return totaltuple


# cursor.close()    
# connect.close()     



