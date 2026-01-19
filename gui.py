import functions as f
import FreeSimpleGUI as gui


label = gui.Text("Add your to do item")
input_box = gui.InputText()
add_button = gui.Button("Add")


window = gui.Window("To Do App",
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 16))

while True:
    event, values = window.read()
    match event:
        case "Add":
            f.write_items("a",values[0] + "\n")


window.close()