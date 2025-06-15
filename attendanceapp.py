import streamlit as st
import json
import os
from datetime import date

DATA_FILE = "attendance.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def run_attendance_app():
    st.title("📋 School Attendance Tracker")
    data = load_data()

    today = str(date.today())
    st.subheader(f"Mark Attendance for {today}")

    student_name = st.text_input("Student Name")
    status = st.radio("Status", ["Present", "Absent"])

    if st.button("Submit Attendance"):
        if today not in data:
            data[today] = []
        data[today].append({"name": student_name, "status": status})
        save_data(data)
        st.success(f"Attendance marked for {student_name} as {status}")

    st.subheader("Today's Attendance")
    if today in data:
        for entry in data[today]:
            st.write(f"- {entry['name']}: {entry['status']}")
    else:
        st.info("No attendance marked yet.")
