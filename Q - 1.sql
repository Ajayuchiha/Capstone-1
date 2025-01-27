# 1. Find top 10 highest revenue generating products

select product_id, sum(sale_price) as top_products
from products_details
group by product_id
order by top_products desc
limit 10;
-- ------------------------------------------------------

# 2. Find the top 5 cities with the highest profit margins

select city, sum(profit) as profit_margins
from orders_details t1
join products_details t2 on t1.order_id = t2.order_id
group by city
order by profit_margins desc
limit 5;
-- ------------------------------------------------------

# 3. Calculate the total discount given for each category

select category, sum(discount) as total_discount 
from products_details
group by category
order by total_discount asc;
-- ------------------------------------------------------

# 4. Find the average sale price per product category

select category, avg(sale_price) as Avg_sales
from products_details
group by category
order by Avg_sales asc;
-- ------------------------------------------------------

# 5. Find the region with the highest average sale price

select region, avg(sale_price) as highest_average_sale 
from orders_details a1
join products_details a2 on a1.order_id = a2.order_id
group by region
order by highest_average_sale desc
limit 1;
-- ------------------------------------------------------

# 6. Find the total profit per category

select category, sum(profit) as total_profit
from products_details
group by category
order by category asc;
-- ------------------------------------------------------

# 7. Identify the top 3 segments with the highest quantity of orders

select segment, sum(quantity) as large_quantity
from orders_details f1
join products_details f2 on f1.order_id = f2.order_id
group by segment
order by large_quantity desc;
-- ------------------------------------------------------

# 8. Determine the average discount percentage given per region

select region, avg(discount_percentage) as  average_discount
from orders_details g1
join products_details g2 on g1.order_id = g2.order_id
group by region
order by average_discount asc;
-- ------------------------------------------------------

# 9. Find the product category with the highest total profit

select category, sum(profit) as highest_profit
from products_details
group by category
order by highest_profit desc;
-- ------------------------------------------------

# 10. Calculate the total revenue generated per year

select year(d.order_date) as year, sum(k.sale_price) as revenue_per_year
from orders_details d
join products_details k on d.order_id = k.order_id
group by year(d.order_date)
order by year desc;