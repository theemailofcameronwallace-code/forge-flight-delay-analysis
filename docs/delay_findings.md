# Cameron Wallace - SQL Findings

## Question
Which airlines experience the worst delays, and what are the largest causes of delays?

---

## Key Findings

### 1. Airlines with Worst Average Arrival Delays
- NK and F9 had the highest average arrival delays.
- NK and UA had the highest average departure delays.
- Major airlines such as AA and DL had lower average delays.

### 2. Largest Causes of Delays
- Late aircraft delay was the largest cause of delays overall.
- Air system delays were also a major cause.
- Security delays contributed very little to delays.

### 3. Delay Trends by Month
- Summer months showed higher average delays.
- February had the highest average arrival delay in the sample.

### 4. Airlines with Most Flights
- WN had the largest number of flights in the dataset.
- AA, DL, and OO also handled high flight volumes.

### 5. Airlines with Most Total Delay Minutes
- WN accumulated the highest total arrival delay minutes due to large flight volume.
- OO, EV, and AA also had large total delay values.

### 6. Taxi-Out Time Analysis
- Some airlines had significantly longer average taxi-out times than others.
- Longer taxi-out times may contribute to later delays.

---

## Tools Used
- MySQL Workbench
- SQL aggregation queries
- Random flight sample dataset (~98k flights)
