todos = []

while True:
    user_action = input("What would you like to do? ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("What would you like to add? ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Which todo would you like to edit? "))
            number -= 1
            new_todo = input("What would you like to change it to? ")
            todos[number] = new_todo
        case 'exit':
            break

print('Bye!')