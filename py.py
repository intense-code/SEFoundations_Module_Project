import json
import os
import time
import threading
from datetime import datetime

# -------------------------------
# Simple Command Line Task Notifier with Persistence + Alerts
# -------------------------------

TASKS_FILE = "tasks.json"
ALERT_INTERVAL = 60  # check every 60 seconds


def load_tasks():
    """Load tasks from a JSON file if it exists."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("⚠️ Corrupted task file detected. Starting fresh.")
    return []


def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


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
        tasks.append({"task": task_name, "time": task_time, "notified": False})
        save_tasks(tasks)
        print(f"✅ Task '{task_name}' scheduled at {task_time} added successfully.")
    except ValueError:
        print("❌ Invalid time format! Please use HH:MM (e.g., 09:30).")


def view_tasks(tasks):
    """View all tasks or alert if none exist."""
    if not tasks:
        print("⚠️ No tasks available.")
    else:
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(tasks, start=1):
            status = "✅ Done" if task.get("notified") else "🕒 Pending"
            print(f"{idx}. {task['task']} at {task['time']} [{status}]")


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
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['task']}' at {removed['time']} deleted successfully.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def notify_tasks(tasks):
    """Background thread that checks for due tasks."""
    while True:
        now = datetime.now().strftime("%H:%M")
        for task in tasks:
            if not task.get("notified") and task["time"] == now:
                print("\n🔔 ALERT! It's time for your task:")
                print(f"➡️ {task['task']} (scheduled at {task['time']})")
                print("\a")  # beep sound (works in most terminals)
                task["notified"] = True
                save_tasks(tasks)
        time.sleep(ALERT_INTERVAL)


def main():
    """Main program loop with background notification thread."""
    tasks = load_tasks()
    print("Welcome to Simple Command Line Task Notifier with Alerts!")

    # Start the background notifier
    threading.Thread(target=notify_tasks, args=(tasks,), daemon=True).start()

    running = True
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
