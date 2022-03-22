from dbConnection import connection
myaccess = connection.cursor()
myaccess.execute( 'create table if not exists departments(dept_id int primary key, name varchar(30))')

# Insert data
# sql = 'insert into departments (dept_id, name) values(%s, %s)'
# val = [(1, 'HR'), (2, 'Training'), (3, 'Finance'), (4, 'Sales'), (5, 'Development')]
# myaccess.execute(sql, val)
# connection.commit()


# show all departments
myaccess.execute('select * from departments')
allDept = myaccess.fetchall()
for i in allDept:
    print(i)




# Update department
# sql = 'update departments set name = "testing" where dept_id = 5 '
# myaccess.execute(sql)
# connection.commit()



# delete department 
# sql = 'delete from departments where dept_id = 5 '
# myaccess.execute(sql)
# connection.commit()



