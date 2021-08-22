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
conn = mydb.cursor()

NEW_USER_ACCCOUNT = 1
NEW_ROLE = 2
NEW_TABLE = 3
NEW_PRIVILIGE= 4
RELATE_UA_TO_ROLE = 5
RELATE_AP_TO_ROLE = 6
RELATE_RP_TO_ROLE = 7
RETRIEVE_PRIVILIGES = 8
EXIT = 9
def main():
    choice = None
    try:
        while choice != 9:
            display_menu()
            choice = int(input('Enter your choice [1-9]: '))
            if choice == 1:
                add_account()
            elif choice == 2:
                add_role()
            elif choice == 3:
                add_table()
            elif choice == 4:
                add_privilige()
            if choice == 5:
                relate_ua_role()
            elif choice == 6:
                relate_ap_role()
            elif choice == 7:
                relate_rp_role_table()
            elif choice == 8:
                retrieve_privileges()
            elif choice == 9:
                conn.close()
                print('Exiting the program...')
                mydb.close()
            else:
                print("***")
    except :
        print("Error: Wrong Input DataType - Try again with integer value [1 to 9]!!! \n")
        main()
    
def display_menu():
    print("--------------------------------------------------------")
    print('MAIN MENU')
    print("--------------------------------------------------------")
    print('1 - ADD A NEW USER ACCOUNT')
    print('2 - ADD A NEW ROLE')
    print('3 - ADD A NEW TABLE')
    print('4 - INSERT A NEW PRIVILIGE')
    print('5 - RELATE  A USER ACCOUNT TO A ROLE')
    print('6 - RELATE AN ACCOUNT PRIVILIGE TO A ROLE')
    print('7 - RELATE RELATION PRIVILIGE, ROLE, AND TABLE')
    print('8 - RETREIVE ALL PRIVILIGES AND CHECK PRIVILIGES')
    print('9 - EXIT A PROGRAM')

