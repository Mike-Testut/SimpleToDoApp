
def retrieve_items(filepath="to_do_items.txt"):
    """ Retrieves items from a file"""
    with open(filepath, "r") as file:
        return file.readlines()

def write_items(action,item_to_add,filepath="to_do_items.txt"):
    """ Writes items to a file"""
    with open(filepath, action) as file:
        return file.writelines(item_to_add)
