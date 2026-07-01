-- prazo medio real x prazo estimado

select AVG(order_delivered_customer_date::timestamp - order_purchase_timestamp::timestamp) as prazo_real, AVG(order_estimated_delivery_date::timestamp - order_purchase_timestamp::timestamp) as prazo_estimado
from pedidos
where order_status = 'delivered';

-- prazo medio de entrega por mês e ano

select AVG(order_delivered_customer_date::timestamp - order_purchase_timestamp::timestamp), extract(year from order_purchase_timestamp::timestamp), extract(month from order_purchase_timestamp::timestamp)
from pedidos p
group by extract(year from order_purchase_timestamp::timestamp), extract(month from order_purchase_timestamp::timestamp);

-- prazo medio de entrega por estado

select AVG(order_delivered_customer_date::timestamp - order_purchase_timestamp::timestamp) as prazo_real, AVG(order_estimated_delivery_date::timestamp - order_purchase_timestamp::timestamp) as prazo_estimado, c.customer_state 
from pedidos p
join clientes c  on p.customer_id = c.customer_id
group by customer_state
order by prazo_real;

-- relação entre prazo de entrega e avaliação do cliente

select AVG(order_delivered_customer_date::timestamp - order_purchase_timestamp::timestamp) as entrega_media, a.review_score as avaliacao
from pedidos p 
join avaliacoes a on p.order_id = a.order_id 
group by a.review_score 
order by a.review_score;