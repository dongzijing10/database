import pymssql

connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'kechengsheji',
    as_dict = True
)
cursor = connect.cursor()

def select(role:str,id:int):
    print("进入函数")
    cursor.execute('select cname from category where ID = %d','1')    
    for row in cursor:
        print('row = %s' % (row,))
        return('row = %s' % (row,))