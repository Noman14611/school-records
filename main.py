import streamlit as st
from feeapp import run_fee_app
from attendanceapp import run_attendance_app
from salaryapp import run_salary_app

st.set_page_config(page_title="School App", layout="wide")
st.sidebar.title("🏫 School Management")

app = st.sidebar.selectbox("Select App", [
    "📋 Attendance Tracker",
    "💰 Fee Records",
    "👨‍🏫 Teacher Salary"
])

if app == "📋 Attendance Tracker":
    run_attendance_app()
elif app == "💰 Fee Records":
    run_fee_app()
elif app == "👨‍🏫 Teacher Salary":
    run_salary_app()
