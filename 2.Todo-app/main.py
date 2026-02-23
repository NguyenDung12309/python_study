prompt = 'Type add, show or exit:'

todos = []
while True:

    action = input(prompt).strip()
    match action:
        case 'add':
            todo = input('enter a todo:')
            todos.append(todo)
        case 'show':
            for index, todo in enumerate(todos, start=1):
                print(f"{index}-{todo.title()}")
        case 'edit':
            to_do_id = int(input('enter a id to edit: '))
            todo  = input('enter new todo:')
            todos[to_do_id - 1] = todo
        case 'exit':
            break
