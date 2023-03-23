while True:
    user_action = input("What would you like to do? add, show, edit, complete? ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("What would you like to add?")

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Which todo would you like to edit? "))
            number -= 1
            new_todo = input("What would you like to change it to? ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("What do you want to mark as complete? "))
            todos.pop(number - 1)
        case 'exit':
            break

print('Bye!')
