# ============================================
# OLA Ride Data Analysis - Streamlit App
# Analyst: Ravi Mamgai
# Date: April 2026
# ============================================

import streamlit as st
import pandas as pd
import mysql.connector

# --------------------
# Page Configuration
# --------------------
st.set_page_config(
    page_title="OLA Ride Analysis",
    page_icon="🚖",
    layout="wide"
)

# --------------------
# Custom CSS
# --------------------
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .block-container { padding: 2rem; }
    h1, h2, h3 { color: #00CC00; }
    .stMetric {
        background-color: #1a1a1a;
        border: 1px solid #00CC00;
        border-radius: 10px;
        padding: 10px;
    }
    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
        font-size: 16px !important;
    }
    [data-testid="stMetricValue"] {
        color: #00CC00 !important;
        font-size: 28px !important;
    }
    .section-box {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00CC00;
        margin-bottom: 20px;
    }
    .insight-box {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FF6600;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------
# Database Connection
# --------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="9997275784",
        database="ola_ride"
    )

# --------------------
# Header
# --------------------
st.markdown("""
    <div style='background-color:#1a1a1a; padding:20px; border-radius:10px;
    border-left: 5px solid #00CC00; margin-bottom:20px;'>
        <h1 style='color:#00CC00; margin:0;'>🚖 OLA Ride Data Analysis</h1>
        <p style='color:#FFFFFF; margin:0;'>July 2024 | Analyst: Ravi Mamgai</p>
    </div>
""", unsafe_allow_html=True)

