import functions
import FreeSimpleGUI as sg
import constraint as const

label = sg.Text("type in todo")
input_box = sg.InputText(tooltip="type", key=const.CMD_GUI.TODO, enable_events=True)
button_ok = sg.Button(const.CMD_GUI.ADD, disabled=True)
button_edit = sg.Button(const.CMD_GUI.EDIT, disabled=True)
button_complete = sg.Button(const.CMD_GUI.COMPLETE, disabled=True)
list_box = sg.Listbox(values=functions.get_todos(), enable_events=True, size=(45,10), key=const.CMD_GUI.TODOS)

buttons_column = [
    [button_edit],
    [button_complete]
]

layout = [
    [label],
    [input_box, button_ok],
    [list_box, sg.Column(buttons_column)],
]

window = sg.Window('Todo App', layout=layout)

while True:
    event, values = window.read()

    print(event, values)
    match event:
        case const.CMD_GUI.ADD:
            new_values = values[const.CMD_GUI.TODO].strip()
            functions.add_todo(new_values)
            window[const.CMD_GUI.TODOS].update(functions.get_todos())

        case const.CMD_GUI.TODOS:
            todo_to_edit = values[const.CMD_GUI.TODOS][0]
            window[const.CMD_GUI.TODO].update(todo_to_edit)
            window[const.CMD_GUI.EDIT].update(disabled=False)
            window[const.CMD_GUI.ADD].update(disabled=False)
            window[const.CMD_GUI.COMPLETE].update(disabled=False)

        case const.CMD_GUI.EDIT:
            todo_to_edit = values[const.CMD_GUI.TODOS][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            new_todo = values[const.CMD_GUI.TODO]
            functions.edit_todos(index, new_todo)
            window[const.CMD_GUI.TODOS].update(functions.get_todos())
            window[const.CMD_GUI.EDIT].update(disabled=True)

        case const.CMD_GUI.TODO:
            content = values[const.CMD_GUI.TODO].strip()
            window[const.CMD_GUI.ADD].update(disabled=(content == ""))
            window[const.CMD_GUI.EDIT].update(disabled=(content == ""))

        case const.CMD_GUI.COMPLETE:
            todo_to_complete = values[const.CMD_GUI.TODOS][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_complete)
            functions.complete_todos(index)
            window[const.CMD_GUI.TODOS].update(functions.get_todos())

        case sg.WIN_CLOSED:
            break

window.close()