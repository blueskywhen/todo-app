import functions
import streamlit as sl

todos = functions.get_todos()

def addTodo():
    newTodo = sl.session_state["newTodo"] + "\n"
    todos.append(newTodo)
    functions.write_todos(todos)

sl.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.rerun()

sl.text_input("", placeholder="Add a todo",
              on_change=addTodo, key="newTodo")