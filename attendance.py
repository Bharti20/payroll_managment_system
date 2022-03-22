from dbConnection import connection
myaccess = connection.cursor()

sql = 'create table if not exists attendance (person_id int unique key not null, present_days_in_month int not null, FOREIGN KEY (person_id) REFERENCES employees(emp_id))'
myaccess.execute(sql)

# insert data 
# sql = 'insert into attendance(person_id, present_days_in_month) values(%s, %s)'
# val = (1115, 30)
# myaccess.execute(sql, val) 
# connection.commit()


# Show all employees attendance
sql = 'select * from attendance'
myaccess.execute(sql)
result = myaccess.fetchall()
for i in result:
    print(i)


# update attendence 
# myaccess.execute('update attendance set present_days_in_month = 20 where person_id = 1111')
# connection.commit()


# Delete data
# myaccess.execute('delete from attendance where person_id = 1115')
# connection.commit()