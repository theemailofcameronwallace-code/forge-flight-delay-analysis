use flight_project

db.flights_random_sample.countDocuments()

db.flights_random_sample.aggregate([
  { $match: { cancelled: 0 } },
  {
    $group: {
      _id: "$airline",
      avg_arrival_delay: { $avg: "$arrival_delay" },
      avg_departure_delay: { $avg: "$departure_delay" },
      total_flights: { $sum: 1 }
    }
  },
  { $sort: { avg_arrival_delay: -1 } }
])

db.flights_random_sample.aggregate([
  { $match: { cancelled: 0 } },
  {
    $group: {
      _id: null,
      airline_delay: { $sum: "$airline_delay" },
      weather_delay: { $sum: "$weather_delay" },
      air_system_delay: { $sum: "$air_system_delay" },
      security_delay: { $sum: "$security_delay" },
      late_aircraft_delay: { $sum: "$late_aircraft_delay" }
    }
  }
])