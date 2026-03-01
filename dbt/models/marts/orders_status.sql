WITH base AS ( 
    SELECT 
    o.order_id, c.name AS customer_name, o.order_date, s.status, s.shipped_at, s.delivered_at, 
    DATEDIFF('hour', s.shipped_at, s.delivered_at) AS delivery_hours 
    FROM {{ ref('stg_orders') }} o 
    JOIN {{ ref('stg_shipments') }} s
    ON o.order_id = s.order_id 
    JOIN {{ ref('stg_customers') }} c 
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