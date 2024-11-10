SELECT league, college, min(year) start_year, max(year) end_year, COUNT(*) as frequency
from (
SELECT o.*,
             row_number() OVER (PARTITION BY league, college ORDER BY year) as seqnum
      from (
      select distinct league, college, year
      FROM playoff_roster
) o
) a
group by league, college, year - seqnum
order by 5 desc
limit 10;
