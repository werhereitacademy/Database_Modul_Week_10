import psycopg2
conn=psycopg2.connect(host="localhost", database="postgres", user="postgres", password= "?", port="5432")
cur=conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary NUMERIC(10, 2),
    job_title VARCHAR(255),
    gender CHAR(10),
    hire_date DATE
);""")

cur.execute("""INSERT INTO employees (emp_id, first_name, last_name, salary, job_title, gender, hire_date) VALUES
(17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04'),
(26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24'),
(30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02'),
(49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22'),
(51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29'),
(67323, 'Lisa', 'Wiener', 75000, 'Business Analyst', 'Female', '2018-08-09'),
(70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2018-12-20'),
(71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-06-28'),
(76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2019-01-21'),
(97927, 'Billie', 'Lanning', 67000, 'Web Developer', 'Female', '2018-06-25') ON CONFLICT (emp_id) DO NOTHING;""")

cur.execute(""" CREATE TABLE IF NOT EXISTS departments (
    emp_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(255),
    dept_id INTEGER
);""")

cur.execute("""INSERT INTO departments (emp_id, dept_name, dept_id) VALUES
(17679,  'Operations', 13),
(26650,  'Marketing', 14),
(30840,  'Operations', 13),
(49823,  'Technology', 12),
(51821,  'Operations', 13),
(67323,  'Marketing', 14),
(71119,  'Administative', 11),
(76589,  'Operations', 13),
(97927,  'Technology', 12) ON CONFLICT (emp_id) DO NOTHING;""")



''' 
# 1. this code finds the employees who get paid more than Rodney Weaver and prints the result here

cur.execute("""SELECT * FROM employees WHERE salary > (SELECT salary FROM employees WHERE first_name = 'Rodney' AND last_name = 'Weaver');""")
results = cur.fetchall()
for row in results:
    print(row)


'''

# 2. this code finds max and min salary and prints the result here
   
'''
cur.execute("""SELECT Max(salary) FROM employees;""")
max = cur.fetchone()
print("Max salary:", max[0])

cur.execute("""SELECT Min(salary) FROM employees;""")
min = cur.fetchone()
print("Min salary:", min[0])

'''

# 3. this code finds the employees who get paid more than 8700 and prints the result here
'''
cur.execute("""SELECT first_name, last_name, salary from employees where salary>8700;""")
results = cur.fetchall()
for row in results:
    print(row)

    '''

# 4. Find the employees (first name, last name from employees table) who work under the Operations department (departments table). Our query should return first name and last name info.
'''
cur.execute("""SELECT employees.first_name, employees.last_name
               FROM employees
               INNER JOIN departments ON employees.emp_id = departments.emp_id
               WHERE departments.dept_name = 'Operations';""")
results = cur.fetchall()
for row in results:
    print(row)
'''

# 5. Find the employees (first name, last name from employees table) who work under the Technology department (departments table). Our query should return first name and last name info.
'''
cur.execute("""SELECT employees.first_name, employees.last_name
               FROM employees
               INNER JOIN departments ON employees.emp_id = departments.emp_id
               WHERE departments.dept_name = 'Technology';""")
results = cur.fetchall()
for row in results:
    print(row)

'''
# 6. Find the average salary of female employees.
'''
cur.execute("""SELECT AVG(salary) FROM employees WHERE gender = 'Female';""")
avg_female_salary = cur.fetchone()
print("Average salary of female employees:", avg_female_salary[0])

'''
# 7. Find the average salary of each department.
'''
cur.execute("""SELECT departments.dept_name, AVG(employees.salary) AS avg_salary
               FROM employees
               INNER JOIN departments ON employees.emp_id = departments.emp_id
               GROUP BY departments.dept_name;""")

results = cur.fetchall()
for row in results:
    print(row)
'''
# 8. Find the oldest and newest employee in the employees table and print their first name and last name
'''
cur.execute("""
SELECT first_name, last_name
FROM employees
WHERE hire_date = (SELECT MIN(hire_date) FROM employees)
   OR hire_date = (SELECT MAX(hire_date) FROM employees);
""")
results = cur.fetchall()
for row in results:
    print(row)
'''
# 9. Find the hire date and department name of the employee with the highest salary.
'''

cur.execute("""
SELECT employees.hire_date, departments.dept_name
FROM employees
JOIN departments ON employees.emp_id = departments.emp_id
WHERE employees.salary = (SELECT MAX(salary) FROM employees);
""")
results = cur.fetchall()
for row in results:
    print(row)
'''
# 10. Find the hire date and department name of the employee with the lowest salary. If there is no department information of the lowest paid employee, print its lowest salary and print no department information.   

cur.execute("""
SELECT employees.hire_date, departments.dept_name
FROM employees
LEFT JOIN departments ON employees.emp_id = departments.emp_id
WHERE employees.salary = (SELECT MIN(salary) FROM employees);
""")
results = cur.fetchall()
for row in results:
    print(row)
    if row[1] is None:
        print("No department information")
    else:
        print("Department:", row[1])

conn.commit()
cur.close()