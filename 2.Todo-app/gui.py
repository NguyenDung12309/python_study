import functions
import FreeSimpleGUI as sg
import constraint as const

label = sg.Text("type in todo")
input_box = sg.InputText(tooltip="type")
button_ok = sg.Button(const.CMD_GUI.ADD, bind_return_key=True)

window = sg.Window('Todo App', layout=[[label], [input_box, button_ok]])

while True:
    event, values = window.read()

    print(event, values)
    match event:
        case const.CMD_GUI.ADD:
            functions.add_todo(values[0])
        case sg.WIN_CLOSED:
            break

window.close()