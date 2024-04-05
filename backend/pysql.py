#python中，"""可以实现字符串跨行输入输出
"""     
Connects to a SQL database using pymssql
"""

import pymssql

connect = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'kechengsheji',
    as_dict = True
)

if connect:
    print("数据库连接成功")

#多行查询或者其他操作用""" """包括，单行可以使用" " 或 ''  包括，在语句中" "  和' ' 作用相同 
SQL_QUERY = """ 
   select * from category
"""
cursor = connect.cursor()
# cursor.execute(SQL_QUERY)   #在语句简单的情况下，可以直接加到execute的()中，不需要定义SQL_QUERY
cursor.execute('select * from category')    

#此处输入类似于c;由%确定输出格式，后面%之后的内容为输出内容    printf("i=%d",i)
print("以元组形式返回")
for row in cursor:
    print('row = %s' % (row,))  #row  = %r 或者 %s 都是占位符，将后面的内容转换为字符串输出，也可以直接 print(row,);输出中的\r\n哪来的

cursor.execute(SQL_QUERY)       #游标类似于一个指针，上一个循环到了最后，这里重置下面才能使用
# cursor.execute("select * from category")
print("以字典形式返回")
for row in cursor:
    print("ID=%d, Name=%s" % (row['ID'], row['cname']), end = '')    #自动换两行：在中文字符串结束后python加了一个\r\n,在print最后默认end是\n

print("操作执行")

# connect.commit()    #修改操作需要提交，查询不需要
cursor.close()     #关闭游标
connect.close()     #如果不关，python一直占用

