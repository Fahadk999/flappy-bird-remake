-- Adding score
INSERT INTO leaderboard (name, score)
VALUES (?, ?);

-- Getting score
SELECT name, score, dateAchived
FROM leaderboard
ORDER BY score DESC
LIMIT 5;

