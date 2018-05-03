import MySQLdb
import os
from random import randint
import sys


# used to clear console in windows environment
def clearConsole():
    clearing = lambda: os.system('cls')
    clearing()


def removeProject():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("DROP DATABASE 138Company")
        conn.commit()
    except:
        conn.rollback()
    conn.close()


def startNewProject():
    fname = input('What is your first name: ')
    lname = input('What is your last name: ')
    # fname = 'Bob'
    # lname = 'Ross'
    userid = 777
    salary = 0
    motivation = 0
    exp = 0
    intel = 0

    # check if database exists
    # note to developers, please change the first conn to a database that exists
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin")
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

    # change connection to the new database, create tables if not exist
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS employee (e_id INTEGER NOT NULL, salary INTEGER NOT NULL, motivation INTEGER NOT NULL, experience INTEGER NOT NULL, f_name char(20) NOT NULL, l_name char(20) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS user (e_id INTEGER NOT NULL, department char(20) NOT NULL)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS to_be_hired (e_id INTEGER NOT NULL, salary INTEGER NOT NULL, motivation INTEGER NOT NULL, experience INTEGER NOT NULL, f_name char(20) NOT NULL, l_name char(20) NOT NULL , expire_time INTEGER NOT NULL)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS projects (p_id INTEGER NOT NULL, potential_profit INTEGER NOT NULL, deadline INTEGER NOT NULL, sucess_rate INTEGER NOT NULL, cost INTEGER NOT NULL, difficulty INTEGER NOT NULL, availability BOOLEAN NOT NULL, complete BOOLEAN NOT NULL, p_name VARCHAR(100), success BOOLEAN)")
        cursor.execute("CREATE TABLE IF NOT EXISTS e_p (e_id INTEGER NOT NULL, p_id INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS works_in (e_id INTEGER NOT NULL, department char(20) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS report (r_id INTEGER NOT NULL, misfortune_id INTEGER NOT NULL)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS engineering_department (name char(20) NOT NULL, level INTEGER NOT NULL, budget INTEGER NOT NULL)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS marketing_department (name char(20) NOT NULL, fame_amt INTEGER NOT NULL, fame_to_next_level INTEGER NOT NULL)")
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    clearConsole()

    # alter table constraints
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE employee ADD CONSTRAINT PK_employee PRIMARY KEY (e_id)")
        cursor.execute(
            "ALTER TABLE user ADD CONSTRAINT FK_user  FOREIGN KEY (e_id) REFERENCES employee(e_id) ON DELETE CASCADE")
        cursor.execute("ALTER TABLE to_be_hired ADD CONSTRAINT PK_to_be_hired PRIMARY KEY (e_id)")
        cursor.execute("ALTER TABLE projects ADD CONSTRAINT PK_projects PRIMARY KEY (p_id)")
        cursor.execute("ALTER TABLE report ADD CONSTRAINT PK_report PRIMARY KEY (r_id)")
        cursor.execute("ALTER TABLE engineering_department ADD CONSTRAINT PK_engineering_department PRIMARY KEY (name)")
        cursor.execute("ALTER TABLE marketing_department ADD CONSTRAINT PK_marketing_department PRIMARY KEY (name)")
        cursor.execute(
            "ALTER TABLE e_p ADD CONSTRAINT FK_e_p FOREIGN KEY (e_id) REFERENCES employee(e_id) ON DELETE CASCADE")
        cursor.execute(
            "ALTER TABLE works_in ADD CONSTRAINT FK_works_in FOREIGN KEY (e_id) REFERENCES employee(e_id) ON DELETE CASCADE")
        cursor.close()
        conn.commit()
    except:
        conn.rollback()

    # insert default values into table
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT IGNORE INTO engineering_department values('engineering', 1, 1000)")
        cursor.execute("INSERT IGNORE INTO marketing_department values('marketing', 1, 15)")
        cursor.execute("INSERT IGNORE INTO employee values(%s, %s, %s, %s, %s, %s)",
                       (userid, salary, motivation, exp, fname, lname))
        cursor.execute("INSERT ignore INTO user values(%s, %s)", (userid, 'engineering'))
        cursor.execute("INSERT ignore INTO works_in values(%s, %s)", (userid, 'engineering'))
        cursor.execute("INSERT INTO to_be_hired values(%s, %s, %s, %s, %s, %s, %s)",
                       (111, 0, 100, 0, 'j', 'k', 0))  # placeholders
        cursor.execute("INSERT INTO to_be_hired values (%s, %s, %s, %s, %s, %s, %s)", (222, 0, 100, 0, 'l', 'm', 0))
        cursor.execute("INSERT INTO to_be_hired values (%s, %s, %s, %s, %s, %s, %s)", (333, 0, 100, 0, 'n', 'o', 0))
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    generate_to_be_hired()


def updateTBH(e_idx, fnamex, lnamex, experiencex, salaryx, motivationx, exp_timex, idx):
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE to_be_hired SET e_id = %s, salary = %s, motivation = %s, experience = %s,  f_name = %s, l_name = %s ,expire_time = %s where e_id = %s",
            (e_idx, salaryx, motivationx, experiencex, fnamex, lnamex, exp_timex, idx))
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()


