Use companydb;

SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, 
 Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Research" AND Salary < 60000 AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, 
Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Headquarters" AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Networking" AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Research" AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Software" AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Hardware" AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "Sales" AND E.Dno = D.Dnumber;
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "HR" AND E.Dno = D.Dnumber; 
SELECT Fname AS FIRST_NAME, Minit AS MIDDLE_NAME, Lname AS LAST_NAME, Salary, Ssn AS EMPLOYEE_ID FROM employee E, department D
 WHERE Dname = "QA" AND E.Dno = D.Dnumber;

#SELECT FNAME, Salary FROM (EMPLOYEE E JOIN DEPARTMENT ON Dno = Dnumber) where Dname = "Research";

SELECT Pname AS PROJECT_NAME, Hours AS HOURS_PER_WEEK 
From (EMPLOYEE JOIN WORKS_ON ON Essn = Ssn JOIN PROJECT ON Pno = Pnumber) WHERE Fname = "Mike" AND Lname = "Henderson";
SELECT SUM(EMPLOYEE.Salary) AS TOTAL_SUM_OF_SALARY FROM (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber) WHERE Dname = "Networking";  
 
SELECT Dname, COUNT(Distinct(Ssn)) FROM EMPLOYEE E, DEPARTMENT D, DEPT_LOCATIONS DL
WHERE E.Dno = D.Dnumber AND D.Dnumber = DL.Dnumber AND DL.Dnumber IN (SELECT Dnumber from DEPT_LOCATIONS 
WHERE Dlocation = "Houston" OR Dlocation = "Austin" OR Dlocation = "Dallas" OR Dlocation = "Arlington" 
OR Dlocation = "Staford" OR Dlocation = "Bellaire" OR Dlocation = "Sugarland")
GROUP BY Dname
ORDER BY COUNT(Distinct(Ssn)) DESC;

SELECT Dname, COUNT(Distinct(Ssn)) FROM EMPLOYEE E, DEPARTMENT D, DEPT_LOCATIONS DL
WHERE E.Dno = D.Dnumber AND D.Dnumber = DL.Dnumber AND SALARY >= 50000 AND DL.Dnumber IN (SELECT Dnumber from DEPT_LOCATIONS 
WHERE Dlocation = "Houston" OR Dlocation = "Austin" OR Dlocation = "Dallas" OR Dlocation = "Arlington" 
OR Dlocation = "Staford" OR Dlocation = "Bellaire" OR Dlocation = "Sugarland")
GROUP BY Dname
ORDER BY COUNT(Distinct(Ssn)) DESC; 
 
SELECT Dname AS DEPARTMENT_NAME, S.Fname AS MANAGER_FIRST_NAME, S.Lname AS MANAGER_LAST_NAME,
 COUNT(E.Ssn), SUM(E.Salary), MIN(E.Salary), MAX(E.Salary)
FROM EMPLOYEE E, EMPLOYEE S, DEPARTMENT D 
WHERE D.Mgr_ssn = S.Ssn AND E.Dno = D.Dnumber GROUP BY Dname ORDER BY Dname Asc;

SELECT Pname, COUNT(Ssn) FROM EMPLOYEE E, PROJECT P, WORKS_ON W
WHERE P.Pnumber =W.Pno AND E.Ssn = W.Essn GROUP BY Pname ORDER BY COUNT(Ssn) DESC; 

SELECT S.Fname AS SUPERVISOR_FIRST_NAME, S.Lname AS SUPERVISOR_LAST_NAME, COUNT(E.Ssn) AS TOTAL_EMPLOYEE_UNDER_SUPERVISION
FROM EMPLOYEE E, EMPLOYEE S 
WHERE E.Super_ssn = S.Ssn GROUP BY SUPERVISOR_FIRST_NAME ORDER BY COUNT(E.Ssn) DESC;


