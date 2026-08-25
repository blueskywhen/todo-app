import functions
import FreeSimpleGUI as SG

label = SG.Text("Enter a To DO")
InputBox = SG.InputText(tooltip = "Enter todo")
addButton = SG.Button("Add")
window = SG.Window("My To Do App", layout = [[label], [InputBox,addButton]])
window.read()
window.close()
