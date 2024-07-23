-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') 
from Book where category = '인문'and PUBLISHED_DATE like '%2021%' order by PUBLISHED_DATE asc;