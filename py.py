from datetime import datetime

# -------------------------------
# Simple Command Line Task Notifier
# -------------------------------

def show_menu():
    """Display the main menu options."""
    print("\n--- Simple Command Line Task Notifier ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task(tasks):
    """Add a new task with time validation."""
    task_name = input("Enter task description: ").strip()
    task_time = input("Enter task time (HH:MM): ").strip()
    try:
        # Validate time format
        datetime.strptime(task_time, "%H:%M")
        tasks.append((task_name, task_time))
        print(f"✅ Task '{task_name}' scheduled at {task_time} added successfully.")
    except ValueError:
        print("❌ Invalid time format! Please use HH:MM (e.g., 09:30).")


def view_tasks(tasks):
    """View all tasks or alert if none exist."""
    if not tasks:
        print("⚠️ No tasks available.")
    else:
        print("\n--- Your Tasks ---")
        for idx, (name, time) in enumerate(tasks, start=1):
            print(f"{idx}. {name} at {time}")


def delete_task(tasks):
    """Delete a specific task by its number."""
    if not tasks:
        print("⚠️ No tasks to delete.")
        return

    view_tasks(tasks)
    try:
        num = int(input("Enter the number of the task to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed[0]}' at {removed[1]} deleted successfully.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    """Main program loop with error handling."""
    tasks = []
    running = True

    print("Welcome to Simple Command Line Task Notifier!")

    while running:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting Simple Command Line Task Notifier. Goodbye!")
            running = False
        else:
            print("❌ Invalid option. Please enter a number from 1 to 4.")


# Run the program safely
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Interrupted by user. Exiting gracefully...")
    finally:
        print("Task Notifier closed.")
