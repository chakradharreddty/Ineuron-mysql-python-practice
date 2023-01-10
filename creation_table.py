import mysql.connector
con = mysql.connector.connect(host="localhost",user="abc",password="password")
print(con.is_connected())
cur = con.cursor()
cur.execute('use praactice ')
cur.execute("CREATE TABLE praactice.ext(name VARCHAR(20),Phn VARCHAR(10),city VARCHAR(30))")
# desc command
cur.execute("desc ext")
for i in  cur:
    print(i)
cur.execute("""INSERT INTO praactice.ext VALUES('Chakri','123456','kakinada'),('VIAJA','456789','vizag'),('sudhanshu','67890','kakinada'),
('indhu','67890','chennai')""")
con.commit()
cur.execute("SELECT * FROM praactice.ext")
for i in cur:
     print(i)
