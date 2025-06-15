import streamlit as st
import json
import os

DATA_FILE = "fees.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def run_fee_app():
    st.title("💰 School Fee Records")
    data = load_data()

    st.subheader("Add/Update Student Fee Record")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    fee = st.number_input("Monthly Fee", min_value=0)
    paid = st.radio("Fee Paid?", ["Yes", "No"])

    if st.button("Save Record"):
        data[roll] = {"name": name, "fee": fee, "paid": paid}
        save_data(data)
        st.success(f"Fee record saved for {name}")

    st.subheader("All Fee Records")
    for roll, record in data.items():
        st.write(f"{record['name']} (Roll: {roll}) - Fee: {record['fee']} - Paid: {record['paid']}")
