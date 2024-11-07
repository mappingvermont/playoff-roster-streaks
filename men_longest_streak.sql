SELECT college, min(year) start_year, max(year) end_year, COUNT(*) as frequency
from (
SELECT o.*,
             row_number() OVER (PARTITION BY college ORDER BY year) as seqnum
      from (
      select distinct college, year
      FROM playoff_rosters
) o
) a
group by college, year - seqnum
order by 4 desc
limit 10;

