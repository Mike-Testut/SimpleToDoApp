from unittest import case

user_prompt = "Type 'add', 'show', or 'exit': "

to_do_list = []

while True:
    user_input = input(user_prompt)
    match user_input:
        case "add":
            to_do = input("Enter to do item: ")
            to_do_list.append(to_do)
        case "show":
            print(to_do_list)
        case "exit":
            print("Goodbye")
            break
