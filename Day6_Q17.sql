



with team_stats as (
    select team1 as teams
    case when team1 = winner then 1 else 0 end as won,
    case when team1 <> winner then 1 else 0 end as lose
    from teams
    
    union all
    
    select team2 as teams
    case when team2 = winner then 1 else 0 end as won,
    case when team1 <> winner then 1 else 0 end as lose
    from teams
    
    )
    
 select teams,
   count(*) as total_played,
   sum(won) as won,
   sum(lose) as lose
   from team_stats
   group by teams
   order by won;



