SELECT playerID,sum(HR) as careerHR
FROM batting
GROUP BY playerID
ORDER BY careerHR DESC
LIMIT 12