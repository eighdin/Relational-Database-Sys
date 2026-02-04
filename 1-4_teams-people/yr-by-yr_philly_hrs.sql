SELECT yearID, sum(HR) as teamHR
FROM batting WHERE teamID = 'PHI'
GROUP BY yearID
ORDER BY teamHR DESC