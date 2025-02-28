import psycopg2

try:
    con = psycopg2.connect(
        dbname = "postgres",
        user = "postgres",
        password = "sunset2014",
        host = "localhost",
        port = "5432"
    )
    cur = con.cursor()
    cur.execute('''
        create table if not exists employees_table(
            emp_id bigint primary key,
            first_name varchar(50),
            last_name varchar(50),
            salary integer,
            job_title varchar(50),
            gender varchar(10),
            hire_date date          
                )
        ''')
    rows = [
        (17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04'),
        (26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24'),
        (30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02'),
        (49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22'),
        (51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29'),
        (67323, 'Lisa', 'Wiener', 75000, 'Business Analyst', 'Female', '2018-08-09'),
        (70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2018-12-20'),
        (71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-06-28'),
        (76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2019-01-21'),
        (97927, 'Billie', 'Lanning', 67000, 'Web Developer', 'Female', '2018-06-25')
    ]
    cur.executemany("""
        INSERT INTO employees_table (emp_id, first_name, last_name, salary, job_title, gender, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (emp_id) DO NOTHING;
    """, rows)

    cur.execute('''
        CREATE TABLE IF NOT EXISTS departments_table (
            emp_id BIGINT,
            dept_name VARCHAR(50),
            dept_id INTEGER,
            PRIMARY KEY (emp_id, dept_id)
        )
    ''')
    rows2 = [
        (17679, 'Operations', 13),
        (26650, 'Marketing', 14),
        (30840, 'Operations', 13),
        (49823, 'Technology', 12),
        (51821, 'Operations', 13),
        (67323, 'Marketing', 14),
        (71119, 'Administrative', 11),
        (76589, 'Operations', 13),
        (97927, 'Technology', 12)
    ]
    cur.executemany("""
        INSERT INTO departments_table (emp_id, dept_name, dept_id)
        VALUES (%s, %s, %s)
        ON CONFLICT (emp_id, dept_id) DO NOTHING;
    """, rows2)
    con.commit()
except Exception as e:
    print(f"connection failed:{e}")

# sorgular

print("________________question1_______________")
query_1 = "select * from employees_table where salary > (select salary from employees_table where first_name = 'Rodney' and last_name = 'Weaver')"
cur.execute(query_1)
question1 = cur.fetchall()
print(question1)
print("________________question2_______________")
query_2 = "select (min(salary)+max(salary))/2 from employees_table"
cur.execute(query_2)
question2 = cur.fetchall()
print(question2)
print("________________question3_______________")
query_3 = """SELECT first_name, last_name, salary FROM public.employees_table
where salary > 8700;"""
cur.execute(query_3)
question3 = cur.fetchall()
print(question3)
print("________________question4_______________")
query_4 = """SELECT first_name, last_name from employees_table
where emp_id in (select emp_id from departments_table)"""
cur.execute(query_4)
question4 = cur.fetchall()
print(question4)
print("________________question5_______________")
query_5 = """SELECT first_name, last_name from employees_table
where emp_id in (select emp_id from departments_table where dept_name = 'Technology')"""
cur.execute(query_5)
question5 = cur.fetchall()
print(question5)
print("________________question6_______________")
query6 = """select avg(salary) from employees_table
where gender = 'Female'"""
query_6 = """select avg(salary) from employees_table
where gender = 'Female'"""
cur.execute(query_6)
question6 = cur.fetchall()
print(question6)
print("________________question7_______________")
query7 = """SELECT dept_name, AVG(salary) AS avg_salary
FROM employees_table e
JOIN departments_table d
ON e.emp_id = d.emp_id
GROUP BY d.dept_name;
"""
cur.execute(query7)
question7 = cur.fetchall()
print(question7)
print("________________question8_______________")
query_8 = """select max(hire_date), min(hire_date) from employees_table"""
cur.execute(query_8)
question8 = cur.fetchall()
print(question8)
print("________________question9_______________")
query9 = """select hire_date, dept_name from employees_table e
join departments_table d on e.emp_id = d.emp_id
where e.salary = (select max(salary) from employees_table)"""
cur.execute(query9)
question9 = cur.fetchall()
print(question9)
print("________________question10_______________")
query10 = """select hire_date from employees_table where salary = (select min(salary) from employees_table)"""
cur.execute(query10)
question10 = cur.fetchall()
print(question10)

cur.close()
con.close()