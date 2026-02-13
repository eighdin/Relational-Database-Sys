SELECT batting.playerID, batting.teamID, teams.name, batting.HR
from batting INNER JOIN teams
ON batting.yearID = teams.yearID AND batting.teamID = teams.teamID
WHERE batting.playerID = 'ruthba01'