
tasks = []

def display_menu():
    print("To-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def mark_task_as_done():
    view_tasks()
    task_number = int(input("Enter the task number to mark as done: ")) - 1

    if 0 <= task_number < len(tasks):
        tasks[task_number]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def remove_task():
    view_tasks()
    task_number = int(input("Enter the task number to remove: ")) - 1

    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_as_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