def generate_to_be_hired():  # need to add the base case where gotta add in new company
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        # read fame and level
        cursor.execute("select fame_amt from marketing_department")
        row = cursor.fetchone()
        fame = row[0]
        cursor.execute("select level from engineering_department")
        row = cursor.fetchone()
        level = row[0]

        # save values of expire time
        cursor.execute("select * from to_be_hired")
        row = cursor.fetchone()
        id1 = row[0]
        exp1 = int(row[1])
        row = cursor.fetchone()
        id2 = row[0]
        exp2 = int(row[1])
        row = cursor.fetchone()
        id3 = row[0]
        exp3 = int(row[1])
        cursor.close()
        conn.commit()
    except:
        conn.rollback()

    if exp1 == 0:
        e_id1 = randint(10000, 100000)
        fname1 = 'employee ' + str(e_id1)
        lname1 = 'smith'
        experience1 = level + (fame * randint(0, 2))
        salary1 = 20 + (experience1 * randint(0, 2))
        motivation1 = 100
        exp_time1 = randint(1, 3)
        updateTBH(e_id1, fname1, lname1, experience1, salary1, motivation1, exp_time1, id1)

    if exp2 == 0:
        e_id2 = randint(10000, 100000)
        fname2 = 'employee ' + str(e_id2)
        lname2 = 'smith'
        experience2 = level + (fame * randint(0, 2))
        salary2 = 20 + (experience2 * randint(0, 2))
        motivation2 = 100
        exp_time2 = randint(1, 3)
        updateTBH(e_id2, fname2, lname2, experience2, salary2, motivation2, exp_time2, id2)

    if exp3 == 0:
        e_id3 = randint(10000, 100000)
        fname3 = 'employee ' + str(e_id3)
        lname3 = 'smith'
        experience3 = level + (fame * randint(0, 2))
        salary3 = 20 + (experience3 * randint(0, 2))
        motivation3 = 100
        exp_time3 = randint(1, 3)
        updateTBH(e_id3, fname3, lname3, experience3, salary3, motivation3, exp_time3, id3)

    conn.close()

    # hire employees


def hireEmployee():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        print('Fname, Lname, Salary, Time before Offer is gone')
        cursor.execute("select * from to_be_hired")
        res = cursor.fetchall()
        i = 0;
        for row in res:
            i = i + 1
            if row[6] != 0:
                print("%d   f:%s, l:%s, %s $, %s" % (i, row[4], row[5], row[1], row[6]))
        cursor.close()
        conn.commit()
    except:
        print('-1')
        conn.rollback()

    # save values of expire time
    # cursor.execute("select * from to_be_hired")
    cursor = conn.cursor()
    try:
        cursor.execute("select * from to_be_hired")
        res = cursor.fetchall()
        cursor.close()
        conn.commit()
    except:
        print('-2')
        conn.rollback()
    while True:
        choice = int(input("1. Hire employee 1\n2. Hire employee 2\n3. Hire employee 3\n4. Exit\n"))
        if choice > 0 and choice < 5:
            break;
        else:
            choice = int(
                input("\nInvalid Choice!\n1. Hire employee 1\n2. Hire employee 2\n3. Hire employee 3\n4. Exit\n"))

        if choice == 1:  # not finished
            cursor.execute("INSERT IGNORE INTO employee values(%s, %s, %s, %s, %s, %s)",
                           (userid, salary, motivation, exp, fname, lname))
        if choice == 2:
            cursor.execute("INSERT IGNORE INTO employee values(%s, %s, %s, %s, %s, %s)",
                           (userid, salary, motivation, exp, fname, lname))
        if choice == 3:
            cursor.execute("INSERT IGNORE INTO employee values(%s, %s, %s, %s, %s, %s)",
                           (userid, salary, motivation, exp, fname, lname))
        conn.close()

    # Delete specific employee from the database using the employeeID


