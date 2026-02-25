import FreeSimpleGUI as sg
import zip_creator
label_1 =  sg.Text("choose file")
label_2 = sg.Text("choose folder")
input_1 = sg.Input(key="path1")
input_2 = sg.Input(key="path2")
button_choose_1 = sg.FilesBrowse()
button_choose_2 = sg.FolderBrowse()
button_compress = sg.Button("compress", key="compress")

layout = [
        [label_1, input_1,button_choose_1],
        [label_2, input_2,button_choose_2],
        [button_compress]
    ]

app = sg.Window(
    "Compress App",
    layout=layout
)

while True:
    event, values = app.Read()

    match event:
        case 'compress':
            print(event, values)
            zip_creator.zip_creator(values["path1"], values["path2"])
        case sg.WIN_CLOSED:
            break

app.close()