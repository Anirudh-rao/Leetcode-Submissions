Write your MySQL query statement below
select 
e.unique_id as unique_id,
ea.name as name
from employees ea
Left join employeeUni e on e.id = ea.id