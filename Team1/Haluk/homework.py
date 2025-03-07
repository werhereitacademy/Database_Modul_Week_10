import psycopg2

conn = psycopg2.connect(host='localhost',dbname='postgres',user='postgres',password='344230haluk',port=5432)

cur = conn.cursor()

# DEPARTMENTS_TABLE

cur.execute("""CREATE TABLE IF NOT EXISTS departments_table( 
    emp_id INT PRIMARY KEY,
    dept_name VARCHAR(100),
    dept_id INT
);
""")

cur.execute("""INSERT INTO departments_table (emp_id,dept_name,dept_id) VALUES
(17679, 'Operations', 13),
(26650, 'Marketing', 14),
(30840, 'Operations', 13),
(49823, 'Technology', 12),
(51821, 'Operations', 13),
(67323, 'Marketing', 14),
(71119, 'Administrative', 11),
(76589, 'Operations', 13),
(97927, 'Technology', 12)
ON CONFLICT (emp_id) DO NOTHING;
""")







# EMPLOYEES_TABLE OLUSTURULAN YER
cur.execute("""CREATE TABLE IF NOT EXISTS employees_table( 
    emp_id INT PRIMARY KEY,
    firs_name VARCHAR(100),
    last_name VARCHAR(100),
    salary INT,
    job_title VARCHAR(200),
    gender VARCHAR(20),
    hire_date DATE
);
""")

cur.execute("""INSERT INTO employees_table (emp_id,firs_name,last_name,salary,job_title,gender,hire_date) VALUES
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
ON CONFLICT (emp_id) DO NOTHING;
""")


conn.commit()
cur.close()
conn.close()