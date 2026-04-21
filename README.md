# OLA Ride Data Analysis

## About the Project

I worked on this project as part of my Data Analyst internship at Labmentix. The goal was to analyze OLA's ride-sharing data for July 2024 and extract useful business insights from it. The dataset had over 1 lakh ride records with details like booking status, vehicle type, payment method, ratings, and cancellation reasons.

The idea was simple — take raw data, clean it, ask the right questions, and present the findings in a way that actually helps a business make better decisions.

---

## What I Did

- Loaded and explored a dataset of 1,03,024 ride records
- Cleaned the data in MySQL — checked for nulls, verified data types, confirmed rating ranges
- Wrote 10 SQL queries to extract key business insights
- Built an interactive Power BI dashboard with 5 pages
- Developed a Streamlit web app to display SQL results and Power BI visuals

---

## Tools and Technologies

- **MySQL Workbench** — Data storage, cleaning, and querying
- **Power BI Desktop** — Interactive dashboard development
- **Python** — Streamlit app development
- **Streamlit** — Web application framework
- **VS Code** — Code editor
- **Git & GitHub** — Version control

---

## Dataset Details

- **Source:** OLA Ride Data — July 2024
- **Total Records:** 1,03,024 rows
- **Total Columns:** 20
- **Key Columns:** Booking ID, Booking Status, Vehicle Type, Ride Distance, Booking Value, Payment Method, Driver Ratings, Customer Rating, Cancellation Reasons

---

## SQL Queries Covered

1. Retrieve all successful bookings
2. Find average ride distance for each vehicle type
3. Get total number of cancelled rides by customers
4. List top 5 customers who booked the highest number of rides
5. Get number of rides cancelled by drivers due to personal and car related issues
6. Find maximum and minimum driver ratings for Prime Sedan bookings
7. Retrieve all rides where payment was made using UPI
8. Find average customer rating per vehicle type
9. Calculate total booking value of rides completed successfully
10. List all incomplete rides along with the reason

---

## Power BI Dashboard Pages

| Page | Visuals |
|---|---|
| Overall | Ride Volume Over Time, Booking Status Breakdown, KPI Cards |
| Vehicle Type | Total Booking Value, Ride Distance, Avg Ratings by Vehicle |
| Revenue | Revenue by Payment Method, Top 5 Customers, Ride Distance Per Day |
| Cancellation | Cancellation Reasons by Customer, Cancellation Reasons by Driver |
| Ratings | Avg Driver Ratings, Avg Customer Ratings by Vehicle Type |

---

## Key Insights

- 62.09% of total rides were successful in July 2024
- Tuesday recorded the highest ride volume throughout the month
- Cash is the most preferred payment method (54.90%) followed by UPI (40.39%)
- Prime Sedan generated the highest total booking value among all vehicle types
- "Driver not moving towards pickup location" is the top reason for customer cancellations
- "Personal & Car related issue" is the top reason for driver cancellations
- Overall average driver and customer ratings are both 4.00 out of 5
- Auto has the lowest average ride distance (6.24 km) showing it is preferred for short trips

---

## Project Structure

OLA_Project/
│
├── app.py                  # Streamlit web application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
└── images/                # Power BI dashboard screenshots
├── overall.jpg
├── vehicle_type.jpg
├── revenue.jpg
├── cancellation.jpg
└── ratings.jpg

---

## How to Run the App

1. Clone this repository
2. Install dependencies: pip install -r requirements.txt
3. Make sure MySQL is running with the ola_ride database
4. Run the Streamlit app: streamlit run app.py
5. Open browser at http://localhost:8501

---

## Business Recommendations

- Deploy more drivers on Tuesdays to meet peak demand
- Investigate and fix driver punctuality issues to reduce customer cancellations
- Encourage UPI payments through offers since digital payments are already at 40%
- Focus on Prime Sedan availability as it generates the most revenue
- Implement regular vehicle maintenance checks to reduce driver cancellations

---

## Acknowledgement

This project was completed as part of my Data Analyst internship at Labmentix. The dataset was provided by Labmentix for learning and analysis purposes.

---

*Analyst: RAvi Mamgai | Internship: Labmentix | July 2024*