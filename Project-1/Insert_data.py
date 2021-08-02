from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
import mysql.connector

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="?",
  port=3306,
  database="companydb",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# View All Database
for x in mycursor:
  print(x)

# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    cursor = mydb.cursor()
    return render_template('index.html')

@app.route('/search' ,methods=['POST'])
def search() :
    cursor = mydb.cursor()
    Fname = request.form.get('Fname')
    Lname = request.form.get('Lname')
    name = Fname +" "+ Lname
    print(name)
    cursor.execute('SELECT Pname, Hours From (EMPLOYEE JOIN WORKS_ON ON Essn = Ssn JOIN PROJECT ON Pno = Pnumber) WHERE Fname = %s AND Lname = %s', (Fname,Lname,))
    results = cursor.fetchall()
    return render_template('index.html', results=results, name=name)

@app.route('/findsum', methods=['POST'])
def findsum() :
    cursor = mydb.cursor()
    Dname = request.form.get('Dname')
    print(Dname)
    cursor.execute('SELECT SUM(EMPLOYEE.Salary) AS TOTAL_SUM_OF_SALARY FROM (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber) WHERE Dname = %s', (Dname,))
    sum1 = cursor.fetchall()
    sum = []
    for row in sum1:
        sum.append(float(row[0]))
    return render_template('index.html', sum=sum, Dname=Dname)


if (__name__ == "__main__"):
     app.run(port = 5000)
