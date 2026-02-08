import streamlit as st
import requests

st.title("Team Tasker Manager")

# Backend URL (Using Docker service name)
BACKEND_URL = "http://backend:8000/tasks"

title = st.text_input("Task Title")
desc = st.text_area("Description")

if st.button("Add Task"):
    response = requests.post(BACKEND_URL, json={"title": title, "description": desc})
    st.success(response.json().get("message"))

if st.sidebar.button("Refresh List"):
    data = requests.get(BACKEND_URL).json()
    for item in data:
        st.write(f"**{item['title']}**: {item['description']}")