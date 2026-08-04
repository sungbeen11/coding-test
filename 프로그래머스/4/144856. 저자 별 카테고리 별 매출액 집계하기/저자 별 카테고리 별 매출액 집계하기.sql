select i.author_id,author_name,category,sum(total)
from
(
    select b.book_id,author_id,category,sum(price*sales) total
    from book b join book_sales s
    on b.book_id = s.book_id
    where DATE_FORMAT(sales_date,"%Y-%m") = '2022-01'
    group by book_id
) i
join author j
on i.author_id = j.author_id
group by i.author_id,category
order by i.author_id,category desc