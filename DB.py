import psycopg2

conn=psycopg2.connect(host="localhost",dbname="postgres",user="postgres",
                       password="postgres",port="5432")
cur=conn.cursor()
cur.execute("""create table if not exists employees(
    emp_id integer primary key,
    first_name varchar(100),
    last_name varchar(100),
    salary  numeric(10,2),
    job_title varchar(100),
    gender varchar(10),
    hire_date date
);
""")

cur.execute("""create table if not exists departments(
    emp_id integer references employees(emp_id),
    department_name varchar(100),
    dep_id integer );""")
cur.execute("""insert into employees(emp_id, first_name, last_name, salary, job_title, gender, hire_date)
               values (17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04'),
                      (26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24'),
                    (30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02'),
    (49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22'),
    (51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29'),
    (67323, 'Lisa', 'Wiener', 75000, 'Business Analyst', 'Female', '2018-08-09'),
    (70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2018-12-20'),
    (71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-06-28'),
            (71119, 'John', 'Doe', 60000, 'Admin Assistant', 'Male', '2019-07-15'),
            (49823, 'AnyName', 'AnyLast', 70000, 'IT Officer', 'Male', '2019-03-01'),
    (76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2019-01-21'),
    (97927, 'Billie', 'Lanning', 67000, 'Web Developer', 'Female', '2018-06-25');""")

cur.execute("""
INSERT INTO departments(emp_id, department_name, dep_id)
VALUES 
    (17679, 'Operations', 13),
    (26650, 'Marketing', 14),
    (30840, 'Operations', 13),
    (49823, 'Technology', 12),
    (51821, 'Operations', 13),
    (67323, 'Marketing', 14),
    (71119, 'Administrative', 11),
    (76589, 'Operations', 13),
    (97927, 'Technology', 12);
""")

conn.commit()
cur.close()
conn.close()