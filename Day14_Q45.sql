select distinct edge_loc from cdn_logs
where status < 400
order by edge_loc desc;
