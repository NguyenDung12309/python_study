prompt = """Enter command:
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
todos = []

def add_todo():
    todo = input('enter a todo:')
    todos.append(todo)

def edit_todos():
    to_do_id = int(input('enter a id to edit: '))
    todo = input('enter new todo:')
    todos[to_do_id - 1] = todo

def show_todos():
    for index, todo in enumerate(todos, start=1):
        print(f"{index}-{todo.title()}")

def complete_todos():
    to_do_id = int(input('enter a id to edit: '))
    complete = todos.pop(to_do_id - 1)
    print(f"completed: {complete}")
    print("Left todo:")
    show_todos()

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
        case EXIT:
            break
