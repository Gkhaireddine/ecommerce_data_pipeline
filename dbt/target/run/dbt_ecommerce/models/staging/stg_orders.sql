
  create or replace   view ecommerce_db.ANALYTICS.stg_orders
  
   as (
    select * from raw.orders
  );

