
user_prompt = "Type 'add'+ your to-do item, or type 'show', 'remove' or 'exit': "

while True:
    user_input = input(user_prompt).strip()
    if "add" in user_input:
        # to_do = input("Enter to do item: ") +"\n"
        with open("to_do_items.txt", "a") as file:
            file.writelines(user_input[4:]+"\n")
    elif user_input == "show":
        with open("to_do_items.txt", "r") as file:
            to_do_list = file.readlines()
            if not to_do_list:
                print("Nothing to do, please add an item")
            else:
                for index,item in enumerate(to_do_list):
                    print(f"{index+1}. {item.strip("\n")}")
    elif user_input == "remove":
        with open("to_do_items.txt", "r") as file:
            to_do_list = file.readlines()
        for index,item in enumerate(to_do_list):
            print(f"{index+1}. {item.strip("\n")}")
        item_to_delete = input("Which number do you want to remove?: ")
        if item_to_delete.isdigit() and 0 < int(item_to_delete) <= len(to_do_list):
            to_do_list.pop(int(item_to_delete)-1)
            with open("to_do_items.txt", "w") as file:
                file.writelines(to_do_list)
            print("Item removed successfully")
        else:
            print("Item not in list")
    elif user_input == "exit":
        print("Goodbye")
        break
    else:
        print("Invalid input")
