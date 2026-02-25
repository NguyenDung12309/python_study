import constraint as const
import functions

while True:
    action = input(const.prompt).strip()
    match action:
        case const.CMD.ADD:
            todo = input('enter a todo:') + '\n'
            functions.add_todo(todo)
        case const.CMD.EDIT:
            try:
                todo_id = int(input('enter a id to edit: '))
                todo = input('enter new todo:') + '\n'
                functions.edit_todos(todo_id, todo)
            except ValueError:
                print('invalid input')
        case const.CMD.SHOW:
            functions.show_todos()
        case const.CMD.COMPLETE:
            try:
                todo_id = int(input('enter a id to edit: '))
                functions.complete_todos(todo_id)
            except ValueError:
                print('invalid input')
        case const.CMD.EXIT:
            break
        case whatever:
            print('command not valid')
            break
