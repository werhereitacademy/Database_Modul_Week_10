import psycopg2

baglan = psycopg2.connect(
    dbname= 'postgres',
    user= 'postgres',
    password='411.Falcon',
    host='localhost',
    port='5432'
)
baglan.autocommit = True
cursor = baglan.cursor()
baglan.close()

# Yeni veri tabanına bağlan
baglan = psycopg2.connect(
    dbname='benim_veritabanim',
    user='postgres',
    password='411.Falcon',
    host='localhost',
    port='5432'
)
cursor = baglan.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        salary INT NOT NULL,
        job_title VARCHAR(100) NOT NULL,
        gender  VARCHAR(20) NOT NULL CHECK(gender IN ('Female', 'Male')),                   
        hire_date DATE DEFAULT CURRENT_DATE
    );
""")
cursor.execute("""INSERT INTO employees (first_name, last_name, salary, job_title, gender) VALUES
('Robert', 'Gilmore', 110000, 'Operation Director', 'Male' ),             
('Elvis', 'Ritter', 86000, 'Sales Manager', 'Male' ),            
('David', 'Barrow', 85000, 'Data Scientist', 'Male' ),             
('Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male' ),            
('Linda', 'Foster', 95000, 'Data Scientist', 'Female' ),            
('Lisa', 'Wiener', 75000, 'Business Analyst', 'Female' ),             
('Rodney', 'Weaver', 87000, 'Project Manager', 'Male' ),             
('Gayle', 'Meyer', 77000, 'HR Manager', 'Female' ),             
('Jason', 'Christian', 99000, 'Project Manager', 'Male' ),             
('Billie', 'Lanning', 67000, 'Web Developer', 'Female' )            
ON CONFLICT (emp_id) DO NOTHING;
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        dept_id SERIAL PRIMARY KEY,
        dept_name VARCHAR(50) NOT NULL UNIQUE
               
    );
""")


cursor.execute("""
    INSERT INTO departments (dept_name) VALUES
    ('Operations'),
    ('Marketing'),
    ('Technology'),
    ('Administrative')
    ON CONFLICT ( dept_id) DO NOTHING;
""")



baglan.commit()

cursor.close()
baglan.close()