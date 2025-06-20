import psycopg2


DB_NAME = "project-1" 
DB_USER = "postgres"       
DB_PASS = "sql321!"       
DB_HOST = "localhost"           
DB_PORT = 5432                  

conn = None
cursor = None

try:
# 1. create database connection
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER,
        password=DB_PASS, port=DB_PORT
    )
    print("Database connection successful!")
    cursor = conn.cursor()

# 2. Create tables
    print("\nCreating tables...")
    create_employees_table_sql = """
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        salary INT,
        job_title VARCHAR(100),
        gender VARCHAR(10),
        hire_date DATE,
        dept_id INT
    );
    """
    create_departments_table_sql = """
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INT PRIMARY KEY,
        dept_name VARCHAR(100)
    );
    """
    cursor.execute(create_employees_table_sql)
    cursor.execute(create_departments_table_sql)
    conn.commit()
    print("Tables 'employees' and 'departments' created or already exist.")

# 3. Insert sample data
    print("\nInserting data...")
    insert_departments_data_sql = """
    INSERT INTO departments (dept_id, dept_name) VALUES
    (13, 'Operations'), (14, 'Marketing'), (12, 'Technology'), (11, 'Administrative')
    ON CONFLICT (dept_id) DO NOTHING;
    """
    insert_employees_data_sql = """
    INSERT INTO employees (emp_id, first_name, last_name, salary, job_title, gender, hire_date, dept_id) VALUES
    (17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04', 13),
    (26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24', 14),
    (30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02', 12),
    (49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22', 12),
    (51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29', 12),
    (67323, 'Lisa', 'Wiener', 75000, 'Business Analyst', 'Female', '2018-09-08', 14),
    (70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2018-12-20', 13),
    (71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-06-28', 11),
    (76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2019-01-21', 13),
    (97927, 'Bill', 'Lanning', 67000, 'Web Developer', 'Female', '2018-06-25', 12)
    ON CONFLICT (emp_id) DO NOTHING;
    """
    cursor.execute(insert_departments_data_sql)
    cursor.execute(insert_employees_data_sql)
    conn.commit()
    print("Sample data inserted or already exists.")

# 4. Execute and display results for all 10 queries
    print("\n--- Query Results ---")

# 1, to find employees who get paid more than Rodney Weaver.
    print("\n1. Employees paid more than Rodney Weaver:")
    query1 = """
    SELECT emp_id, first_name, last_name, salary
    FROM employees
    WHERE salary > (SELECT salary FROM employees WHERE first_name = 'Rodney' AND last_name = 'Weaver');
    """
    cursor.execute(query1)
    for row in cursor.fetchall():
        print(row)

# 2, to find the average, min and max salaries.
    print("\n2. Average, Min, Max Salaries:")
    query2 = "SELECT AVG(salary), MIN(salary), MAX(salary) FROM employees;"
    cursor.execute(query2)
    print(cursor.fetchone())

# 3, to find employees whose salary is more than 8700.
    print("\n3. Employees with salary > 8700:")
    query3 = "SELECT first_name, last_name, salary FROM employees WHERE salary > 8700;"
    cursor.execute(query3)
    for row in cursor.fetchall():
        print(row)

# 4, to find employees who work under the Operations department.
    print("\n4. Employees in Operations department:")
    query4 = """
    SELECT e.first_name, e.last_name
    FROM employees e JOIN departments d ON e.dept_id = d.dept_id
    WHERE d.dept_name = 'Operations';
    """
    cursor.execute(query4)
    for row in cursor.fetchall():
        print(row)

# 5,  to find employees who work under the Technology department.
    print("\n5. Employees in Technology department:")
    query5 = """
    SELECT e.first_name, e.last_name
    FROM employees e JOIN departments d ON e.dept_id = d.dept_id
    WHERE d.dept_name = 'Technology';
    """
    cursor.execute(query5)
    for row in cursor.fetchall():
        print(row)

# 6, find the average salary of female employees.
    print("\n6. Average salary of female employees:")
    query6 = "SELECT AVG(salary) FROM employees WHERE gender = 'Female';"
    cursor.execute(query6)
    print(cursor.fetchone())

# 7, find the average salaries of each department.
    print("\n7. Average salaries per department:")
    query7 = """
    SELECT d.dept_name, AVG(e.salary)
    FROM employees e JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY d.dept_name;
    """
    cursor.execute(query7)
    for row in cursor.fetchall():
        print(row)

# 8, find the oldest and newest employees.
    print("\n8. Oldest and Newest Employees (by hire_date):")
    query8 = """
    (SELECT emp_id, first_name, last_name, hire_date FROM employees ORDER BY hire_date ASC LIMIT 1)
    UNION ALL
    (SELECT emp_id, first_name, last_name, hire_date FROM employees ORDER BY hire_date DESC LIMIT 1);
    """
    cursor.execute(query8)
    for row in cursor.fetchall():
        print(row)

# 9, find the hiring date and department of the highest paid employee.
    print("\n9. Hiring date and department of highest paid employee:")
    query9 = """
    SELECT e.hire_date, d.dept_name
    FROM employees e JOIN departments d ON e.dept_id = d.dept_id
    ORDER BY e.salary DESC LIMIT 1;
    """
    cursor.execute(query9)
    print(cursor.fetchone())

# 10, find the hiring date and department of the lowest paid employee.
    print("\n10. Hiring date and department of lowest paid employee:")
    query10 = """
    SELECT e.hire_date, d.dept_name
    FROM employees e JOIN departments d ON e.dept_id = d.dept_id
    ORDER BY e.salary ASC LIMIT 1;
    """
    cursor.execute(query10)
    print(cursor.fetchone())

except Exception as e:
    print(f"An error occurred: {e}")
    if conn:
        conn.rollback() # Rollback any changes on error
finally:
# 5. Close cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("\nScript finished. Database connection closed.")