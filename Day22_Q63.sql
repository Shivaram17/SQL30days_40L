
select p.product_name,
coalesce(sum( case when p.category = 'Electronics' then total_amount else 0 end),0) as electronics_total
 from products p
left join transactions t on p.product_id = t.product_id
group by p.product_name
order by electronics_total desc, p.product_name
