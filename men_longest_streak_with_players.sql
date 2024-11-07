select playoff_rosters.*, frequency as consecutive_years
from (
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
limit 5
) ranked
join playoff_rosters
using ( college )
where year between start_year and end_year
order by frequency desc, year, player;

