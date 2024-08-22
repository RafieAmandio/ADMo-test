# Data Engineering Intern Test
## Rafie Amandio Fauzan


## (Set B) No.1 Python
Write a function that takes two lists and returns a new list containing unique elements present in either of the original lists.
Input : ([1, 2, 6], [3, 4, 5])
Output : [1, 2, 3, 4, 5, 6]

### Code Result
```python
def setb_1(list1, list2):

    unique_set = set(list1).union(list2)
    
    return sorted(unique_set)
```
**How it works**
1. Receive 2 List from the function
 2. Create a union (merging the list) and make a set(unique element list) on that two list
 3. Return the sorted list

### Test Case
1. **Multiple Overlapping Elements**
   - **Input:** `setb_1([1, 2, 3], [2, 3, 4])`
   - **Expected:** `[1, 2, 3, 4]`


2. **Identical Elements in Both Lists**
   - **Input:** `setb_1([1, 1, 1], [1, 1])`
   - **Expected:** `[1]`
   
3. **Both Lists Empty**
   - **Input:** `setb_1([], [])`
   - **Expected:** `[]`
   
4. **One List Empty, Other Non-Empty**
   - **Input:** `setb_1([], [1, 2, 3])`
   - **Expected:** `[1, 2, 3]`
   
5. **Non-Overlapping Elements in Both Lists**
   - **Input:** `setb_1([1, 2, 3], [4, 5, 6])`
   - **Expected:** `[1, 2, 3, 4, 5, 6]`
   
6. **Negative and Positive Numbers**
   - **Input:** `setb_1([-1, -2, -3], [1, 2, 3])`
   - **Expected:** `[-3, -2, -1, 1, 2, 3]`
   
7. **Lists with Duplicates Across Both Lists**
   - **Input:** `setb_1([1, 2, 2, 3], [3, 4, 4, 5])`
   - **Expected:** `[1, 2, 3, 4, 5]`
   
8. **One List Contains a Single Element**
   - **Input:** `setb_1([7], [1, 2, 3])`
   - **Expected:** `[1, 2, 3, 7]`

### Testcase Result


## (Set B) No.2 SQL
**Dataset :** 
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



**Test:**
	1	Insert 5 records into the employees table with sample data.
	2	Write a query to retrieve all employees from the sales department.
	3	Write a query to find the highest salary among all employees.
	4	Write a query to calculate the average salary of all employees.
	5	Update the salary of the employee with employee_id 3 to 70000.
	6	Delete the employee with the lowest salary.

### Code Result
```sql
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
```

### Test Result