def fireEmployee(employeeID):
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")

    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT salary FROM employee where %s = employeeID", (employeeID))
        cost = cursor.fetchone()
        # increase the budget from whatever pay that the employee has
        cursor.execute("UPDATE engineering_department SET budget = budget + cost")
        cursor.execute("SELECT fname, lname FROM employee WHERE %s = e_ID", (employeeID))
        row = cursor.fetchone()
        print(row.fname + ' ' + row.lname + ' has been fired due to their incompetence')
        cursor.execute("DELETE FROM employee WHERE e_id = employeeID")
    except:
        conn.rollback()
    conn.close()


# Sweeps all and delete any employees that has less than 10 motivation
def employeeQuit():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")

    conn.autocommit = False
    cursor = conn.cursor()
    try:
        # selects all employees with motivation less than 10
        cursor.execute("SELECT fname, lname FROM employee WHERE motivation < 10")
        row = cursor.fetchall()
        # prints out the list of employees that left
        print('The following employees have left the company due to lack of motivation:')
        for x in range(0, len(row)):
            print
            row[x],
            if x % 2 == 1:
                print

        # executes the delete command to the database
        cursor.execute("DELETE FROM employee WHERE motivation < 10")
    except:
        conn.rollback()
    conn.close()


# Delete a specific employee if their motivation is less than 10
def employeeQuit(employeeID):
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")

    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT salary FROM employee WHERE %s = e_id AND motivation < 10", (employeeID))
        cost = cursor.fetchone()
        # increase the budget from whatever pay that the employee has
        cursor.execute("UPDATE engineering_department SET budget = budget + cost")
        cursor.execute("SELECT fname, lname FROM employee WHERE %s = e_ID AND motivation < 10", (employeeID))
        row = cursor.fetchone()
        print(row.fname + ' ' + row.lname + ' has sent the letter of resignation due to the lack of motivation.')
        cursor.execute("DELETE FROM employee WHERE employeeID = e_id AND motivation < 10")
    except:
        conn.rollback()
    conn.close()


# Generates ONE single new project *******UNFINISHED*******
def generateProjects():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")

    conn.autocommit = False
    cursor = conn.cursor()
    try:
        # clears out any expired projects
        sweepRemoveProjects()
        # counts the amount of available projects that are left
        cursor.execute("SELECT COUNT(p_id) FROM projects WHERE availability = 1")
        size = cursor.fetchone()
        # generate up to 5 different projects
        for x in range(size, 5):
            print(1)
            # generate projects ***********
    except:
        conn.rollback()
    conn.close()


# Removes any expired projects
def sweepRemoveProjects():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")

    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM projects WHERE deadline <= 0 AND availability = 1")
    except:
        conn.rollback()
    conn.close()


def removeSelectedProjects(projectID):
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="138Company")

    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE FROM projects SET availability = NOT availability WHERE %s = p_id", (projectID))
    except:
        conn.rollback()
    conn.close()


def RaiseSalaryStart():  # Not Done
    while True:
        choice = (input("Type Employee ID:\n"))
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
        conn.autocommit = False
        cursor = conn.cursor()
        try:
            cursor.execute(f'UPDATE employee SET salary = salary+5 WHERE e_id = {choice}')
            cursor.execute(f'UPDATE employee SET motivation = motivation+5 WHERE e_id = {choice}')
            conn.commit()
            conn.close()
        except:
            conn.rollback()
        break




def decreaseSalary():  # Decreases the salary of an employee by a set amount. Decreases motivation as well.
    while True:
        choice = (input("Type Employee ID:\n"))
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
        conn.autocommit = False
        cursor = conn.cursor()
        try:
            cursor.execute(f'UPDATE employee SET salary = salary-5 WHERE e_id = {choice}')
            cursor.execute(f'UPDATE employee SET motivation = motivation-5 WHERE e_id = {choice}')
            conn.commit()
            conn.close()
        except:
            conn.rollback()
        break

