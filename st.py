import streamlit as st
import pandas as pd
import mysql.connector  
import wordcloud as wc

mydb = mysql.connector.connect(
  host = "localhost", 
  user = "root", 
  password = "Narut0@kurama",
  database = 'retail_orders',
  autocommit = True)

mycursor = mydb.cursor(dictionary = True)

st.balloons()

@st.cache_data 
def query_database(query):
    df = pd.read_sql(query,mydb)
    return df

st.markdown("""
<style>
.title, .Overview, li, label, div, span, table{
    font-family: 'Times New Roman', serif;
}
.title {
    color: #2E2EFF;
    font-size: 50px;
    text-align: center;
    font-weight: bold;
}
.overview {
    color: #d209e0;
    font-size: 30px;
    font-weight: bold;
}
.description {
    font-size: 18px;
    color: #FFFFF4;
    line-height: 1.6;
    font-family: 'Times New Roman', serif;
}
.tools {
    font-size: 12px;
    color: #FFFFF4;
    font-family: 'Times New Roman', serif;
}
.sql {
    font-size: 18px;
    color: #09e0bc;
    line-height: 1.6;
    font-family: 'Times New Roman', serif;
    font-weight: bold;
}
.heading {
    color: #ffa200;
    font-size: 20px;
    font-family: 'Times New Roman', serif;
    font-weight: bold;
}
</style>""", unsafe_allow_html = True)

st.markdown("""<div class = "title">
Retail Orders Data Analysis
</div>""", unsafe_allow_html = True)

st.markdown("""<div class = "overview">
Overview
</div>""", unsafe_allow_html = True)

st.markdown("""
<div class = description>
            Retail Orders Data typically contains information 
            about customer orders, including order id's, order dates, product details, quantities, prices, customer demographics, 
            and delivery statuses. It helps analyze sales trends, customer behavior, 
            and supply chain efficiency.
        <br><br>
<span class = "heading"> Tools Used: </span>
<ul class = "tools">
    <li>VS Code</li>
    <li>Pandas</li>
    <li>MySQL</li>
    <li>Streamlit</li>
</ul> <br><br>
</div>""", unsafe_allow_html = True)

st.markdown("""
<div class = "sql">
    SQL Queries
</div>""", unsafe_allow_html = True)

# Queries Input
tabs = st.tabs(["Given Queries", "Framed Queries"])

with tabs[0]:  # Given Queries Tab
#1
    if st.button ("Find top 10 highest revenue generating products"):
        mycursor.execute("""
    select product_id, sum(sale_price) as top_products 
    from products_details
    group by product_id
    order by top_products desc
    limit 10;
""")
        st.table(mycursor)
#2
    if st.button("Find the top 5 cities with the highest profit margins"):
        mycursor.execute("""
    select city, sum(profit) as profit_margins
    from orders_details t1
    join products_details t2 on t1.order_id = t2.order_id
    group by city
    order by profit_margins desc
    limit 5;
""")
        st.table(mycursor)
#3
    if st.button("Calculate the total discount given for each category"):
        mycursor.execute("""
    select category, sum(discount) as total_discount 
    from products_details
    group by category
    order by total_discount asc;
""")
        st.table(mycursor)
#4
    if st.button("Find the average sale price per product category"):
        mycursor.execute("""
    select category, avg(sale_price) as Avg_sales
    from products_details
    group by category
    order by Avg_sales asc;
""")
        st.table(mycursor)
#5
    if st.button("Find the region with the highest average sale price"):
        mycursor.execute("""
    select region, avg(sale_price) as highest_average_sale 
    from orders_details a1
    join products_details a2 on a1.order_id = a2.order_id
    group by region
    order by highest_average_sale desc
    limit 1;
""")
        st.table(mycursor)
#6
    if st.button("Find the total profit per category"):
        mycursor.execute("""
    select category, sum(profit) as total_profit 
    from products_details
    group by category
    order by category asc;
""")
        st.table(mycursor)
#7
    if st.button("Identify the top 3 segments with the highest quantity of orders"):
        mycursor.execute("""
    select segment, sum(quantity) as large_quantity
    from orders_details f1
    join products_details f2 on f1.order_id = f2.order_id
    group by segment
    order by large_quantity desc;
""")
        st.table(mycursor)
#8
    if st.button("Determine the average discount percentage given per region"):
        mycursor.execute("""
    select region, avg(discount_percentage) as  average_discount
    from orders_details g1
    join products_details g2 on g1.order_id = g2.order_id
    group by region
    order by average_discount asc;
""")
        st.table(mycursor)
#9
    if st.button("Find the product category with the highest total profit"):
        mycursor.execute("""
    select category, sum(profit) as highest_profit
    from products_details
    group by category
    order by highest_profit desc;
""")
        st.table(mycursor)
#10
    if st.button("Calculate the total revenue generated per year"):
        mycursor.execute("""
    select year(d.order_date) as year, sum(k.sale_price) as revenue_per_year
    from orders_details d
    join products_details k on d.order_id = k.order_id
    group by year(d.order_date)
    order by year desc;
""")
        st.table(mycursor)
    
    
with tabs[1]:  # Framed Queries Tab
#1
    if st.button ("Find the number of orders shipped by each mode."):
        mycursor.execute("""
    select ship_mode, COUNT(*) as num_orders
from orders_details
group by ship_mode
order by num_orders desc;
""")
        st.table(mycursor)
#2
    if st.button("Find top 10 orders with a total order value greater than $1000."):
        mycursor.execute("""
    select order_id, SUM(sale_price * quantity) as order_value
from products_details 
group by order_id
having SUM(sale_price * quantity) > 1000
order by order_value desc
limit 10;
""")
        st.table(mycursor)
#3
    if st.button(" What is the average profit per product in each sub_category?"):
        mycursor.execute("""
    select sub_category, AVG(profit) as avg_profit
from products_details 
group by sub_category
order by avg_profit;
""")
        st.table(mycursor)
#4
    if st.button("How many distinct products were sold in each category?"):
        mycursor.execute("""
    select category, COUNT(DISTINCT product_id) as products_sold
from products_details
group by category
order by products_sold desc;
""")
        st.table(mycursor)
#5
    if st.button("What is the total profit contribution of each region per year?"):
        mycursor.execute("""
    select year(order_date) as YEAR, od.region, sum(pd.profit) as total_profit
from orders_details od
join products_details pd on od.order_id = pd.order_id 
group by YEAR, region
order by region;
""")
        st.table(mycursor)
#6
    if st.button("Identify the state with the largest discount given and its total discount."):
        mycursor.execute("""
    select state, sum(discount) as total_discount
from orders_details od
join products_details pd on od.order_id = pd.order_id 
group by state
order by total_discount desc
limit 1;
""")
        st.table(mycursor)
#7
    if st.button("What is the monthly trend of revenue generated of each categories?"):
        mycursor.execute("""
    select MONTH(order_date) as month, category, sum(sale_price) as total_revenue
from products_details pd
join orders_details od on pd.order_id = od.order_id
group by month, category
order by month, total_revenue desc;
""")
        st.table(mycursor)
#8
    if st.button("Which region has the highest profit to sale_price ratio?"):
        mycursor.execute("""
    select region, sum(profit) / sum(sale_price) as profit_sale_ratio
from orders_details od
join products_details pd on od.order_id = pd.order_id 
group by region
order by profit_sale_ratio desc
limit 1;
""")
        st.table(mycursor)
#9
    if st.button("Identify the top 10 most profitable products."):
        mycursor.execute("""
    select product_id, sum(profit) as total_profit
from products_details
group by product_id
order by total_profit desc
limit 10;
""")
        st.table(mycursor)
        
#10
    if st.button("Find the 5 order with the highest profit."):
        mycursor.execute("""
    select order_id, sum(profit) as highest_profit
from products_details 
group by order_id
order by highest_profit desc
limit 5;
""")
        
        st.table(mycursor)