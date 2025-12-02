import streamlit as st

st.title("py-todo")

# Input field for adding tasks
task = st.text_input("Add a task")

# Initialize session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
    
# Button to add task
if st.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        task = ""

# Checkbox to show completed tasks
show_completed = st.checkbox("Show Completed Tasks", value=True)

if show_completed:
    tasks_to_display = st.session_state.tasks
else:
    tasks_to_display = [t for t in st.session_state.tasks if not t["completed"]]
    
# Display the list of tasks with checkboxes
st.write("### Tasks")

if tasks_to_display:
    for i, t in enumerate(tasks_to_display, start=1):
        tasks = t["task"]
        completed = t["completed"]
        t["completed"] = st.checkbox(f"{i}. {tasks}", value=completed)
else:
    st.write("No tasks available.")
    
# Button to clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]

# Button to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []