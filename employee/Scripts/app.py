import streamlit as st
import pandas as pd
from employee_crud import fetch_employees, add_employee
from department_crud import get_departments
from salary_crud import get_salaries
from attendance_crud import get_attendance
from leaves_crud import get_leaves
import datetime

st.title("Employee Management System")
menu = ["Home","User","Admin","View Employees", "Add Employee", "View Departments", "View Salaries", "View Attendance", "View Leaves"]
choice = st.sidebar.selectbox("Menu", menu)

if choice=="Home":
    st.image("https://www.phpcrm.com/wp-content/uploads/HR_Software.png")
elif choice=="User":
    st.write("This is a web application developed by Madhumati as a part of training project")    
elif choice=="Admin":
    st.video("https://www.youtube.com/watch?v=rLMb6kuJ7pk")
elif choice == "View Employees":
    data = fetch_employees()
    df = pd.DataFrame(data, columns=[
        "ID", "First Name", "Last Name", "Email", "Phone", "Gender", "Department", "Job Title", "Hire Date", "Status"
    ])
    st.dataframe(df)
elif choice == "Add Employee":
    st.subheader("Add New Employee")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
    department_id = st.number_input("Department ID", min_value=1)
    job_title = st.text_input("Job Title")
    hire_date = st.date_input("Hire Date", datetime.date.today())
    status = st.selectbox("Status", ['Active','On Leave','Resigned','Terminated'])

    if st.button("Add Employee"):
        add_employee(first_name, last_name, email, phone, gender, department_id, job_title, hire_date, status)
        st.success("Employee added successfully!")
elif choice == "View Departments":
    data = get_departments()
    df = pd.DataFrame(data, columns=["ID", "Name", "Manager ID", "Location"])
    st.dataframe(df)
elif choice == "View Salaries":
    data = get_salaries()
    df = pd.DataFrame(data, columns=["Salary ID", "Employee ID", "Basic Salary", "HRA", "DA", "Deductions", "Net Salary", "Pay Date"])
    st.dataframe(df)
elif choice == "View Attendance":
    data = get_attendance()
    df = pd.DataFrame(data, columns=["Attendance ID", "Employee ID", "Date", "Check-in", "Check-out", "Total Hours"])
    st.dataframe(df)
elif choice == "View Leaves":
    data = get_leaves()
    df = pd.DataFrame(data, columns=["Leave ID", "Employee ID", "Leave Type", "Start Date", "End Date", "Reason", "Status"])
    st.dataframe(df)
