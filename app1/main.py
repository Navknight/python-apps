while True:
    user_action = input(
        "What would you like to do? add, show, edit, complete? ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("What would you like to add?") + "\n"

            with open('./todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            if len(todos) == 0:
                print("Add todos to get started! ")

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Which todo would you like to edit? "))
            number -= 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("What would you like to change it to? ")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("What do you want to mark as complete? ")) - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            while (number >= len(todos) or number < 0):
                number = int(input("Enter a valid number! "))
                number -= 1

            todos.pop(number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

print('Bye!')
