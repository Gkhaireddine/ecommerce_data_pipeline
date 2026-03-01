
  create or replace   view ecommerce_db.ANALYTICS.stg_customers
  
   as (
    select * from raw.customers
  );

