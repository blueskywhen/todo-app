import functions
import FreeSimpleGUI as SG

label = SG.Text("Enter a To DO")
InputBox = SG.InputText(tooltip = "Enter todo", key = "todo")
addButton = SG.Button("Add")
listBox = SG.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45, 10])
editButton = SG.Button("Edit")
completeButton = SG.Button("Complete")
exitButton = SG.Button("Exit")
window = SG.Window("My To Do App",
                   layout = [[label], [InputBox,addButton],
                             [listBox, editButton, completeButton],
                             [exitButton]],font = ("Arial", 20))
while True:
    action, todo = window.read()
    match action:
        case "Add":
            newTodo = todo["todo"] + "\n"
            todolist = functions.get_todos()
            todolist.append(newTodo)
            functions.write_todos(todolist)
            window["todos"].update(values=todolist)
        case "Edit":
            todoToEdit = todo["todos"][0]
            newTodo = todo["todo"] + "\n"
            todolist = functions.get_todos()
            todolist[todolist.index(todoToEdit)] = newTodo
            functions.write_todos(todolist)
            window["todos"].update(values = todolist)
        case "Complete":
            todoCompleted = todo["todos"][0]
            todolist = functions.get_todos()
            todolist.remove(todoCompleted)
            functions.write_todos(todolist)
            window["todos"].update(values=todolist)
            window["todo"].update(value = "")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=todo["todos"][0])
        case SG.WIN_CLOSED:
            break
window.close()
