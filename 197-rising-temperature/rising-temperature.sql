# Write your MySQL query statement below
select e.id from Weather as e join Weather as w where dateDiff(e.recordDate,w.recordDate)=1 and w.temperature<e.temperature