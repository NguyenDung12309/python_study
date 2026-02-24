import functions

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

while True:
    action = input(prompt).strip()
    match action:
        case CMD.ADD:
            functions.add_todo()
        case CMD.EDIT:
            functions.edit_todos()
        case CMD.SHOW:
            functions.show_todos()
        case CMD.COMPLETE:
            functions.complete_todos()
        case CMD.EXIT:
            break
        case whatever:
            print('command not valid')
            break
