import streamlit as st
import requests

# Define API base URL
API_URL = "http://localhost:8100/api/tasks"

def add_task(description, status):
    data = {"description": description, "status": status}
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        return True
    else:
        return False

def get_tasks():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def update_task(id, description, status):
    data = {"id": id, "description": description, "status": status}
    response = requests.put(API_URL + f"/{id}", json=data)
    if response.status_code == 200:
        return True
    else:
        st.error(f"Failed to update task {id}! Error: {response.text}")
        return False


def delete_task(id):
    response = requests.delete(API_URL + f"/{id}")
    if response.status_code == 200:
        return True
    else:
        return False

# Streamlit UI
st.title("Task Manager")

# Add Task Section
st.header("Add Task")
description = st.text_input("Description")
status = st.selectbox("Status", ["Pending", "Completed"])
if st.button("Add Task"):
    if add_task(description, status):
        st.success("Task added successfully!")
    else:
        st.error("Failed to add task!")

# View Tasks Section
st.header("Tasks")
tasks = get_tasks()
if tasks:
    for task in tasks:
        task_id = task['ID']
        task_description = st.text_input(f"Description for Task {task_id}", value=task['Description'])
        task_status = st.selectbox(f"Status for Task {task_id}", ["Pending", "Completed"], index=["Pending", "Completed"].index(task['Status']))
        
        if st.button(f"Update Task {task_id}"):
            if update_task(task_id, task_description, task_status):
                st.success(f"Task {task_id} updated successfully!")
            else:
                st.error(f"Failed to update task {task_id}!")
        
        if st.button(f"Delete Task {task_id}"):
            if delete_task(task_id):
                st.success(f"Task {task_id} deleted successfully!")
            else:
                st.error(f"Failed to delete task {task_id}!")
else:
    st.warning("No tasks available.")