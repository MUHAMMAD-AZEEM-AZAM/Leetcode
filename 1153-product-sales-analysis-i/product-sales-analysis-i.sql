# Write your MySQL query statement below
select product_name,year,price from Product as p
inner join Sales as s on p.product_id=s.product_id