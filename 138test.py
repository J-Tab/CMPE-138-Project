'''
requirements:
python 3
pip
do:
pip install  mysqlclient
modify your connections in the .connect below
in cursor.execute("") enter your sql statements if it were in a mysqlworkbench script, but without the semicolon
if it says try by itself, it worked, if its try then except, then it rolled back
this is purely for example uses
'''

import MySQLdb


conn = MySQLdb.connect(host="localhost",port = 3306, user="root", passwd="root",db="138proj")

conn.autocommit = False
cursor = conn.cursor()



# select example
try:
    print('try: ')
    cursor.execute("select * from test;")
    row = cursor.fetchone()
    print(row)
    cursor.close()
    conn.commit()
except:
    print('except: ')
    conn.rollback()

conn.close()

'''
#insert
try:
    print('try: ')
    cursor.execute("INSERT INTO test (statement) VALUES ('Test2')")
    cursor.close()
    conn.commit()
except:
    print('except: ')
    conn.rollback()

conn.close()
'''

'''
# delete
try:
    print('try: ')
    cursor.execute("DELETE from test where statement = 'Test1'")
    cursor.close()
    conn.commit()
except:
    print('except: ')
    conn.rollback()

conn.close()
'''

# row = cursor.fetchone()
# print('id:', row.user_id)

# rows = cursor.fetchall()
# for row in rows:
#   print(row.user_id, row.user_name)

# cursor.execute("""
#    select user_id, user_name
#      from users
#     where last_logon < ?
#       and bill_overdue = ?
# """, datetime.date(2001, 1, 1), 'y')

# insert
# cursor.execute("insert into products(id, name) values (?, ?)", 'pyodbc', 'awesome library')
# cnxn.commit()

# update & delete
# cursor.execute("delete from products where id <> ?", 'pyodbc')
# print(cursor.rowcount, 'products deleted')
# cnxn.commit()

