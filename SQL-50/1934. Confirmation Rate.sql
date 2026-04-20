# Write your MySQL query statement below
Select 
s.user_id,
round(avg(
    Case
        when c.action ='Confirmed' Then 1.00
        Else 0
    End
    ),
    2
)confirmation_rate
From Signups s
left join  Confirmations c on 
s.user_id = c.user_id
group by s.user_id;