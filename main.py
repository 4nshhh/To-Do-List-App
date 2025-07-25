# Daily To-Do List App (Text File Version)

# Goal: Command-line app to manage your daily tasks.

# Features to Include:
# > Add task
# > View all tasks
# > Mark task as done
# > Delete task
# > Save tasks in a text file

def add_task():
    # view_tasks()
    while True:
        print(task := input("Enter task (0 for none): "))
        if task == '0':
            break
        with open("tasks.txt", "a", newline='') as f:
            f.write(f"[ ] {task}\n")
    print("Tasks Added Successfully!")
    view_tasks()

def view_tasks():
    print("\n========== Your To Do List ===========")
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        i = 1
        tasks = [task.strip() for task in tasks]
        for task in tasks:
            print(f"{i}. {task}")
            i+=1

def mark_completed_task():
    view_tasks()
    print(no := int(input("Enter the task number to mark as done: ")))
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        if '[ ]' in tasks[no-1]:
            tasks[no-1] = tasks[no-1].replace("[ ]","[*]")
    with open("tasks.txt", "w") as f:
        f.writelines(tasks)
    updated_list()

def delete_task():
    view_tasks()
    print(no := int(input("Enter the task number to delete : ")))
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        tasks.remove(tasks[no-1])
        print("Successfully removed!")
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task)
    updated_list()
    

def updated_list():
    print("\n========== Updated To Do List ===========")
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        i = 1
        tasks = [task.strip() for task in tasks]
        for task in tasks:
            print(f"{i}. {task}")
            i+=1

while True:
    print("\n========== TO-DO LIST MENU ==========")
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print(choice := int(input("> Choose an option(1-5): ")))

    match choice:
        case 1:
            add_task()
        case 2:
            view_tasks()
        case 3:
            mark_completed_task()
        case 4:
            delete_task()
        case 5:
            print("Thank you for coming!")
            break
        case _:
            print("Invalid Option!")