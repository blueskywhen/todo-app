import functions
import streamlit as sl

todos = functions.get_todos()

def addTodo():
    newTodo = sl.session_state["newTodo"] + "\n"
    todos.append(newTodo)
    functions.write_todos(todos)

sl.title("My Todo App")
for todo in todos:
    sl.checkbox(todo)

sl.text_input("", placeholder="Add a todo",
              on_change=addTodo, key="newTodo")