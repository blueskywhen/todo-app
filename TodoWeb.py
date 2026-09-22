import functions
import streamlit as sl

todos = functions.get_todos()

sl.title("My Todo App")
for todo in todos:
    sl.checkbox(todo)

sl.text_input("", placeholder="Add a todo")