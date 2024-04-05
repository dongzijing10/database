cursor = connect.cursor()
# cursor.execute('select cname from category where ID = %d','1')    #不需要定义SQL_QUERY可以直接在execute中输入多行语句

# #此处输入类似于c;由%确定输出格式，后面%之后的内容为输出内容    printf("i=%d",i)
# print("以元组形式返回")
# for row in cursor:
#     print('row = %s' % (row,))  #row  = %r 或者 %s 都是占位符，将后面的内容转换为字符串输出，也可以直接 print(row,);输出中的\r\n哪来的

# #注意，在sql语句中等于就是=，==执行不了
# SQL_QUERY = """ 
#    select * from category
#         where ID = %s
# """
# cursor.execute(SQL_QUERY,2)
# print("以字典形式返回")
# for row in cursor:
#     print("ID=%d, Name=%s" % (row['ID'], row['cname']), end = '')    #自动换两行：在中文字符串结束后python加了一个\r\n,在print最后默认end是\n

# sql = 'select * from category where id >= %s and id <= %s'		
# cursor.execute(sql, (1,3))			
# for row in cursor:
#     print('row = %s' % (row,))

# print("操作执行成功")

# # connect.commit()    #修改操作需要提交，查询不需要
# cursor.close()     #关闭游标
# connect.close()     #如果不关，python一直占用

