from dbConnection import connection
myaccess = connection.cursor()

#creating table 
sql = 'create table if not exists employees_status(emp_id int not null, status varchar(20) not null, FOREIGN KEY (emp_id) REFERENCES employees(emp_id))'
myaccess.execute(sql)


# add status
# sql = 'insert into employees_status(emp_id, status) values(%s, %s)'
# val = (1115, 'active')
# myaccess.execute(sql, val)
# connection.commit()


# show all employees status
myaccess.execute('select * from employees_status')
result = myaccess.fetchall()
for i in result:
    print(i)


# update status
# myaccess.execute('update employees_status set status = inactive where emp_id = 1115')
# connection.commit()


# delete data
# myaccess.execute('delete from employees_status where emp_id = 1115')
# connection.commit()