COPY playoff_roster
FROM '/Users/charlie/Desktop/dev/playoff-roster-streaks/data/nba.csv'
DELIMITER ',' CSV HEADER quote '"';

COPY playoff_roster
FROM '/Users/charlie/Desktop/dev/playoff-roster-streaks/data/wnba.csv'
DELIMITER ',' CSV HEADER quote '"';
