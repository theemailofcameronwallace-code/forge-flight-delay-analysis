USE project2;

SELECT airlines.AIRLINE, flights.MONTH, flights.DAY_OF_WEEK, TAXI_OUT, flights.DEPARTURE_DELAY, flights.DISTANCE
FROM flights
JOIN airlines
ON 
	flights.AIRLINE = airlines.IATA_CODE;