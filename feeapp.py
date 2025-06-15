import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime
from io import BytesIO

DATA_FILE = "fees.json"

# Load and Save
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Convert to Excel
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
    df = pd.DataFrame(rows)
    return df

# Main App
def run_fee_app():
    st.title("💰 School Fee Records (Upgraded)")
    data = load_data()
    today_month = datetime.now().strftime("%B")

    menu = st.radio("Choose Action", ["➕ Add Student", "📂 View Records", "📤 Export to Excel"])

    if menu == "➕ Add Student":
        st.subheader("Add or Update Student Record")
        roll = st.text_input("Roll Number")
        name = st.text_input("Student Name")
        class_name = st.text_input("Class")
        monthly_fee = st.number_input("Monthly Fee", min_value=0)
        status = st.selectbox("This Month Fee Status", ["Paid", "Due"])

        if st.button("Save / Update"):
            if roll not in data:
                data[roll] = {
                    "name": name,
                    "class": class_name,
                    "monthly_fee": monthly_fee,
                    "history": {}
                }
            else:
                data[roll]["name"] = name
                data[roll]["class"] = class_name
                data[roll]["monthly_fee"] = monthly_fee

            data[roll]["history"][today_month] = status
            save_data(data)
            st.success(f"Record saved for {name}")

    elif menu == "📂 View Records":
        st.subheader("All Students Fee Records")

        # 🔍 Search + Filter
        search = st.text_input("🔍 Search by Name or Roll")
        filter_unpaid = st.checkbox("Show Only Unpaid")

        month_filter = st.selectbox("Select Month", ["All"] + list({m for d in data.values() for m in d.get("history", {})}))

        for roll, info in data.items():
            if (search.lower() in roll.lower() or search.lower() in info["name"].lower()):
                if filter_unpaid and info["history"].get(today_month) != "Due":
                    continue
                if month_filter != "All" and info["history"].get(month_filter) is None:
                    continue

                st.markdown(f"**{info['name']}** (Roll: {roll}, Class: {info['class']})")
                st.write(f"💵 Monthly Fee: {info['monthly_fee']}")
          st.write(f"📆 Fee Status for {month_filter if month_filter != 'All' else today_month}: {info['history'].get(month_filter if month_filter != 'All' else today_month, 'N/A')}")


