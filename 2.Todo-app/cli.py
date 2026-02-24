import constraint as const
import functions

while True:
    action = input(const.prompt).strip()
    match action:
        case const.CMD.ADD:
            todo = input('enter a todo:') + '\n'
            functions.add_todo(todo)
        case const.CMD.EDIT:
            functions.edit_todos()
        case const.CMD.SHOW:
            functions.show_todos()
        case const.CMD.COMPLETE:
            functions.complete_todos()
        case const.CMD.EXIT:
            break
        case whatever:
            print('command not valid')
            break
