import functions
import FreeSimpleGUI as SG

label = SG.Text("Enter a To DO")
InputBox = SG.InputText(tooltip = "Enter todo", key = "todo")
addButton = SG.Button("Add")
window = SG.Window("My To Do App",
                   layout = [[label], [InputBox,addButton]],
                   font = ("Arial", 20))
while True:
    action, todo = window.read()
    match action:
        case "Add":
            newTodo = todo["todo"] + "\n"
            todolist = functions.get_todos()
            todolist.append(newTodo)
            functions.write_todos(todolist)
        case SG.WIN_CLOSED:
            break
window.close()

window.close()
