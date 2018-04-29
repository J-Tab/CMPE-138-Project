import MySQLdb
import os

#used to clear console in windows environment
def clearConsole():
    clearing = lambda: os.system('cls')
    clearing()

def startNewProject ():
    fname = input('What is your first name: ')
    lname = input('What is your last name: ')
    userid = 777
    salary = 0
    motivation = 0
    exp = 0
    intel = 0

    #check if database exists 
    #note to developers, please change the first conn to a database that exists
    conn = MySQLdb.connect(host="localhost",port = 3306, user="root", passwd="root",db="138proj")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS 138Company")
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    clearConsole()
    conn.close()

    #change connection to the new database, create tables if not exist
    conn = MySQLdb.connect(host="localhost",port = 3306, user="root", passwd="root",db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS employee (e_id INTEGER NOT NULL, salary INTEGER NOT NULL, motivation INTEGER NOT NULL, experience INTEGER NOT NULL, intellligence INTEGER NOT NULL, f_name char(20) NOT NULL, l_name char(20) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS user (e_id INTEGER NOT NULL, department char(20) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS to_be_hired (e_id INTEGER NOT NULL, expire_time INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS projects (p_id INTEGER NOT NULL, potential_profit INTEGER NOT NULL, deadline INTEGER NOT NULL, sucess_rate INTEGER NOT NULL, cost INTEGER NOT NULL, difficulty INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS e_p (e_id INTEGER NOT NULL, p_id INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS works_in (e_id INTEGER NOT NULL, department char(20) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS report (r_id INTEGER NOT NULL, misfortune_id INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS engineering_department (name char(20) NOT NULL, level INTEGER NOT NULL, budget INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS marketing_department (name char(20) NOT NULL, fame_amt INTEGER NOT NULL, fame_to_next_level INTEGER NOT NULL)")
        conn.commit()
    except:
        conn.rollback()
    clearConsole()

    #alter table constraints
    try:
        print("try: ")
        #cursor.execute("ALTER TABLE employee ADD CONSTRAINT PK_employee PRIMARY KEY (e_id)")
        cursor.execute("ALTER IGNORE TABLE user ADD CONSTRAINT PK_user PRIMARY KEY (e_id)")
        #cursor.execute("ALTER TABLE to_be_hired ADD CONSTRAINT PK_to_be_hired PRIMARY KEY (e_id)")
        #cursor.execute("ALTER TABLE projects ADD CONSTRAINT PK_projects PRIMARY KEY (p_id)")
        #cursor.execute("ALTER TABLE e_p ADD CONSTRAINT PK_e_p PRIMARY KEY (e_id, p_id)")
        #cursor.execute("ALTER TABLE works_in ADD CONSTRAINT PK_works_in PRIMARY KEY (e_id, department)")
        #cursor.execute("ALTER TABLE report ADD CONSTRAINT PK_report PRIMARY KEY (r_id)")
        #cursor.execute("ALTER TABLE engineering_department ADD CONSTRAINT PK_engineering_department PRIMARY KEY (name)")
        #cursor.execute("ALTER TABLE marketing_department ADD CONSTRAINT PK_marketing_department PRIMARY KEY (name)")
        conn.commit()
    except:
        print("rollback: ")
        conn.rollback()
    conn.close()

    '''
    #insert default values into table
    try:
        print("try: ")
        #cursor.execute("INSERT IGNORE INTO engineering_department values('engineering', 1, 1000)")
        #cursor.execute("INSERT IGNORE INTO marketing_department values('marketing', 1, 15)")
        #cursor.execute("INSERT IGNORE INTO user values(%i, 'engineering')", userid)
        cursor.close()
        conn.commit()
    except:
        print("rollback: ")
        conn.rollback()
    conn.close()
    '''
# main

#main menu

startNewProject()

















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

