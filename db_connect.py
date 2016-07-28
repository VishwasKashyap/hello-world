import mysql.connector 
import 
cnx = mysql.connector.connect(user='root',password='root',host="localhost",database='dummy')

name = document.getElementbyID("name")
age = document.getElementbyID("age")
print name
print age
cur = cnx.cursor()
cur.execute("select * from test")
for row in cur.fetchall():
	print "Name: " + row[0] +" " "Age: "+str(row[1])
cnx.close()
