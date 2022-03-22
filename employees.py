from dbConnection import connection

myaccess = connection.cursor()

# creating table
myaccess.execute('create table if not exists employees (emp_id int primary key, emp_name varchar(40) not null, dept_no int, Gender varchar(15), joining_date date not null, DOB date, phone varchar(12) not null, father_or_spouse varchar(30), address varchar(100))')


# insert employee data
# sql = 'insert into employees (emp_id, emp_name, dept_no, Gender,joining_date, DOB, phone, father_or_spouse,address)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# val = (1115, 'Sheetal', 5, 'Female','2022-2-20','1998-8-14','3456767891','Lal singh','Utrakhand')
# myaccess.execute(sql, val)
# connection.commit()


# show all data employees data 
myaccess.execute('select * from employees')
allData = myaccess.fetchall()
for i in allData:
    print(i)


#update employee data
# sql = 'update employees set phone = "8965342101" where emp_id = 1' 
# myaccess.execute(sql)
# connection.commit()


# delete employee data
# sql = 'delete from employees where emp_id = 5'
# myaccess.execute(sql)
# connection.commit()

