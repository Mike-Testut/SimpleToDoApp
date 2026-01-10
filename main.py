from unittest import case

user_prompt = "Type 'add', 'show', 'remove' or 'exit': "

to_dos = []
while True:
    user_input = input(user_prompt).strip()
    match user_input:
        case "add":
            to_do = input("Enter to do item: ") +"\n"
            file = open("to_do_items.txt", "a")
            to_dos.append(to_do)
            file.writelines(to_do)
            file.close()
        case "show":
            file = open("to_do_items.txt", "r")
            to_do_list = file.readlines()
            for index,item in enumerate(to_do_list):
                print(f"{index+1}. {item}")
        case "remove":
            for index,item in enumerate(to_dos):
                print(f"{index+1}. {item}")
            item_to_delete = input("Which number do you want to remove?: ")
            to_dos.pop(int(item_to_delete)-1)
        case "exit":
            print("Goodbye")
            break
