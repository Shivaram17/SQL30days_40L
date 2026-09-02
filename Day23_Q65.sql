select count(distinct owner_id) as distinct_owner
   from api_tokens
   where issued >= 2026-01-01 and issued < 2027-01-01;
