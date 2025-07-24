import json

FILENAME = 'tasks.json'

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Add task
def add_task(tasks):
    task_text = input("Enter new task: ")
    tasks.append({'task': task_text, 'done': False})
    save_tasks(tasks)

# Mark task as done
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]['done'] = True
        save_tasks(tasks)
    except (IndexError, ValueError):
        print("Invalid input.")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
    except (IndexError, ValueError):
        print("Invalid input.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Show Tasks\n2. Add Task\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
