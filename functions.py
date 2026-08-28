def writeToDos(todoListArg):
    with open("todos.txt", "w") as file:
        file.writelines(todoListArg)