FILEPATH = "todos.txt"  # default file path


# from its own perspective, this file is a script; from the perspective of main, it is a module.
def get_todos(filepath=FILEPATH):  # default param
    """ Read a text file and return a list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # creates list of lines
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item's list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(" 'Functions.py' was successfully imported.")
