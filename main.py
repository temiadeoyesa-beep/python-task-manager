import json # Module to handle data saving/loading
import random # 1. Import the random module

# Function to load existing tasks from a file
def load_tasks(filename="tasks.json"):
    """Reads tasks from a JSON file and returns a list of dictionaries."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If no file exists, return an empty list
        return []

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.json"):
    """Saves the current list of tasks to a JSON file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully!")

# Function to show a random tip
def show_random_tip():
    """Displays a random productivity tip to the user."""
    tips = [
        "Focus on one task at a time!",
        "Take a short break every 25 minutes.",
        "Clear your workspace to clear your mind.",
        "The best way to start is to just write the first line!"
    ]
    print(f"\n[Tip of the day]: {random.choice(tips)}")

# 3. Main program loop
def main():
    tasks = load_tasks() # Initialize list by loading from file
    show_random_tip() # 2. Call the tip function when the program starts
    
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "[x]" if task['done'] else "[ ]"
                print(f"{i}. {status} {task['name']}")
        elif choice == "2":
            new_name = input("Enter task name: ")
            tasks.append({"name": new_name, "done": False})
            print("Task added!")
        elif choice == "3":
            save_tasks(tasks) # Write data to file before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
