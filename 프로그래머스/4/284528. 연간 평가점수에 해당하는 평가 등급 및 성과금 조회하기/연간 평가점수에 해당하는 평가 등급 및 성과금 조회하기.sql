select e.emp_no,emp_name,grade,
case
    when grade = 'S' then SAL * 0.2
    when grade = 'A' then SAL * 0.15
    when grade = 'B' then SAL * 0.1
    else 0
end as BONUS
from hr_employees e join 
(
    select emp_no,
    case
        when AVG(score) >= 96 then 'S'
        when AVG(score) >= 90 then 'A'
        when AVG(score) >= 80 then 'B'
    else 'C' END as GRADE
    from hr_grade
    group by emp_no
) g
on e.emp_no = g.emp_no
order by e.emp_no