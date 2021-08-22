CREATE DATABASE SECURITY_DB;
USE SECURITY_DB;

CREATE TABLE USER_ACCOUNTS (
    IdNo INT NOT NULL PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    Email VARCHAR(320) NOT NULL UNIQUE
);

CREATE TABLE USER_ROLES (
    IdNo INT NOT NULL PRIMARY KEY,
    RoleName VARCHAR(100) NOT NULL UNIQUE,
    RoleDescription VARCHAR(100) NOT NULL
);

CREATE TABLE RELATE_ACCOUNT_TO_ROLE (
    IdNo INT NOT NULL PRIMARY KEY,
    AccountIdNo INT NOT NULL UNIQUE,
    RoleIdNo INT NOT NULL UNIQUE,
    FOREIGN KEY (AccountIdNo) REFERENCES USER_ACCOUNTS(IdNo),
    FOREIGN KEY (RoleIdNo) REFERENCES USER_ROLES(IdNo)
);

CREATE TABLE USER_PRIVILEGES(
    IdNo INT NOT NULL PRIMARY KEY,
    PrivType VARCHAR(100) NOT NULL
);

CREATE TABLE USER_TABLES(
    TableName VARCHAR(100) NOT NULL PRIMARY KEY,
    AccountIdNo INT NOT NULL UNIQUE,
    FOREIGN KEY (AccountIdNo) REFERENCES USER_ACCOUNTS(IdNo)
);

CREATE TABLE ACCOUNT_PRIVILEGES(
    IdNo INT NOT NULL,    
    RName VARCHAR(100) NOT NULL,
    FOREIGN KEY (IdNo) REFERENCES USER_PRIVILEGES(IdNo),
    FOREIGN KEY (RName) REFERENCES USER_ROLES(RoleName)   
);

CREATE TABLE RELATION_PRIVILEGES(
    IdNo INT NOT NULL,    
    TName VARCHAR(100) NOT NULL,
    RName VARCHAR(100) NOT NULL,
    FOREIGN KEY (IdNo) REFERENCES USER_PRIVILEGES(IdNo),
    FOREIGN KEY (TName) REFERENCES USER_TABLES(TableName),
    FOREIGN KEY (RName) REFERENCES USER_ROLES(RoleName)
);