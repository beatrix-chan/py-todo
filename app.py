import streamlit as st
import time

st.set_page_config(
    page_title="py-todo",
    layout="centered",
    menu_items={
        "About": """
        A simple Kanban-style to-do list application built with Python and Streamlit.
        
        This project is open source! Check it out on GitHub:
        https://github.com/beatrix-chan/py-todo
        
        This app is also under the MIT License.
        """,
        "Report a bug": "https://github.com/beatrix-chan/py-todo/issues",
        "Get help": "https://github.com/beatrix-chan/py-todo/discussions"
    }
)

st.title("py-todo")
st.link_button("GitHub Repository", "https://github.com/beatrix-chan/py-todo", help="@beatrix-chan/py-todo", type="primary", icon=":material/code:")

# Initialize session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if 'editing_index' not in st.session_state:
    st.session_state.editing_index = None

if 'context_menu' not in st.session_state:
    st.session_state.context_menu = None

# Input field for adding tasks using form for Enter key support
with st.form(key='task_form', clear_on_submit=True):
    task = st.text_input("Add a task")
    submit_button = st.form_submit_button("Add Task")
    
    if submit_button and task:
        st.session_state.tasks.append({"task": task, "status": "todo"})
        st.toast("Task added!", icon=":material/done_outline:")
        time.sleep(1)
        st.rerun()

# Kanban Board Layout
st.write("---")

# Create two columns for Kanban board
col_todo, col_completed = st.columns(2)

# Filter tasks by status
todo_tasks = [(i, t) for i, t in enumerate(st.session_state.tasks) if t.get("status", "todo") != "completed"]
completed_tasks = [(i, t) for i, t in enumerate(st.session_state.tasks) if t.get("status", "todo") == "completed"]

# To Do Column
with col_todo:
    st.markdown("## To Do")
    st.markdown(f"**{len(todo_tasks)} tasks**")
    
    if todo_tasks:
        for i, t in todo_tasks:
            with st.container():
                # Checkbox to mark as completed
                is_completed = st.checkbox(
                    t['task'],
                    value=False,
                    key=f"check_{i}"
                )
                
                if is_completed:
                    st.session_state.tasks[i]["status"] = "completed"
                    st.rerun()
    else:
        st.info("No tasks")

# Completed Column
with col_completed:
    st.markdown("## Completed")
    st.markdown(f"**{len(completed_tasks)} tasks**")
    
    if completed_tasks:
        for i, t in completed_tasks:
            with st.container():
                # Checkbox to unmark completion
                is_unchecked = not st.checkbox(
                    t['task'],
                    value=True,
                    key=f"check_completed_{i}"
                )
                
                st.balloons()
                
                if is_unchecked:
                    st.session_state.tasks[i]["status"] = "todo"
                    st.rerun()
    else:
        st.info("No tasks")

st.write("---")

# Action buttons at the bottom
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    # Button to clear completed tasks
    if st.button("Clear Completed Tasks", use_container_width=True):
        st.session_state.tasks = [t for t in st.session_state.tasks if t.get("status", "todo") != "completed"]
        st.toast("Completed tasks cleared!", icon=":material/done_outline:")
        time.sleep(1)
        st.rerun()

with btn_col2:
    # Button to clear all tasks
    if st.button("Clear All Tasks", use_container_width=True):
        st.session_state.tasks = []
        st.toast("All tasks cleared!", icon=":material/done_outline:")
        time.sleep(1)
        st.rerun()