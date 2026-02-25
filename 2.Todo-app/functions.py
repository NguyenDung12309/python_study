def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines([todo.strip() + '\n' for todo in todos])

def add_todo(todo):
    todos = get_todos()
    todos.append(todo)
    write_todos(todos)

def edit_todos(index, todo):
        todos = get_todos()
        todos[index] = todo
        write_todos(todos)

def show_todos():
    todos = get_todos()

    for index, todo in enumerate(todos):
        print(f"{index}-{todo.title()}")

def complete_todos(index):
        todos = get_todos()
        todos.pop(index)
        write_todos(todos)

print(__name__)
if __name__ == '__main__':
    print('im inside')