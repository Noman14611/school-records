import streamlit as st
from attendanceapp import run_attendance_app
from feeapp import run_fee_app
from salaryapp import run_salary_app

st.set_page_config(page_title="School Management System", layout="wide")

st.sidebar.title("🏫 School Management System")
app = st.sidebar.selectbox("Choose App", [
    "📋 School Attendance Tracker",
    "💰 School Fee Records",
    "👨‍🏫 Teachers Salary Manager"
])

if app == "📋 School Attendance Tracker":
    run_attendance_app()
elif app == "💰 School Fee Records":
    run_fee_app()
elif app == "👨‍🏫 Teachers Salary Manager":
    run_salary_app()
