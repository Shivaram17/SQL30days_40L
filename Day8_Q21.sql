 select distinct lower(author) as author,
 count(distinct repo_name) as repo_count
 from repo_commits
 group by author
 having count(repo_name)  > 1;
