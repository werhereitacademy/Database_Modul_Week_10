import psycopg2

# 1. Önce 'postgres' veritabanına bağlan ve yeni veritabanını oluştur
baglan = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='411.Falcon',
    host='localhost',
    port='5432'
)

baglan.autocommit = True  # CREATE DATABASE için autocommit açık olmalı
cursor = baglan.cursor()

# 'odev' veritabanı varsa oluşturma
cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'odev';")
db_var_mi = cursor.fetchone()

if not db_var_mi:
    cursor.execute("CREATE DATABASE odev;")
else:
    print("Veritabanı zaten var, oluşturulmadı.")

#1️⃣ pg_database, sistemdeki tüm veritabanlarının kayıtlı olduğu bir tablodur.
#2️⃣ datname = 'odev', bu tablo içinde "odev" adında bir veritabanı olup olmadığını kontrol eder.
#3️⃣ SELECT 1, sadece "odev" varsa 1 döndürmesini sağlar (gereksiz veri çekmemek için).

#📌 Eğer "odev" veritabanı varsa, sonuç olarak 1 döner.
#📌 Eğer yoksa, sonuç boş (None) olur.


cursor.close()
baglan.close()

# 2. Yeni oluşturduğun 'odev' veritabanına bağlan
baglan = psycopg2.connect(
    dbname='odev',
    user='postgres',
    password='411.Falcon',
    host='localhost',
    port='5432'
)

cursor = baglan.cursor()

# 3. 'employees' tablosunu oluştur
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id SERIAL PRIMARY KEY,
        first_name VARCHAR(100), 
        last_name VARCHAR(100),
        salary INT,
        job_title VARCHAR(200),
        gender VARCHAR(20),
        hire_date DATE       
    );               
""")


cursor.execute("""
    INSERT INTO employees (emp_id,first_name,last_name,salary,job_title,gender,hire_date) VALUES
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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments_table( 
        emp_id INT PRIMARY KEY,
        dept_name VARCHAR(100),
        dept_id INT
);
""")

cursor.execute("""
    INSERT INTO departments_table (emp_id,dept_name,dept_id) VALUES
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
# 1- Find the employees who get paid more than Rodney Weaver.
cursor.execute("""
    SELECT first_name, last_name, salary
    FROM employees
    WHERE salary > 87000;
""")
## print(cursor.fetchone())

# 2- Find the average, min and max salaries
cursor.execute("""
    SELECT MIN(salary), MAX(salary), AVG(salary)
    FROM employees;
""")
#print(cursor.fetchone())

# 3- Find the employees whose salary is more than 8700.
#  Our query should return first name, last name, and salary info of the employees.
cursor.execute("""
    SELECT first_name, last_name, salary
    FROM employees
    WHERE salary > 87000;
""")
# print(cursor.fetchone())

# 4- Find the employees (first name, last name from employees table) who work under the Operations department (departments table).
#  Our query should return first name and last name info.
cursor.execute("""
    SELECT first_name, last_name
    FROM employees
    INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
    WHERE dept_name = 'Operations';
""")
#print(cursor.fetchone())

# 5- Find the employees (first name, last name from employees table) who work under the Technology department (departments table).
#  Our query should return first name and last name info.
cursor.execute("""
    SELECT first_name, last_name
    FROM employees
    INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
    WHERE dept_name = 'Technology';
""")
#print(cursor.fetchone())

# 6- Find the average salary of female employees.
cursor.execute("""
    SELECT AVG(salary)
    FROM employees
    WHERE gender = 'Female';
""")
#print(cursor.fetchone())

# 7- Find the average salaries of each department.
cursor.execute("""
    SELECT departments_table.dept_name, AVG(salary)
    FROM employees
    INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
    GROUP BY departments_table.dept_name; 
""")
#print(cursor.fetchone())

# 8- Find the oldest and newest employees.
cursor.execute("""
SELECT MIN(hire_date) AS oldest_hire, MAX(hire_date) AS newest_hire
FROM employees;
""")
#print(cursor.fetchone())

# 9- Find the hiring date and department of the highest paid employee
cursor.execute("""
    SELECT employees.hire_date, departments_table.dept_name
    FROM employees
    INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
    WHERE employees.salary = (SELECT MAX(salary) FROM employees);
""")
# print(cursor.fetchone())

# 10-Find the hiring date and department of the lowest paid employee
cursor.execute("""
    SELECT employees.hire_date, departments_table.dept_name
    FROM employees
    INNER JOIN departments_table ON employees.emp_id = departments_table.emp_id
    WHERE employees.salary = (SELECT MIN (salary) FROM employees)
 """)



baglan.commit()
cursor.close()
baglan.close()
