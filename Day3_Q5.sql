-- Active Users With April Transactions
-- SQL
-- The growth team is measuring transacting reach for April 2026.
-- How many users with active accounts completed at least one transaction during that month? Return a single count.


select count(Distinct t.user_id) as active_users_with_transactions
from transactions t
left join users u on t.user_id = u.user_id
where u.account_status = 'active' and
 (t.transaction_date >= '2026-04-01' and  t.transaction_date <= '2026-04-30')
group by t.user_id;
