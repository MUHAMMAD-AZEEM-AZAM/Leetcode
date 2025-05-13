# Write your MySQL query statement below
select e.machine_id,round(avg(a.timestamp-e.timestamp),3) as processing_time from Activity as e join Activity as a
where e.process_id=a.process_id and e.machine_id=a.machine_id and e.activity_type='start' and a.activity_type='end'
group by machine_id