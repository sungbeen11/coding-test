select distinct id,email,first_name,last_name
from developers join skillcodes s
on skill_code & s.code = s.code
where category = 'Front End'
order by id