def generateReport():
    while True:
        projectID = (input("Type Project ID:\n"))
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
        conn.autocommit = False
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT * FROM projects WHERE p_id = %s' % projectID)
            res = cursor.fetchall()
            i = 0;
            for row in res:
                i = i + 1
                if (row[7] != 1):
                    print('IN PROGRESS:\nReport for %d AKA %s is as follows:\n This project has a difficulty of: %d \n It has a cost of: $ %d. \n Therefore, it has a potential profit of: $ %d \n The deadline for the project is: %d \n '  % (row[0],row[8],row[5],row[4],row[1],row[2]))
                elif (row[9] != 1):
                    print('COMPLETE:\n %s AKA %s is complete.\n The project has been a success. \n We have earned $ %s.\n Good work! \n' %(row[0],row[8],row[1]))
                else:
                    print('%d AKA %s is complete:\n The project has been a failure! \n Misfortune has occured! \n ' % (row[0],row[8]))
            cursor.close()
            conn.commit()
        except:
            conn.rollback()
        xd = (input("Enter to exit:\n"))
        conn.close()
        break

def raiseEXP(employeeID):  # Decreases the salary of an employee by a set amount. Decreases motivation as well.
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE employee SET experience = (experience+1) WHERE e_id = %s', (employeeID))
        conn.commit()
    except:
        conn.rollback()
    conn.close()


# view list of employees
def viewEmployee():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()
    try:
        print('Select an Employee')
        cursor.execute("select * from employee")
        res = cursor.fetchall()
        i = 0
        for row in res:
            i = i + 1
            print("%d ID:%s  Name:%s %s, Salary:%s $, Motivation:%s" % (i, row[0], row[4], row[5], row[1], row[2]))
        cursor.close()
        conn.commit()
    except:
        print('-1')
        conn.rollback()
    while True:
        choice = (input("Type to Exit\n"))
        break
    conn.close()


def viewProject():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        print('Projects:')
        cursor.execute("select * from projects")
        res = cursor.fetchall()
        i = 0;
        for row in res:
            i = i + 1
            if row[6] != 0:
                print("%d   Potential Profit:%s, Deadline: %s , Sucess Rate:%s , Cost: %s" % (
                i, row[2], row[3], row[4], row[5]))
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    while True:
        choice = input("Enter to return to main menu.")
        conn.close()
        break


def viewReport():
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="admin", db="138Company")
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        print('Projects:')
        cursor.execute("select * from projects")
        res = cursor.fetchall()
        i = 0;
        for row in res:
            i = i + 1
            if row[6] != 0:
                print("%d   Potential Profit:%s, Deadline: %s , Sucess Rate:%s , Cost: %s" % (
                i, row[2], row[3], row[4], row[5]))
        cursor.close()
        conn.commit()
    except:
        conn.rollback()
    while True:
        choice = input("Enter to return to main menu.")
        conn.close()
        break


# main
# start
while True:
    choice = int(input("1. Continue Company\n2. Delete and Start a New Company\n"))
    if choice > 0 and choice < 3:
        break;
    else:
        choice = int(input("\nInvalid Choice!\n1. Continue Company\n2. Delete and Start a New Company\n"))

if choice == 2:
    # main menu
    removeProject()
    startNewProject()

while True:
    clearConsole()
    choice = int(input(
        "1. Hire Employee\n2. Fire Employee\n3.Raise Salary\n4.Decrease Salary\n5.Assign Projects\n6.View Report\n7. View Employees\n8. View Project\n9. Exit\n"))

    while True:
        if choice > 0 and choice < 9:
            break
        else:
            choice = int(input(
                "1. Hire Employee\n2. Fire Employee\n3.Raise Salary\n4.Decrease Salary\n5.Assign Projects\n6.View Report\n7. View Employees\n8. View Project\n9. Exit\n"))

    if choice == 1:
        hireEmployee()
    elif choice == 2:
        clearConsole()
        viewEmployee()
        employeeID = input('Enter the employee ID you wish to fire: ')
        fireEmployee(employeeID)
    elif choice == 3:
        RaiseSalaryStart()
    elif choice == 4:
        decreaseSalary()
    # elif choice == 5:
    # assign project
    elif choice == 6:
        generateReport()
    elif choice == 7:
        viewEmployee()
    elif choice == 8:
        viewProject()
    elif choice == 9:
        sys.exit(0)

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
