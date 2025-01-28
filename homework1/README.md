# Question 1
docker run -it --entrypoint=/bin/bash python:3.12.8

# Question 2
docker compose up -d

# Question 3
```sql
SELECT 
    COUNT(CASE WHEN trip_distance <= 1 THEN 1 END) as "Up to 1 mile",
    COUNT(CASE WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 END) as "1-3 miles",
    COUNT(CASE WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 END) as "3-7 miles",
    COUNT(CASE WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 END) as "7-10 miles",
    COUNT(CASE WHEN trip_distance > 10 THEN 1 END) as "Over 10 miles"
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_pickup_datetime < '2019-11-01';
```

I found this : 
104830;198995;109642;27686;35201

# Question 4
```sql
SELECT 
    DATE(lpep_pickup_datetime) as pickup_day,
    MAX(trip_distance) as longest_distance
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_pickup_datetime < '2019-11-01'
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY longest_distance DESC
LIMIT 1;
```

# Question 5
```sql
SELECT 
    tz."Zone" 
FROM green_taxi_trips gt
JOIN taxi_zones tz ON gt."PULocationID" = tz."LocationID" 
WHERE DATE(gt.lpep_pickup_datetime) = '2019-10-18'
GROUP BY tz."Zone" 
HAVING SUM(gt.total_amount) > 13000
ORDER BY SUM(gt.total_amount) DESC;
```

# Question 6
```sql
SELECT 
    dropoff."Zone" as dropoff_zone,
    MAX(gt.tip_amount) as max_tip
FROM green_taxi_trips gt
JOIN taxi_zones pickup ON gt."PULocationID" = pickup."LocationID"
JOIN taxi_zones dropoff ON gt."DOLocationID" = dropoff."LocationID"
WHERE 
    DATE(gt.lpep_pickup_datetime) >= '2019-10-01'
    AND DATE(gt.lpep_pickup_datetime) < '2019-11-01'
    AND pickup."Zone" = 'East Harlem North'
GROUP BY dropoff."Zone" 
ORDER BY max_tip DESC
LIMIT 1;
```
