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


def putInData(info:models.category):
    cursor.execute('insert into category(ID,cname,explain) values(%d,%s,%s)',(9,info.cname,info.explain))
    connect.commit()
    cursor.execute('select * from category ')    
    for row in cursor:
        return('row = %s' % (row,))

        # for row in cursor:
        #     return('row = %s' % (row,))

# cursor.close()    
# connect.close()     



