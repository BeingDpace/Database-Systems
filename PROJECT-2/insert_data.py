# -*- coding: utf-8 -*-
"""
@author: Deepesh Bhatta
"""
from tabulate import tabulate
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306,
  database="security_db",
)
conn = mydb.cursor(buffered=True)
conn.execute("SELECT * FROM USER_ACCOUNTS;")
account_data = conn.fetchall()
#print(len(account_data))
#print(account_data)
if len(account_data) == 0:
    account_data = [(1, "John Doe", "john@utab.com"), 
            (2, "Johny Doe", "johny@utab.com"),
            (3, "Noob Doe", "noob@utab.com"),
            (4, "Noob Noob", "noobnoob@utab.com"),
            (5, "Rick Sanchez", "rick@utab.com"),
            (6, "Morty Smith", "morty@utab.com"),
            (7, "Summer Smith", "summer@utab.com"),
            (8, "Berry Smith", "berry@utab.com"),
            (9, "Rick Decoy", "rickdecoy@utab.com"),
            (10, "Morty Decoy", "mortydecoy@utab.com")]
    query = 'INSERT INTO USER_ACCOUNTS(IdNO, UserName, Email) VALUES (%s, %s, %s);'
    conn.executemany(query, account_data)
    mydb.commit()
print("\nUSER ACCOUNT:")
print("-----------------------------------------")
print(tabulate(account_data, headers=["IdNo", "Name", "Email"]))
        
conn.execute("SELECT * FROM USER_ROLES;")
role_data = conn.fetchall()
#print(len(role_data))
#print(role_data)
if len(role_data) == 0:
    role_data = [(1, "Manager", "Manages all users"), 
            (2, "User", "Regular User"),
            (3, "HR", "Human Resources")]
    query = 'INSERT INTO USER_ROLES(IdNo, RoleName, RoleDescription) VALUES (%s, %s, %s);'
    conn.executemany(query, role_data)
    mydb.commit()
print("\nUSER ROLE:")
print("--------------------------------------------")
print(tabulate(role_data, headers=["IdNo", "RoleName", "RoleDescription"]))

conn.execute("SELECT * FROM USER_TABLES;")
table_data = conn.fetchall()
#print(len(table_data))
#print(table_data)
if len(table_data) == 0:
    table_data = [("Table-1", 1), 
            ("Table-2", 2),
            ("Table-3", 3),
            ("Table-4", 4),
            ("Table-5", 6)]
    query = 'INSERT INTO USER_TABLES(TableName, AccountIdNo) VALUES (%s, %s);'
    conn.executemany(query, table_data)
    mydb.commit()
print("\nUSER TABLE:")
print("--------------------------")
print(tabulate(table_data, headers=["TableName", "AccountIdNo"]))

conn.execute("SELECT * FROM USER_PRIVILEGES;")
privilege_data = conn.fetchall()
#print(len(privilege_data))
#print(privilege_data)
if len(privilege_data) == 0:
    privilege_data = [(100, "SELECT"), 
            (101, "INSERT"),
            (102, "DELETE"),
            (103, "UPDATE"),
            (104, "CREATETAB")]
    query = 'INSERT INTO USER_PRIVILEGES(IdNo, PrivType) VALUES (%s, %s);'
    conn.executemany(query, privilege_data)
    mydb.commit()
print("\nUSER PRIVILEGES:")
print("-----------------------")
print(tabulate(privilege_data, headers=["IdNo", "PrivilegeType"]))

conn.execute("SELECT * FROM ACCOUNT_PRIVILEGES;")
ap_data = conn.fetchall()
#print(len(ap_data))
#print(ap_data)
if len(ap_data) == 0:
    ap_data = [(100, "HR"), 
            (101, "HR"),
            (102, "Manager"),
            (103, "Manager"),
            (100, "Manager"),
            (104, "User")]
    query = 'INSERT INTO ACCOUNT_PRIVILEGES(IdNo, Rname) VALUES (%s, %s);'
    conn.executemany(query, ap_data)
    mydb.commit()
    
print("\nACCOUNT PRIVILEGES:")
print("---------------------------")
print(tabulate(ap_data, headers=["PrivilegeIdNo", "RoleName"]))

conn.execute("SELECT * FROM RELATION_PRIVILEGES;")
rp_data = conn.fetchall()
#print(len(rp_data))
#print(rp_data)
if len(rp_data) == 0:
    rp_data = [(100, "Table-1", "User"), 
            (101, "Table-1", "User")]
    query = 'INSERT INTO RELATION_PRIVILEGES(IdNo, Tname, Rname) VALUES (%s, %s, %s);'
    conn.executemany(query, rp_data)
    mydb.commit()
print("\nRELATION PRIVILEGES:")
print("----------------------------------------")
print(tabulate(rp_data, headers=["PrivilegeIdNo","TableName", "RoleName"]))
conn.close()
mydb.close()



