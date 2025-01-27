-- 10 QUERIES and ANALYSIS

# 1. Find the number of orders shipped by each mode.

select ship_mode, COUNT(*) as num_orders
from orders_details
group by ship_mode
order by num_orders desc;
-- ------------------------------------------------------

# 2. Find top 10 orders with a total order value greater than $1000.

select order_id, SUM(sale_price * quantity) as order_value
from products_details 
group by order_id
having SUM(sale_price * quantity) > 1000
order by order_value desc
limit 10;
-- ------------------------------------------------------

# 3. What is the average profit per product in each sub_category?

select sub_category, AVG(profit) as avg_profit
from products_details 
group by sub_category
order by avg_profit;
-- ------------------------------------------------------

# 4. How many distinct products were sold in each category?

select category, COUNT(DISTINCT product_id) as products_sold
from products_details
group by category
order by products_sold desc;
-- ------------------------------------------------------

# 5. What is the total profit contribution of each region per year?

select year(order_date) as YEAR, od.region, sum(pd.profit) as total_profit
from orders_details od
join products_details pd on od.order_id = pd.order_id 
group by YEAR, region
order by region;
-- ------------------------------------------------------ 

# 6. Identify the state with the largest discount given and its total discount.

select state, sum(discount) as total_discount
from orders_details od
join products_details pd on od.order_id = pd.order_id 
group by state
order by total_discount desc
limit 1;
-- ------------------------------------------------------

# 7. What is the monthly trend of revenue generated of each categories?

select MONTH(order_date) as month, category, sum(sale_price) as total_revenue
from products_details pd
join orders_details od on pd.order_id = od.order_id
group by month, category
order by month, total_revenue desc;
-- ------------------------------------------------------

# 8. Which region has the highest profit to sale_price ratio?

select region, sum(profit) / sum(sale_price) as profit_sale_ratio
from orders_details od
join products_details pd on od.order_id = pd.order_id 
group by region
order by profit_sale_ratio desc
limit 1;
-- ------------------------------------------------------

# 9. Identify the top 10 most profitable products.

select product_id, sum(profit) as total_profit
from products_details
group by product_id
order by total_profit desc
limit 10;
-- ------------------------------------------------------

# 10. Find the 5 order with the highest profit.

select order_id, sum(profit) as highest_profit
from products_details 
group by order_id
order by highest_profit desc
limit 5;