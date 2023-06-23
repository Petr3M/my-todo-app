def get_todos(filepath="todos.txt"): #default arguments filepath="todos.txt"
    #with open('todos.txt', 'r') as file_local:
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"): #todos_arg, filepath are local variables and parameters
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")