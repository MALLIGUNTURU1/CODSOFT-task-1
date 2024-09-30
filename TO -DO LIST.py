tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Mark a Task as Complete")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✖"
            print(f"{index}. {task['task']} [{status}]")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def update_task():
    view_tasks()
    task_number = int(input("Enter the task number to update: "))
    if task_number <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_number - 1]["task"] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_task_complete():
    view_tasks()
    task_number = int(input("Enter the task number to mark as complete: "))
    if task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_complete()
        elif choice == '6':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
