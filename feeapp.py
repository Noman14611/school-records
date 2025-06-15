import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime
from io import BytesIO

DATA_FILE = "fees.json"

# 🔹 Load & Save Functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# 🔹 Excel Export Helper
def convert_to_excel(data):
    rows = []
    for roll, info in data.items():
        for month, status in info.get("history", {}).items():
            rows.append({
                "Roll No": roll,
                "Name": info["name"],
                "Class": info["class"],
                "Monthly Fee": info["monthly_fee"],
                "Month": month,
                "Status": status
            })
    return pd.DataFrame(rows)

# 🔷 MAIN APP FUNCTION
def run_fee_app():
    st.title("💰 School Fee Records")
    data = load_data()
    today_month = datetime.now().strftime("%B")

    menu = st.radio("Choose Action", ["➕ Add Student", "📂 View Records", "📤 Export to Excel"])

    # ➕ Add or Update Student
    if menu == "➕ Add Student":
        st.subheader("Add / Update Student Record")
        roll = st.text_input("Roll Number")
        name = st.text_input("Student Name")
        class_name = st.text_input("Class")
        monthly_fee = st.number_input("Monthly Fee", min_value=0)
        status = st.selectbox("Fee Status for This Month", ["Paid", "Due"])

        if st.button("Save / Update"):
            if roll not in data:
                data[roll] = {
                    "name": name,
                    "class": class_name,
                    "monthly_fee": monthly_fee,
                    "history": {}
                }
            data[roll]["name"] = name
            data[roll]["class"] = class_name
            data[roll]["monthly_fee"] = monthly_fee
            data[roll]
