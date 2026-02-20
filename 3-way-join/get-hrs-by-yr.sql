SELECT batting.yearID, batting.HR FROM batting
WHERE batting.playerID = ?
GROUP BY batting.yearID
ORDER BY batting.yearID