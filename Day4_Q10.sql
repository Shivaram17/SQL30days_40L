The Ones Worth Paging
PySpark
The SRE team is building a triage chart covering the three severity levels that call for action: 
CRITICAL, ERROR, and WARN. Show each of these levels alongside the total number of log entries recorded for it.


select log_level,
count(*) as totol_count
from server_logs
where log_level not in ("DEBUG", "INFO")
group by log_level;
