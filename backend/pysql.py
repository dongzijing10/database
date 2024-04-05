"""
Connects to a SQL database using pymssql
"""

import pymssql

conn = pymssql.connect(
    server = 'ZIJING-PC',
    user = 'sa',
    password = '19222126',
    database = 'kechengsheji',
    as_dict = True
)

SQL_QUERY = 
