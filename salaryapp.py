import streamlit as st
import json
import os

DATA_FILE = "salaries.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def run_salary_app():
    st.title("👨‍🏫 Teachers Salary Manager")
    data = load_data()

    st.subheader("Add/Update Teacher Salary")

    name = st.text_input("Teacher Name")
    salary = st.number_input("Monthly Salary", min_value=0)
    paid = st.radio("Salary Paid?", ["Yes", "No"])

    if st.button("Save Salary"):
        data[name] = {"salary": salary, "paid": paid}
        save_data(data)
        st.success(f"Salary record saved for {name}")

    st.subheader("All Salary Records")
    for name, record in data.items():
        st.write(f"{name} - Salary: {record['salary']} - Paid: {record['paid']}")