# --------------------
# KPI Cards
# --------------------
st.markdown("<h2 style='color:#00CC00;'>📊 Key Performance Indicators</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("🚖 Total Bookings", "1,03,024")
col2.metric("💰 Total Booking Value", "₹57M")
col3.metric("✅ Success Rate", "62%")
col4.metric("📍 Avg Ride Distance", "14.19 Km")

st.markdown("---")

# --------------------
# Power BI Dashboards
# --------------------
st.markdown("<h2 style='color:#00CC00;'>📈 Power BI Dashboard Visuals</h2>", unsafe_allow_html=True)

# Overall
st.markdown("<h3 style='color:#FF6600;'>1. Overall Summary</h3>", unsafe_allow_html=True)
st.image("images/overall.jpg", use_container_width=True)
# st.markdown("""
#     <div class='insight-box'>
#         <p style='color:#FFFFFF;'>📌 Total <b style='color:#00CC00;'>1,03,024 rides</b> recorded in July 2024 with a success rate of <b style='color:#00CC00;'>62.09%</b></p>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#00CC00;'>Tuesday</b> recorded highest ride volume while <b style='color:#FF6600;'>Sunday</b> had the lowest</p>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#FF6600;'>17.89%</b> rides were cancelled by drivers — a significant operational concern</p>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("---")

# Vehicle Type
st.markdown("<h3 style='color:#FF6600;'>2. Vehicle Type Analysis</h3>", unsafe_allow_html=True)
st.image("images/vehicle_type.jpg", use_container_width=True)
# st.markdown("""
#     <div class='insight-box'>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#00CC00;'>Prime Sedan</b> generated highest total booking value (₹82.98L)</p>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#FF6600;'>Auto</b> has lowest average ride distance (6.24 km) — preferred for short trips</p>
#         <p style='color:#FFFFFF;'>📌 All vehicle types show similar successful booking values between ₹48L to ₹52L</p>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("---")

# Revenue
st.markdown("<h3 style='color:#FF6600;'>3. Revenue Analysis</h3>", unsafe_allow_html=True)
st.image("images/revenue.jpg", use_container_width=True)
# st.markdown("""
#     <div class='insight-box'>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#00CC00;'>Cash</b> is the most preferred payment method (54.90%) followed by UPI (40.39%)</p>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#FF6600;'>CID785112</b> is the highest spending customer at ₹8,025</p>
#         <p style='color:#FFFFFF;'>📌 Ride distance remains consistently between 46K-51K km per day throughout July</p>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("---")

# Cancellation
st.markdown("<h3 style='color:#FF6600;'>4. Cancellation Analysis</h3>", unsafe_allow_html=True)
st.image("images/cancellation.jpg", use_container_width=True)
# st.markdown("""
#     <div class='insight-box'>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#FF6600;'>"Driver not moving towards pickup"</b> is top customer cancellation reason (3,175 rides)</p>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#FF6600;'>"Personal & Car related issue"</b> is top driver cancellation reason (6,542 rides)</p>
#         <p style='color:#FFFFFF;'>📌 OLA should implement <b style='color:#00CC00;'>stricter driver accountability</b> and vehicle maintenance checks</p>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("---")

# Ratings
st.markdown("<h3 style='color:#FF6600;'>5. Ratings Analysis</h3>", unsafe_allow_html=True)
st.image("images/ratings.jpg", use_container_width=True)
# st.markdown("""
#     <div class='insight-box'>
#         <p style='color:#FFFFFF;'>📌 Overall average driver and customer ratings are both <b style='color:#00CC00;'>4.00 out of 5</b></p>
#         <p style='color:#FFFFFF;'>📌 <b style='color:#00CC00;'>eBike</b> and <b style='color:#00CC00;'>Prime SUV</b> have highest driver ratings (4.01)</p>
#         <p style='color:#FFFFFF;'>📌 Consistent ratings across all vehicle types suggest <b style='color:#00CC00;'>uniform service quality</b></p>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("---")

# --------------------
# SQL Query Results
# --------------------
st.markdown("<h2 style='color:#00CC00;'>🔍 SQL Query Results</h2>", unsafe_allow_html=True)

conn = get_connection()

queries = {
    "1. All Successful Bookings": "SELECT * FROM ola_dataset WHERE Booking_Status = 'Success' LIMIT 100",
    "2. Avg Ride Distance by Vehicle Type": "SELECT Vehicle_Type, AVG(Ride_Distance) AS Avg_Distance FROM ola_dataset GROUP BY Vehicle_Type",
    "3. Total Cancelled Rides by Customer": "SELECT COUNT(*) AS Total_Cancelled FROM ola_dataset WHERE Booking_Status = 'Canceled by Customer'",
    "4. Top 5 Customers by Rides": "SELECT Customer_ID, COUNT(*) AS Total_Rides FROM ola_dataset GROUP BY Customer_ID ORDER BY Total_Rides DESC LIMIT 5",
    "5. Driver Cancellations - Personal & Car Issue": "SELECT COUNT(*) AS Total FROM ola_dataset WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue'",
    "6. Max & Min Driver Ratings - Prime Sedan": "SELECT MAX(Driver_Ratings) AS Max_Rating, MIN(Driver_Ratings) AS Min_Rating FROM ola_dataset WHERE Vehicle_Type = 'Prime Sedan'",
    "7. UPI Payment Rides": "SELECT * FROM ola_dataset WHERE Payment_Method = 'UPI' LIMIT 100",
    "8. Avg Customer Rating by Vehicle Type": "SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Rating FROM ola_dataset GROUP BY Vehicle_Type",
    "9. Total Booking Value - Successful Rides": "SELECT SUM(Booking_Value) AS Total_Value FROM ola_dataset WHERE Booking_Status = 'Success'",
    "10. Incomplete Rides with Reason": "SELECT Booking_ID, Vehicle_Type, Incomplete_Rides_Reason FROM ola_dataset WHERE Incomplete_Rides = 'Yes'"
}

selected_query = st.selectbox("Select a Query to View Results", list(queries.keys()))
df = pd.read_sql(queries[selected_query], conn)
st.markdown(f"<p style='color:#00CC00;'>Showing <b>{len(df)}</b> records</p>", unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)

conn.close()

# --------------------
# Footer
# --------------------
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#666666; padding:10px;'>
        <p>OLA Ride Data Analysis | Internship Project | Labmentix | Analyst: Ravi Mamgai | July 2024</p>
    </div>
""", unsafe_allow_html=True)