def add_account():    
    try:
        idno = int(input('IdNo: '))
        username = str(input('UserName: '))
        email = str(input("Email: "))
        data = (idno, username, email,)
        query = '''INSERT INTO USER_ACCOUNTS(IdNO, UserName, Email) VALUES (%s, %s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!!NEW USER ACCOUNT ADDED SUCCESFULLY!!!')
    except Exception as err:
        print(err)
        
def add_role():
    try:
        idno = int(input('IdNo: '))
        rolename = str(input('RoleName: '))
        description = str(input("RoleDescription: "))
        data = (idno, rolename, description,)
        query = '''INSERT INTO USER_ROLES(IdNo, RoleName, RoleDescription) VALUES (%s, %s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!!NEW USER ROLE ADDED SUCCESFULLY!!!')
    except Exception as err:
        print(err)    

def add_table():
    try:
        tablename = str(input('TableName: '))
        accountidno = int(input('AccountIdNo: '))
        data = (tablename, accountidno,)
        query = '''INSERT INTO USER_TABLES(TableName, AccountIdNo) VALUES (%s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!!NEW USER TABLE ADDED SUCCESFULLY!!!')
    except Exception as err:
        print(err) 
    
def add_privilige():
    try:
        idno = int(input('IdNo: '))
        privilege_type = str(input('PrivilegeType: '))
        data = (idno, privilege_type,)
        query = '''INSERT INTO USER_PRIVILEGES(IdNo, PrivType) VALUES (%s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!!NEW PRIVILEGE ADDED SUCCESFULLY!!!')           
    except Exception as err:
        print(err)     

def relate_ua_role():    
    try:
        idno = int(input('IdNo: '))
        account_idno = int(input('AccountIdNo: '))
        role_idno = int(input('RoleIdNo: '))
        data = (idno, account_idno, role_idno,)
        query = '''INSERT INTO RELATE_ACCOUNT_TO_ROLE(IdNo, AccountIdNo, RoleidNo) VALUES (%s, %s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!! USER ACCOUNT AND ROLE RELATED SUCCESFULLY!!!')
    except Exception as err:
        print(err)
        
def relate_ap_role():
    try:
        idno = int(input('IdNo: '))
        rolename= str(input('RoleName: '))
        data = (idno, rolename,)
        query = '''INSERT INTO ACCOUNT_PRIVILEGES(IdNo, Rname) VALUES (%s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!!ACCOUNT PRIVILEGE AND ROLE RELATED SUCCESFULLY!!!')
    except Exception as err:
        print(err)    

def relate_rp_role_table():
    try:
        idno = int(input('PrivilegeIdNo: '))
        tablename= str(input('TableName: '))
        rolename= str(input('RoleName: '))
        data = (idno, tablename, rolename,)
        query = '''INSERT INTO RELATION_PRIVILEGES(IdNo, TName, Rname) VALUES (%s, %s, %s)'''
        conn.execute(query,data)
        mydb.commit()
        print('!!!REALTION PRIVILEGE, ROLE, AND TABLE RELATED SUCCESFULLY!!!')
    except Exception as err:
        print(err) 
    
def retrieve_privileges():
    choice = None
    '''
    privilege_of_role = 1
    privilege_of_account = 2
    check_privilege = 3
    back_to_main_menu = 4
    '''
    try:
        while choice != 4:
            retrieve_menu()
            choice = int(input('Enter your choice [1-4]: '))
            if choice == 1:
                show_role_priv()
            elif choice == 2:
                show_account_priv()
            elif choice == 3:
                check_priv()
            elif choice == 4:
                print('Exiting the mini-menu...')
            else:
                print("Choice Not Available - Try again with value 1 to 4!!!\n")
    except :
        print("Error: Wrong Input DataType - Try again with integer value [1 to 4]!!! \n")
        retrieve_privileges()     

def retrieve_menu():
    print("-----------------------------------------------------------------------")
    print('MINI-MENU')
    print("-----------------------------------------------------------------------")
    print('1 - RETRIEVE ALL PRIVILEGES ASSOCIATED WITH PARTICULAR ROLE')
    print('2 - RETRIEVE ALL PRIVILEGES ASSOCIATED WITH PARTICULAR USER ACCOUNT')
    print('3 - CHECK PRIVILEGES AVAILABLE FOR USER ACCOUNT')
    print('4 - EXIT MINI-MENU')
    
def show_role_priv():
    try:
        rolename = input("Role: ")
        data = (rolename,)
        query = '''SELECT DISTINCT(P.PrivType)  AS ACCOUNT_PRIVILEGE 
                   FROM ACCOUNT_PRIVILEGES AS AP, USER_PRIVILEGES AS P 
                   WHERE AP.IdNo = P.IdNo AND AP.Rname = %s'''
        conn.execute(query, data)
        data = conn.fetchall()
        if len(data) == 0:
            print(f" Account Privileges for {rolename} is not yet given")
        else:
            list = []
            for i in data:
                list.append(i[0])
            print(f"Account Privileges for {rolename} : {list}")
        
        data = (rolename,)
        query = '''SELECT DISTINCT(P.PrivType)  AS RELATION_PRIVILEGE 
                   FROM RELATION_PRIVILEGES AS RP, USER_PRIVILEGES AS P 
                   WHERE RP.IdNo = P.IdNo AND RP.Rname = %s'''
        conn.execute(query, data)
        data = conn.fetchall()
        if len(data) == 0:
            print(f"Relation Privileges for {rolename} is not yet given")
        else:
            list = []
            for i in data:
                list.append(i[0])
            print(f"Relation Privileges for {rolename} : {list}")
    except Exception as err:
        print(err)
        
def show_account_priv():
    try:
        idno = input("AccountIdNo: ")
        conn.execute('''SELECT * FROM USER_ACCOUNTS WHERE IdNo = %s''',(idno,))
        name = list(conn.fetchone())
        print("Name: ", name[1])
        data = (idno,)
        query = '''SELECT DISTINCT(P.PrivType)
                    FROM ACCOUNT_PRIVILEGES AS AP, USER_PRIVILEGES AS P,
                    USER_ACCOUNTS AS UA, USER_ROLES AS UR, RELATE_ACCOUNT_TO_ROLE AS R                  
                    WHERE UA.IdNo = %s AND UA.IdNo = R.AccountIdNo AND R.RoleIdNo = UR.IdNo
                    AND AP.Rname = UR.RoleName AND AP.IdNo = P.IdNo'''
        conn.execute(query, data)
        data = conn.fetchall()
        print("-------------------")
        print(tabulate(data, headers=["ACCOUNT_PRIVILEGE"]))
        
        data = (idno,)
        query = '''SELECT DISTINCT(P.PrivType)  AS RELATION_PRIVILEGE 
                   FROM RELATION_PRIVILEGES AS RP, USER_PRIVILEGES AS P,
                   USER_ACCOUNTS AS UA, USER_ROLES AS UR, RELATE_ACCOUNT_TO_ROLE AS R                  
                   WHERE UA.IdNo = %s AND UA.IdNo = R.AccountIdNo AND R.RoleIdNo = UR.IdNo
                   AND RP.Rname = UR.RoleName AND RP.IdNo = P.IdNo'''
        conn.execute(query, data)
        data = conn.fetchall()
        print("--------------------")
        print(tabulate(data, headers=["RELATION_PRIVILEGE"]))
    except Exception as err:
        print(err)
        
def check_priv():
    try:
        idno = input("Enter AccountIdNo: ")
        conn.execute('''SELECT * FROM USER_ACCOUNTS WHERE IdNo = %s''',(idno,))
        name = list(conn.fetchone())
        print("Name: ", name[1])
        priv = input("Enter the privilege you want to check: ")
        priv = priv.upper()
        data = (idno,idno,)
        query = '''SELECT DISTINCT(P.PrivType)
                    FROM ACCOUNT_PRIVILEGES AS AP, USER_PRIVILEGES AS P,
                    USER_ACCOUNTS AS UA, USER_ROLES AS UR, RELATE_ACCOUNT_TO_ROLE AS R                  
                    WHERE UA.IdNo = %s AND UA.IdNo = R.AccountIdNo AND R.RoleIdNo = UR.IdNo
                    AND AP.Rname = UR.RoleName AND AP.IdNo = P.IdNo
                    UNION 
                    SELECT DISTINCT(P.PrivType)  AS RELATION_PRIVILEGE 
                    FROM RELATION_PRIVILEGES AS RP, USER_PRIVILEGES AS P,
                    USER_ACCOUNTS AS UA, USER_ROLES AS UR, RELATE_ACCOUNT_TO_ROLE AS R                  
                    WHERE UA.IdNo = %s AND UA.IdNo = R.AccountIdNo AND R.RoleIdNo = UR.IdNo
                    AND RP.Rname = UR.RoleName AND RP.IdNo = P.IdNo'''
        conn.execute(query, data)
        data = conn.fetchall()
        print("----------------------------------------------")
        #print(tabulate(data, headers=["PRIVILEGE"]))
        privilege_list = []
        for i in data:
            privilege_list.append(i[0])
        if priv in privilege_list:
            print(f"{priv} is granted to above account")
        else:
            print(f"{priv} is not granted to above account")
        #print(f"Privileges for {idno} : {priviledge_list}")
    except Exception as err:
        print(err)
      
main()
