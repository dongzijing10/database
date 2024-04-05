import pymssql
from models import Info


connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'kechengsheji',
    as_dict = True
)
cursor = connect.cursor()

def getInfo(info:Info):
    cursor.execute('select cname from category where ID = %d',info.id)    
    for row in cursor:
        return('row = %s' % (row,))




