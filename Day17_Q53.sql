
select distinct u.username,d.device_type
 from users u
join user_sessions s on u.user_id = s.user_id
join devices d on s.device_id = d.device_id
