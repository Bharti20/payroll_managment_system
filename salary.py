from dbConnection import connection
myaccess = connection.cursor()

# sql = 'create table if not exists salaries (empId int not null, basic_salary float, permotion float ,FOREIGN KEY (empId) REFERENCES employees(emp_id) )'
# myaccess.execute(sql)


# insert data 
# sql = 'insert into salaries(empId, basic_salary) values (%s, %s)'
# val =  (1115, 25000 )
# myaccess.execute(sql, val)
# connection.commit()


# show all employees salary
myaccess.execute('select * from salaries')
allD = myaccess.fetchall()
for i in allD:
    print(i)


# update employees salary
# sql = 'update salaries set permotion = 30000 where empId = 1115'
# myaccess.execute(sql)
# connection.commit()


# delete data
# sql = 'delete from salaries where empId = 1115'
# myaccess.execute(sql)
# connection.commit()




