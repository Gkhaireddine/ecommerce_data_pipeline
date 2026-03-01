
  create or replace   view ecommerce_db.ANALYTICS.orders_status
  
   as (
    WITH base AS (
  SELECT 
      o.order_id, 
      c.name AS customer_name, 
      o.order_date, 
      s.status,
      s.shipped_at, 
      s.delivered_at,

      CASE 
          WHEN s.shipped_at IS NOT NULL AND s.delivered_at IS NOT NULL 
              THEN DATEDIFF('hour', s.shipped_at, s.delivered_at)

          WHEN s.shipped_at IS NOT NULL AND s.delivered_at IS NULL 
              THEN DATEDIFF('hour', s.shipped_at, CURRENT_TIMESTAMP)

          ELSE NULL
      END AS delivery_hours

  FROM ecommerce_db.ANALYTICS.stg_orders o
  JOIN ecommerce_db.ANALYTICS.stg_shipments s 
      ON o.order_id = s.order_id
  JOIN ecommerce_db.ANALYTICS.stg_customers c 
      ON o.customer_id = c.customer_id
)

SELECT *,
       CASE 
           WHEN delivered_at IS NULL 
                AND shipped_at IS NOT NULL 
                AND delivery_hours > 48 
                THEN 'DELAYED'

           WHEN delivered_at IS NOT NULL 
                THEN 'DELIVERED'

           ELSE status
       END AS final_status

FROM base
  );

