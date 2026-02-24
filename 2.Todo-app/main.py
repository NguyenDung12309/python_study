prompt = """choose command number:
1. add
2. edit
3. show
4. complete
5. exit
"""

class CMD:
    ADD = '1'
    EDIT = '2'
    SHOW = '3'
    COMPLETE = '4'
    EXIT = '5'

def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines([todo.strip() + '\n' for todo in todos])

def add_todo():
    todos = get_todos()
    todo = input('enter a todo:') + '\n'
    todos.append(todo)
    write_todos(todos)

def edit_todos():
    try:
        todos = get_todos()
        todo_id = int(input('enter a id to edit: '))
        todo = input('enter new todo:') + '\n'
        todos[todo_id - 1] = todo
        write_todos(todos)
    except ValueError:
        print('invalid id')

def show_todos():
    todos = get_todos()

    for index, todo in enumerate(todos, start=1):
        print(f"{index}-{todo.title()}")

def complete_todos():
    try:
        todos = get_todos()
        todo_id = int(input('enter a id to edit: '))
        complete = todos.pop(todo_id - 1)
        write_todos(todos)
        print(f"completed: {todo_id}-{complete}")
        print("Left todo:")
        show_todos()
    except ValueError:
        print('invalid id')

while True:
    action = input(prompt).strip()
    match action:
        case CMD.ADD:
            add_todo()
        case CMD.EDIT:
            edit_todos()
        case CMD.SHOW:
            show_todos()
        case CMD.COMPLETE:
            complete_todos()
        case CMD.EXIT:
            break
        case whatever:
            print('command not valid')
            break
