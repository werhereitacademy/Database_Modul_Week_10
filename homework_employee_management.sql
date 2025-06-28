Create Table employees (
	emp_id Int Primary Key,
	first_name Varchar(50),
	last_name Varchar(50),
	salary Int,
	job_title Varchar(100),
	gender Varchar(10),
	hire_date Date
);

Create Table departments (
	emp_id Int,
	dept_name Varchar(50),
	dept_id Int,
	Foreign Key (emp_id) references employees(emp_id)
);

INSERT INTO employees (emp_id, first_name, last_name, salary, job_title, gender, hire_date) VALUES
(17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04'),
(26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24'),
(30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02'),
(49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22'),
(51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29'),
(67323, 'Lisa', 'Wiener', 75000, 'Business Analyst', 'Female', '2018-08-09'),
(70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2018-12-20'),
(71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-06-28'),
(76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2019-01-21'),
(97927, 'Billie', 'Lanning', 67000, 'Web Developer', 'Female', '2018-06-25');

INSERT INTO departments (emp_id, dept_name, dept_id) VALUES
(17679, 'Operations', 13),
(26650, 'Marketing', 14),
(30840, 'Operations', 13),
(51821, 'Operations', 13),
(67323, 'Marketing', 14),
(76589, 'Operations', 13),
(97927, 'Technology', 12);

INSERT INTO departments (emp_id, dept_name, dept_id)
VALUES (49714, 'Technology', 12); --for Hugo Forester

Select first_name, last_name, salary
From employees
Where salary > (
	 Select salary from employees
	 Where first_name = 'Rodney' and last_name = 'Weaver'
);

Select 
	Avg(salary) as average_salary,
	Min(salary) as min_salary,
	Max(salary) as max_salary
From employees;

Select first_name, last_name, salary
From employees
Where salary > 87000;

Select employees.first_name, employees.last_name
From employees
Join departments On employees.emp_id = departments.emp_id
Where departments.dept_name = 'Operations';

Select employees.first_name, employees.last_name
From employees
Join departments On employees.emp_id = departments.emp_id
Where departments.dept_name = 'Technology';

Select 
	Avg(salary) as average_female_salary
From employees
Where gender = 'Female';

Select departments.dept_name, Avg(employees.salary) as avg_salary
From employees
Join departments On employees.emp_id = departments.emp_id
Group By departments.dept_name;

Select first_name, last_name, hire_date
From employees
Order by hire_date ASC
LIMIT 1;

Select first_name, last_name, hire_date
From employees
Order by hire_date DESC
LIMIT 1;

Select employees.hire_date, dept_name
From employees
Join departments On employees.emp_id = departments.emp_id
Where employees.salary = (Select Max(salary) From employees);

Select employees.hire_date, dept_name
From employees
Join departments On employees.emp_id = departments.emp_id
Where employees.salary = (Select Min(salary) From employees);