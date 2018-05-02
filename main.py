import MySQLdb
import os

#used to clear console in windows environment
def clearConsole():
    clearing = lambda: os.system('cls')
    clearing()

def removeProject():
    conn = MySQLdb.connect(host="localhost",port = 3306, user="root", passwd="admin",db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("DROP DATABASE 138Company")
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    

def startNewProject ():
    #fname = input('What is your first name: ')
    #lname = input('What is your last name: ')
    fname = 'Bob'
    lname = 'Ross'
    userid = 777
    salary = 0
    motivation = 0
    exp = 0
    intel = 0

    #check if database exists 
    #note to developers, please change the first conn to a database that exists
    conn = MySQLdb.connect(host="localhost",port = 3306, user="root", passwd="admin")
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
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
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
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    clearConsole()

    #alter table constraints
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE employee ADD CONSTRAINT PK_employee PRIMARY KEY (e_id)")
        cursor.execute("ALTER TABLE user ADD CONSTRAINT FK_user  FOREIGN KEY (e_id) REFERENCES employee(e_id) ON DELETE CASCADE")
        cursor.execute("ALTER TABLE to_be_hired ADD CONSTRAINT PK_to_be_hired PRIMARY KEY (e_id)")
        cursor.execute("ALTER TABLE projects ADD CONSTRAINT PK_projects PRIMARY KEY (p_id)")
        cursor.execute("ALTER TABLE report ADD CONSTRAINT PK_report PRIMARY KEY (r_id)")
        cursor.execute("ALTER TABLE engineering_department ADD CONSTRAINT PK_engineering_department PRIMARY KEY (name)")
        cursor.execute("ALTER TABLE marketing_department ADD CONSTRAINT PK_marketing_department PRIMARY KEY (name)")
        cursor.execute("ALTER TABLE e_p ADD CONSTRAINT FK_e_p FOREIGN KEY (e_id) REFERENCES employee(e_id) ON DELETE CASCADE")
        cursor.execute("ALTER TABLE works_in ADD CONSTRAINT FK_works_in FOREIGN KEY (e_id) REFERENCES employee(e_id) ON DELETE CASCADE")
        cursor.close()
        conn.commit()
    except:
        conn.rollback()

    #insert default values into table
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT IGNORE INTO engineering_department values('engineering', 1, 1000)")
        cursor.execute("INSERT IGNORE INTO marketing_department values('marketing', 1, 15)")
        cursor.execute("INSERT IGNORE INTO employee values(%s, %s, %s, %s, %s, %s, %s)", (userid, salary, motivation, exp, intel, fname, lname))
        cursor.execute("INSERT ignore INTO user values(%s, %s)", (userid, 'engineering'))
        cursor.execute("INSERT ignore INTO works_in values(%s, %s)", (userid, 'engineering'))
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def toBeHired(fame, level):
    
    print(1)

def generate_to_be_hired():
    conn = MySQLdb.connect(host="localhost",port = 3306, user="root", passwd="admin",db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        print('try: ')
        cursor.execute("select fame_amt from marketing_department")
        row = cursor.fetchone()
        fame = row[0]
        cursor.execute("select level from engineering_department")
        row = cursor.fetchone()
        level = row[0]
        cursor.close()
        conn.commit()
    except:
        print('except: ')
        conn.rollback()
    conn.close()

    toBeHired(fame, level)

# main
#start
while True:
    choice = int(input("1. Continue Company\n2. Delete and Start a New Company\n"))
    if choice > 0 and choice < 3:
        break;
    else:
        choice = int(input("\nInvalid Choice!\n1. Continue Company\n2. Delete and Start a New Company\n"))


if choice == 2:
    #main menu
    removeProject() #debug nuke database
    startNewProject()
    
    
while True:
    clearConsole()
    choice = int(input("1. Hire Employee\n2. Fire Employee\n3.Raise Salary\n4.Decrease Salary\n5.View Report\n6. View Employees\n7. View Project\n8. Exit\n"))
    
    while True:
        if choice > 0 and choice < 9:
            break
        else:
            choice = int(input("\nInvalid Choice!\n1. Hire Employee\n2. Fire Employee\n3.Raise Salary\n4.Decrease Salary\n5.View Report\n6. View Employees\n7. View Project\n8. Exit\n"))
        

    if choice == 1:
        generate_to_be_hired()
















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

# update & delete
# cursor.execute("delete from products where id <> ?", 'pyodbc')
# print(cursor.rowcount, 'products deleted')
# cnxn.commit()

