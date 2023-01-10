import mysql.connector
con = mysql.connector.connect(host="localhost",user="abc",password="password")
print(con.is_connected())
cur = con.cursor()
cur.execute("CREATE DATABASE praactice")
for i in cur:
     print(i)