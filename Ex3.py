import mysql.connector
con = mysql.connector.connect(host='localhost',user='abc',password='password')
cur = con.cursor()
# cur.execute("CREATE DATABASE employee")
cur.execute("USE employee")
# cur.execute("CREATE TABLE employeedet(emp_id INT(2) AUTO_INCREMENT,emp_name VARCHAR(30),city VARCHAR(20),age INT(2),PRIMARY KEY(emp_id))")
# cur.execute("INSERT INTO employeedet(emp_name,city,age) VALUES('chakri','kakinada',23),('krish','chennai',21)")
# con.commit()
cur.execute("SELECT * FROM employeedet")
for i in cur:
    print(i)
