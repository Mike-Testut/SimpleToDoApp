from unittest import case

user_prompt = "Type 'add', 'show', 'remove' or 'exit': "

to_dos = []
while True:
    user_input = input(user_prompt).strip()
    match user_input:
        case "add":
            to_do = input("Enter to do item: ") +"\n"
            with open("to_do_items.txt", "a") as file:
                file.writelines(to_do)
        case "show":
            with open("to_do_items.txt", "r") as file:
                to_do_list = file.readlines()
            for index,item in enumerate(to_do_list):
                print(f"{index+1}. {item.strip("\n")}")
        case "remove":
            with open("to_do_items.txt", "r") as file:
                to_do_list = file.readlines()
            for index,item in enumerate(to_do_list):
                print(f"{index+1}. {item.strip("\n")}")
            item_to_delete = input("Which number do you want to remove?: ")
            to_do_list.pop(int(item_to_delete)-1)
            with open("to_do_items.txt", "w") as file:
                file.writelines(to_do_list)
        case "exit":
            print("Goodbye")
            break
