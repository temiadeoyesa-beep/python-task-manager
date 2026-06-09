# 1. Define a function to load existing tasks from a file
def load_tasks():
    # Will use File Read here later
    print("Loading tasks...")
    return [] # Returns a list of tasks

# 2. Define a function to save tasks to a file
def save_tasks(tasks):
    # Will use File Write here later
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
            pass 
        elif choice == "2":
            # Add a new dictionary to the list
            pass
        elif choice == "3":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
if __name__ == "__main__":
    main()
