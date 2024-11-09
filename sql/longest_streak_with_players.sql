select playoff_roster.*, frequency as consecutive_years
from (
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
limit 5
) ranked
join playoff_roster
using ( league, college )
where year between start_year and end_year
order by frequency desc, college, year, player;

