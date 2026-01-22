import functions as f
import FreeSimpleGUI as gui


label = gui.Text("Add your to do item")
input_box = gui.InputText(key="input")
list_box = gui.Listbox(f.retrieve_items())
add_button = gui.Button("Add")
list_box = gui.Listbox(f.retrieve_items(),key="todo_items",enable_events=True,size=(45,10))
remove_button = gui.Button("Remove")
window = gui.Window("To Do App",
                    layout=[[label], [input_box, add_button],[list_box, remove_button]],
                    font=("Helvetica", 16))

while True:
    event, values = window.read()

    match event:
        case "Add":
            f.write_items("a",values['input'] + "\n")
            window["todo_items"].update(f.retrieve_items())
        case "Remove":
            to_do_list = f.retrieve_items()
            to_do_list.remove(values['todo_items'][0])
            f.write_items("w", to_do_list)
            window["todo_items"].update(f.retrieve_items())
        case gui.WIN_CLOSED:
            break

window.close()