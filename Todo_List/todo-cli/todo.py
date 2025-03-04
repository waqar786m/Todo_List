import streamlit as st
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from the JSON file"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        st.write("📂 No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            st.write(f"{index}. {task['task']} [{status}]")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        st.write(f"Task {task_number} marked as completed.")
    else:
        st.write(f"Invalid task number: {task_number}")

def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        st.write(f"Removed task: {removed_task['task']}")
    else:
        st.write("Invalid task number")

# Streamlit app
st.title("Todo List Manager")

# Custom Background Color
st.markdown(
    """
    <style>
        body {
            background-color: #e3f2fd; /* Light Blue */
        }
        .stApp {
            background-color: #e3f2fd; /* Light Blue */
        }
        h1 {
            text-align: center;
            color: #0d47a1; /* Dark Blue */
        }
    </style>
    """,
    unsafe_allow_html=True
)

task_input = st.text_input("Add a new task")
if st.button("Add Task"):
    add_task(task_input)
    st.success(f"Task added: {task_input}")

st.subheader("Your Tasks")
list_tasks()

task_to_complete = st.number_input("Task number to complete", min_value=1, step=1)
if st.button("Complete Task"):
    complete_task(task_to_complete)

task_to_remove = st.number_input("Task number to remove", min_value=1, step=1)
if st.button("Remove Task"):
    remove_task(task_to_remove)


# Footer (Centered)
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center; color: grey;'>💻 Created by Waqar Ahmed</h4>", 
    unsafe_allow_html=True
)
