import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mysql@12345',
    auth_plugin = 'mysql_native_password',
    database = 'payroll_system'
)

myaccess = connection.cursor()

myaccess.execute('create database if not exists payroll_system')

# show all tables
# myaccess.execute('show tables')
# allTables = myaccess.fetchall()
# for table in allTables:
#     print(table)
