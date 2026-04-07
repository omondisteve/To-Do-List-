import os
TASK_FILE = "tasks.txt"
def load_tasks():
    """Load tasks from a file."""
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks
def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    """Display all tasks with their statuses."""
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_task_complete(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        tasks[task_number - 1] = "[Completed] " + tasks[task_number - 1]
        print(f"Task {task_number} marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    """Main function to run the To-Do List app."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
