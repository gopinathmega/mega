import streamlit as st
import pandas as pd
from datetime import datetime

# Load attendance data
def load_data():
    try:
        data = pd.read_csv("attendance.csv")
        
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Name", "ID", "Attendance Date"])
    return data

# Save attendance data
def save_data(data):
    data.to_csv("attendance.csv", index=False)

# Display the app
def main():
    st.title("Class Attendance Tracker")

    # Load attendance data
    data = load_data()

    # Enter student details
    name = st.text_input("Enter your name")
    student_id = st.text_input("Enter your ID")
    attendance_code = st.text_input("Enter the attendance code")

    # Check and mark attendance
    if st.button("Mark Attendance"):
        if name and student_id and attendance_code:
            # Check if already marked today
            today = datetime.now().strftime("%Y-%m-%d")
            if data[(data["ID"] == student_id) & (data["Attendance Date"] == today)].empty:
                # Append new record
                new_data = pd.DataFrame([[name, student_id, today]], columns=["Name", "ID", "Attendance Date"])
                data = pd.concat([data, new_data], ignore_index=True)
                save_data(data)
                st.success("Attendance marked successfully!")
            else:
                st.warning("Attendance already marked for today.")
        else:
            st.error("Please fill out all fields.")

    # Display attendance records
    if st.checkbox("Show Attendance Records"):
        st.write(data)

if __name__ == "__main__":
    main()
