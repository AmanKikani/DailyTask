import streamlit as st
import datetime

def main():
    st.title("Daily Task Tracker")

    # Set the current date
    today = datetime.date.today()
    st.header(f"Tasks for {today.strftime('%A, %B %d, %Y')}")

    # Load tasks from session state or initialize
    if "tasks" not in st.session_state:
        st.session_state.tasks = [
            {"task": "Morning exercise", "completed": False},
            {"task": "Check emails", "completed": False},
            {"task": "Team meeting at 10 AM", "completed": False},
            {"task": "Work on project report", "completed": False},
            {"task": "Evening walk", "completed": False},
        ]

    # Display tasks with checkboxes
    for i, task in enumerate(st.session_state.tasks):
        task_name = task["task"]
        completed = st.checkbox(task_name, value=task["completed"], key=f"task_{i}")
        st.session_state.tasks[i]["completed"] = completed

    # Button to reset tasks
    if st.button("Reset Tasks"):
        for task in st.session_state.tasks:
            task["completed"] = False

    # Add a new task
    st.subheader("Add a new task")
    new_task = st.text_input("Task description")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success(f"Task '{new_task}' added!")

if __name__ == "__main__":
    main()
