--1 
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 87000;

--2
SELECT MIN(salary), MAX(salary), AVG(salary)
FROM employees;

--3
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 87000;

--4
SELECT first_name, last_name
FROM employees
INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
WHERE dept_name = 'Operations';

--5 
SELECT first_name, last_name
FROM employees
INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
WHERE dept_name = 'Technology';

--6
SELECT AVG(salary)
FROM employees
WHERE gender = 'Female';

--7
SELECT departments_table.dept_name, AVG(salary)
FROM employees
INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
GROUP BY departments_table.dept_name;

--8 
SELECT MIN(hire_date) AS oldest_hire, MAX(hire_date) AS newest_hire
FROM employees;

--9
SELECT employees.hire_date, departments_table.dept_name
FROM employees
INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
WHERE employees.salary = (SELECT MAX(salary) FROM employees);

--10 
SELECT employees.hire_date, departments_table.dept_name
FROM employees
INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
WHERE employees.salary = (SELECT MIN (salary) FROM employees)
