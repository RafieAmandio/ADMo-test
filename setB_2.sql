-- Rafie Amandio Fauzan
-- Data Engineering Intern Candidate

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);


INSERT INTO employees (employee_id, first_name, last_name, department, salary)
VALUES
    (1, 'John', 'Doe', 'Sales', 50000),
    (2, 'Jane', 'Smith', 'Marketing', 60000),
    (3, 'Bob', 'Johnson', 'Sales', 55000),
    (4, 'Alice', 'Williams', 'HR', 48000),
    (5, 'James', 'Brown', 'Sales', 52000);



-------------------------------------------------------------------------------
-- Test
-------------------------------------------------------------------------------

-- Test 1 : Insert 5 new records into the employees table with additional sample data
INSERT INTO employees (employee_id, first_name, last_name, department, salary)
VALUES
    (6, 'Rafie', 'Amandio', 'Marketing', 62000),
    (7, 'Amandio', 'Fauzan', 'Sales', 70000),
    (8, 'Katy', 'Perry', 'HR', 58000),
    (9, 'Taylor', 'Swift', 'Sales', 64000),
    (10, 'Michael', 'Jackson', 'HR', 50000);

-- Test 2 : Query to retrieve all employees from the Sales department
SELECT * FROM employees
WHERE department = 'Sales';

-- Test 3 : Query to find the highest salary among all employees
SELECT MAX(salary) AS highest_salary
FROM employees;

-- Test 4 : Query to calculate the average salary of all employees
SELECT AVG(salary) AS average_salary
FROM employees;

-- Test 5 : Update the salary of the employee with employee_id 3 to 70000
UPDATE employees
SET salary = 70000
WHERE employee_id = 3;

-- Test 6 : Delete the employee with the lowest salary
DELETE FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees);
