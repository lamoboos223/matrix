select count (*) from public.users;

select count (*) from public.rooms;

select * from public.rooms where room_id ='!<room_id>:twkl.chat';
select * from public.rooms where room_id ='!<room_id>:twkl.chat';

select * from public.rooms where room_id ='!<room_id>:twkl.chat';


select count(*) from public.events where "type" = 'm.room.message'; 

select public.rooms.room_id from public.rooms left outer join public.room_memberships on public.rooms.room_id = public.room_memberships.room_id where public.room_memberships.room_id is null ;

SELECT COUNT(*)
FROM rooms
WHERE NOT EXISTS (
    SELECT 1 FROM current_state_events cse WHERE cse.room_id = rooms.room_id
);


select distinct type from public.events;


select count(*) from public.room_memberships where room_id = '!<room_id>:twkl.chat';
select * from public.events where room_id = '!<room_id>:twkl.chat'; 



select count(*) from public.events where type = 'm.room.message' and date(TO_TIMESTAMP(received_ts/ 1000)) > '2023-08-23';


select public.events.instance_name, count(*) from public.events where public.events.type = 'm.room.message' group by public.events.instance_name; 
select public.events.instance_name, count(*) from public.events where public.events.type = 'm.room.create' group by public.events.instance_name; 


SELECT public.events.instance_name, COUNT(*) AS event_count
FROM public.events
WHERE public.events.type = 'm.room.create'
GROUP BY public.events.instance_name
ORDER BY event_count DESC;


SELECT public.events.instance_name, COUNT(*) AS event_count
FROM public.events
WHERE public.events.type = 'm.room.create'
GROUP BY public.events.instance_name
ORDER BY 
  substring(public.events.instance_name, '^[a-zA-Z]+'),
  substring(public.events.instance_name, '[0-9]+')::integer;