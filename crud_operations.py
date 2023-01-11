import mysql.connector as msc
con = msc.connect(host = 'localhost',user = 'abc', password = 'password')
cur = con.cursor()
cur.execute('CREATE DATABASE employee')#creation of database
#creation of table
cur.execute("CREATE TABLE employee.empdetail(emp_id INT(2) PRIMARY KEY,emp_name VARCHAR(30) NOT NULL,age INT(2) NOT NULL,city VARCHAR(30) NOT NULL DEFAULT 'chennai',Phone_no BIGINT(10) NOT NULL)")
#describe command
cur.execute("desc employee.empdetail")
for i in cur:
     print(i)
#insert command
cur.execute("INSERT INTO employee.empdetail(emp_id,emp_name,age,city,phone_no) VALUES(1,'chakri',23,'kakinada',9666338739),(2,'krish',25,'viag',1234567890)")
con.commit()
#select command
cur.execute("SELECT * FROM employee.empdetail")
cur.execute("SELECT * FROM employee.empdetail WHERE BINARY emp_name='krish'")#making case senstive
#Update command
cur.execute("UPDATE employee.empdetail SET emp_name='vishnu' WHERE emp_name='chakri'")
con.commit()
#updating location of krish to chennai
cur.execute("UPDATE employee.empdetail SET city='chennai' where emp_name='krish'")
con.commit()
#increase age by 5 years for all
cur.execute("UPDATE employee.empdetail SET age=age+5")
con.commit()
cur.execute("SELECT * FROM employee.empdetail")
#Delete command
cur.execute("DELETE FROM employee.empdetail WHERE emp_id=2")
con.commit()
cur.execute("SELECT * FROM employee.empdetail")
for i  in cur:
     print(i)
# Adding column using alter command
cur.execute("ALTER TABLE employee.empdetail ADD COLUMN emp_role VARCHAR(30)")
#dropping column using alter
cur.execute("ALTER TABLE employee.empdetail DROP COLUMN emp_rol")
cur.execute("desc employee.empdetail")
for i  in cur:
     print(i)
#modify existing column in table using ALTER commad
cur.execute("ALTER TABLE employee.empdetail MODIFY COLUMN emp_name VARCHAR(40)")
#truncate commad
cur.execute("TRUNCATE TABLE employee.empdetail")