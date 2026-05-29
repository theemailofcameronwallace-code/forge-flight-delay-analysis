Create DATABASE project2;
USE project2;

SELECT 
	CASE DAY_OF_WEEK
	WHEN 1 THEN 'Sunday'
	WHEN 2 THEN 'Monday'
	WHEN 3 THEN 'Tuesday'
	WHEN 4 THEN 'Wednesday'
	WHEN 5 THEN 'Thursday'
	WHEN 6 THEN 'Friday'
	WHEN 7 THEN 'Saturday'
    END 
    AS 'day of week', 
    COUNT(*) AS TotalFlights
FROM flights
GROUP BY DAY_OF_WEEK
ORDER BY DAY_OF_WEEK;

SELECT 
	CASE flights.MONTH
	WHEN 1 THEN 'January'
	WHEN 2 THEN 'February'
	WHEN 3 THEN 'March'
	WHEN 4 THEN 'April'
	WHEN 5 THEN 'May'
	WHEN 6 THEN 'June'
	WHEN 7 THEN 'July'
	WHEN 8 THEN 'August'
	WHEN 9 THEN 'September'
	WHEN 10 THEN 'October'
	WHEN 11 THEN 'November'
	WHEN 12 THEN 'December'
    END AS 'Month', COUNT(*) AS TotalFlights
FROM flights
GROUP BY flights.MONTH
ORDER BY flights.MONTH;


SELECT flights.AIRLINE AS Airline, 
airlines.AIRLINE AS ID, 
COUNT(flights.AIRLINE) AS 'TotalFlights'
FROM flights
JOIN airlines
ON 
	flights.AIRLINE = airlines.IATA_CODE
GROUP BY flights.AIRLINE, airlines.AIRLINE
ORDER  BY TotalFlights DESC ;