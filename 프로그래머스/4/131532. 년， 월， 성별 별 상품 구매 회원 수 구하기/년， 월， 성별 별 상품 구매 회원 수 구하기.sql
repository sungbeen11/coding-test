-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) as YEAR,MONTH(SALES_DATE) as MONTH,GENDER,count(distinct s.user_id) as USERS
from online_sale s join user_info i
on s.user_id = i.user_id
where gender is not null
group by YEAR(SALES_DATE),MONTH(SALES_DATE),GENDER
order by YEAR,MONTH,GENDER