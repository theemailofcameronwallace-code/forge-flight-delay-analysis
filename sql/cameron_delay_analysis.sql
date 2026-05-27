select
    airline,
    avg(arrival_delay) as avg_arrival_delay,
    count(*) as total_flights
from flights_random_sample
where cancelled = 0
group by airline
order by avg_arrival_delay desc;

select
    sum(airline_delay) as airline_delay,
    sum(weather_delay) as weather_delay,
    sum(air_system_delay) as air_system_delay,
    sum(security_delay) as security_delay,
    sum(late_aircraft_delay) as late_aircraft_delay
from flights_random_sample
where cancelled = 0;

select
    airline,
    avg(departure_delay) as avg_departure_delay
from flights_random_sample
where cancelled = 0
group by airline
order by avg_departure_delay desc;

select
    airline,
    count(*) as cancelled_flights
from flights_random_sample
where cancelled = 1
group by airline
order by cancelled_flights desc;