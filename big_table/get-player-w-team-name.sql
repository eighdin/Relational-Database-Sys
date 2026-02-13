SELECT playerID, teams.name
FROM batting INNER JOIN teams
ON batting.teamID = teams.teamID AND batting.yearID = teams.yearID
WHERE batting.yearID = 1976