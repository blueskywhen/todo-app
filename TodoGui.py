import functions
import FreeSimpleGUI as sg
import time

sg.theme("LightBlue3")
clock = sg.Text("", key = "Clock")
label = sg.Text("Enter a To DO")
InputBox = sg.InputText(tooltip = "Enter todo", key = "todo")
addButton = sg.Button("Add")
listBox = sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45, 10])
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("Exit")
window = sg.Window("My To Do App",
                   layout = [[clock], [label], [InputBox,addButton],
                             [listBox, editButton, completeButton],
                             [exitButton]],font = ("Arial", 20))
while True:
    action, todo = window.read(timeout=500)
    if action != sg.WIN_CLOSED:
        window["Clock"].update(value=time.strftime("%d-%m-%y %H:%M:%S"))
    match action:
        case "Add":
            newTodo = todo["todo"] + "\n"
            todolist = functions.get_todos()
            todolist.append(newTodo)
            functions.write_todos(todolist)
            window["todos"].update(values=todolist)
        case "Edit":
            try:
                todoToEdit = todo["todos"][0]
                newTodo = todo["todo"] + "\n"
                todolist = functions.get_todos()
                todolist[todolist.index(todoToEdit)] = newTodo
                functions.write_todos(todolist)
                window["todos"].update(values = todolist)
            except IndexError:
                sg.popup("Please select a todo first", font = ("Arial", 20))
        case "Complete":
            try:
                todoCompleted = todo["todos"][0]
                todolist = functions.get_todos()
                todolist.remove(todoCompleted)
                functions.write_todos(todolist)
                window["todos"].update(values=todolist)
                window["todo"].update(value = "")
            except IndexError:
                sg.popup("Please select a todo first", font=("Arial", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=todo["todos"][0])
        case sg.WIN_CLOSED:
            break
window.close()
