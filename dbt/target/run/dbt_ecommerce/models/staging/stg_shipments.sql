
  create or replace   view ecommerce_db.ANALYTICS.stg_shipments
  
   as (
    select * from raw.shipments
  );

