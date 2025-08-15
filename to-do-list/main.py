tasks= []

def menu():
    print ( "TO - DO LIST \n" \
    "1.- Add task \n" \
    "2.- View tasks\n" \
    "3.- Mark as done\n" \
    "4.- Delete task\n" \
    "5.- Exit \n")

def AddTask():
    newTask = input('Write your task: ')
    tasks.append({"task": newTask, "done": False})
    print(f"Task: '{newTask}' added!\n")

def ViewTasks():
    if not tasks:
        print("You don't have any tasks")
        return
    print ('\nYour tasks: ')
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}, {task['task']} [{status}]")

def MarkAsDone():
    ViewTasks()
    if not tasks:
        return
    try: 
        index = int(input("Enter task number to mark done: ")) - 1
        if 0<= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")

def deleteTask():
    ViewTasks()
    if not tasks:
        return
    try: 
        index = int(input("Enter task number to delete: ")) -1
        if 0<=index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number. ")        

while True: 
    menu()
    option = input("Choice an option (1-5) ")

    if option == '1': 
        AddTask()
    elif option == '2':
        ViewTasks()
    elif option == '3':
        MarkAsDone()
    elif option == '4':
        deleteTask()
    elif option == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
