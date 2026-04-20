# Write your MySQL query statement below
Select 
r.contest_id as contest_id,
round(count(distinct u.user_id) *100/ (Select count(*) from Users),2) As percentage
from  Users u
Inner Join Register r 
on r.user_id = u.user_id
Group by r.contest_id
Order by percentage desc , r.contest_id asc