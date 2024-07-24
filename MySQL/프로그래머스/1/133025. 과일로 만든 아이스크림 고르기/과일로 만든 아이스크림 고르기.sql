-- 코드를 입력하세요
select icecream_info.flavor from icecream_info,FIRST_HALF
where INGREDIENT_TYPE = 'fruit_based' and ICECREAM_INFO.flavor = FIRST_HALF.flavor
and first_half.total_order > 3000
order by total_order desc;