db.flights.aggregate([
    {
        $group: {
            _id: "$DAY_OF_WEEK",
            TotalFLights: {$sum:1 }
    
        }
    },
    {
        $sort: { _id:1}
    }
])

db.flights.aggregate([
    {
        $group: {
            _id: "$MONTH",
            TotalFLights: {$sum:1 }
    
        }
    },
    {
        $sort: { _id:1}
    }
])