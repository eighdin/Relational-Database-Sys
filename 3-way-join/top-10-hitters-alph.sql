WITH top_hitters AS(
	SELECT people.nameFirst, people.nameLast FROM
	batting INNER JOIN people
	ON batting.playerID = people.playerID
	WHERE batting.teamID = "PHI"
	GROUP BY batting.playerID
	ORDER BY sum(batting.HR) DESC
	LIMIT 10
)
SELECT CONCAT(nameFirst, " ", nameLast) as nameFull
FROM top_hitters
ORDER BY nameLast ASC
