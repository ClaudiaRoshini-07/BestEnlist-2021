//1.	Create a JSON of all object types and import the JSON into a SQL Database

import json

x=[
     {'First_name':"Tina",Last_name':"Mary",'age':20,'Student':True,'Percentage':75.30,'Group':'Biology'},
     {'First_name':"John",Last_name':"Raj",'age':20,'Student':True,'Percentage':96.85,'Group':"ComputerScience"},
     {'First_name':"Rohit",Last_name':"Kumar",'age':20,'Student':True,'Percentage':85.00,'Group':'Biology'},
     {'First_name':"Akshay",Last_name':"Kumar",'age':20,'Student':True,'Percentage':92.50,'Group':'Biology'},
     {'First_name':"Karthick",Last_name':"Vel",'age':20,'Student':True,'Percentage':69.00,'Group':'ComputerScience'}
     {'First_name':"Henry",Last_name':"Chris",'age':20,'Student':True,'Percentage':75.90,'Group':'Biology'}
]


rs =json.dumps(x)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0712"
)

print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE JSONFIL")
dbse = mydb.cursor()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0712",
  database="jsonfil"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE stud (First_name VARCHAR(255),Last_name VARCHAR(255),age INT, Student VARCHAR(255), Percentage DOUBLE, Group VARCHAR(255))")

dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for i in dbse:
  print(i)

dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM stud")

for i in dbse:
  print(i)
