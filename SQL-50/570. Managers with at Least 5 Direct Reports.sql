# Write your MySQL query statement below
Select E1.Name
from employee e1
join(
    select managerId, count(*) as directReports
    from employee
    group by managerId
    having count(*) >= 5
)E2 on E2.managerId = E1.id