from unittest import case

user_prompt = "Type 'add', 'show', 'remove' or 'exit': "

to_do_list = []
while True:
    user_input = input(user_prompt).strip()
    match user_input:
        case "add":
            to_do = input("Enter to do item: ")
            to_do_list.append(to_do)
        case "show":
            for index,item in enumerate(to_do_list):
                print(f"{index+1}. {item}")
        case "remove":
            for index,item in enumerate(to_do_list):
                print(f"{index+1}. {item}")
            item_to_delete = input("Which number do you want to remove?: ")
            to_do_list.pop(int(item_to_delete)-1)
        case "exit":
            print("Goodbye")
            break
