from functions import get_todos, write_todos

while True:
    user_action = input(
        "What would you like to do? add, show, edit, complete? ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        if len(todos) == 0:
            print("Add todos to get started! ")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("What would you like to change it to? ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Enter a valid command! ")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number -= 1

            todos = get_todos()

            todos.pop(number)

            write_todos(todos)
        except IndexError:
            print("Enter a valif number! ")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("enter a valid command! ")

print('Bye!')
