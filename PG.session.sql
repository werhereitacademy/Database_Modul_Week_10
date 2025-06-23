-- Q1 - 
select *
from employees
where salary > (
        select salary
        from employees
        where last_name = 'Weaver'
            and first_name = 'Rodney'
    );
--Q2 -
select max(salary) as Max_salary,
    min(salary) as Min_salary,
    avg(salary) as avg_salary
from employees --Q3-
select first_name,
    last_name,
    salary
from employees
where salary > 87000;
--Q4-
select first_name,
    last_name
from employees e,
    departments d
where e.emp_id = d.emp_id
    and d.department_name = 'Operations';
--Q5-
select first_name,
    last_name
from employees e,
    departments d
where e.emp_id = d.emp_id
    and d.department_name = 'Technology';
--Q6-
select avg(salary) as avg_salary_female
from employees
where gender = 'Female';
--Q7-
select avg(salary) as avg_salary , department_name  from employees e, departments d 
where e.emp_id=d.emp_id

GROUP BY department_name
َ--َ8-
select max(hire_date) as newest_date
, min(hire_date) as oldest_date from employees
--Q9-
select hire_date,department_name from employees e ,departments d 
where e.emp_id=d.emp_id and salary=(select max(salary) from employees)

--Q10-
select hire_date,department_name from employees e ,departments d 
where e.emp_id=d.emp_id and salary=(select min(salary) from employees)
