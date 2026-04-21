create database ola_ride;

USE ola_ride;

Select * from ola_dataset_july;

SELECT BOOKING_STATUS, COUNT(BOOKING_STATUS) FROM OLA_DATASET_JULY
GROUP BY BOOKING_STATUS
order by COUNT(BOOKING_STATUS);

SELECT INCOMPLETE_RIDES_REASON, COUNT(INCOMPLETE_RIDES_REASON)
FROM OLA_DATASET_JULY
GROUP BY INCOMPLETE_RIDES_REASON;

Select COUNT(*) from ola_dataset_july
WHERE BOOKING_VALUE=0 OR BOOKING_VALUE IS NULL;

SELECT * FROM ola_dataset_july
where ride_distance=0 or ride_distance is null;

select vehicle_type, count(*)
from ola_dataset_july
group by vehicle_type;

SELECT * FROM ola_dataset_july
where payment_method is null;

Select count(*) from ola_dataset_july
where payment_method is not null;

create table ola_dataset as
select date, time, Booking_Status, Customer_ID, Vehicle_Type, V_TAT, C_TAT, 
Canceled_Rides_by_Customer, Canceled_Rides_by_Driver, Incomplete_Rides, Driver_Ratings, Customer_Rating
from ola_dataset_july;

SELECT * FROM OLA_DATASET;

show tables from ola_ride;

update ola_dataset
set v_tat=coalesce(v_tat, 0),
    c_tat=coalesce(c_tat, 0)
where v_tat is null or c_tat is null;

update ola_dataset
set driver_ratings = (
	select median(driver_ratings)
    from ola_dataset
    where driver_ratings is not null)
    where driver_ratings is null;