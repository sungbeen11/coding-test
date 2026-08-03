select distinct id,email,first_name,last_name
from developers d join skillcodes s
on s.code & skill_code = s.code
where s.name in ("C#", "Python")
order by id
