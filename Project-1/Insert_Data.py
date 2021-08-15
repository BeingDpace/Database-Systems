# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:12:41 2021

@author: AvengersEndGame
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306,
  database="companydb",
)
'''
Pname = input("Please enter the name of project to add: ")
Pnumber = int(input("Please enter the project number to add: "))
Plocation = input("Please enter the project location  to add: ")
Dnum = int(input("Please enter the department number to add: "))
mycursor = mydb.cursor()
mycursor.execute("""INSERT INTO project(Pname, Pnumber, Plocation, Dnum) VALUES (%s, %s, %s, %s)""",(Pname, Pnumber, Plocation, Dnum,))
mydb.commit()
print("\nDATA ADDED SUCCESFULLY TO PROJECT TABLE")
'''
mycursor = mydb.cursor()
print("\nSHOWING UPDATED TABLE")
mycursor.execute(" SELECT * FROM project")
for data in mycursor:
    print(data)
