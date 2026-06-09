# 1. Define a function to load existing tasks from a file
def load_tasks():
    # Placeholder: returning a sample list to test the logic
    # Each task is a dictionary with a 'name' and 'status'
    return [{"name": "Finish Python Project", "done": False}]

# 2. Define a function to save tasks to a file
def save_tasks(tasks):
    print("Saving tasks to file...")

# 3. Main program loop
def main():
    tasks = load_tasks() # Initialize list
    
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            # Loop through the list to display tasks
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "[x]" if task['done'] else "[ ]"
                print(f"{i}. {status} {task['name']}")
        elif choice == "2":
            # Add a new dictionary to the list
            new_name = input("Enter task name: ")
            tasks.append({"name": new_name, "done": False})
            print("Task added!")
        elif choice == "3":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
if __name__ == "__main__":
    main()
