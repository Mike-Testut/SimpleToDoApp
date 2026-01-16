
def retrieve_items(filepath="to_do_items.txt"):
    """ Retrieves items from a file"""
    with open(filepath, "r") as file:
        return file.readlines()

def write_items(action,item_to_add,filepath="to_do_items.txt"):
    """ Writes items to a file"""
    with open(filepath, action) as file:
        return file.writelines(item_to_add)

user_prompt = "Type 'add'+ your to-do item, or type 'show', 'remove' or 'exit': "
while True:
    user_input = input(user_prompt).strip()
    if "add" in user_input:
        write_items("a",user_input[4:]+"\n")
        print(f"Successfully added '{user_input[4:]}'")
    elif user_input == "show":
        to_do_list = retrieve_items()
        if not to_do_list:
            print("Nothing to do, please add an item")
        else:
            for index,item in enumerate(to_do_list):
                print(f"{index+1}. {item.strip("\n")}")
    elif user_input == "remove":
        to_do_list = retrieve_items()
        for index,item in enumerate(to_do_list):
            print(f"{index+1}. {item.strip("\n")}")
        item_to_delete = input("Which number do you want to remove?: ")
        if item_to_delete.isdigit() and 0 < int(item_to_delete) <= len(to_do_list):
            to_do_list.pop(int(item_to_delete)-1)
            write_items("w", to_do_list)
            print("Item removed successfully")
        else:
            print("Item not in list")
    elif user_input == "exit":
        print("Goodbye")
        break
    else:
        print("Invalid input")
