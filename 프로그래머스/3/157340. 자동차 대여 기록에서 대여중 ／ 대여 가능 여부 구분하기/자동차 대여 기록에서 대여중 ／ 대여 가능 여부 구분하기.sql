-- 코드를 입력하세요
SELECT distinct car_id,
case 
    when car_id in 
    (   select car_id
        from car_rental_company_rental_history
        where START_DATE <= '2022-10-16' and END_DATE >= '2022-10-16'
    ) then '대여중'
    else '대여 가능'
END as AVAILABILITY
from car_rental_company_rental_history
order by car_id desc
