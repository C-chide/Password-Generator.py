def main():
    # Dynamic list acting as our database in volatile memory (RAM)
    todo_list = []
    
    print("========================================")
    print("   DecodeLabs - To-Do List Application  ")
    print("========================================\n")

    while True:
        # Display Menu
        print("\n--- MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            # OUTPUT: View Tasks
            print("\n--- YOUR TO-DO LIST ---")
            if not todo_list:
                print("Your to-do list is currently empty!")
            else:
                for idx, item in enumerate(todo_list, 1):
                    print(f"{idx}. {item['task']}")

        elif choice == "2":
            # INPUT: Data Entry
            task_name = input("\nEnter task description: ").strip()
            
            if task_name:
                # PROCESS: Logic / Data Modification
                # Store task as a dictionary inside our list collection
                task_entry = {"id": len(todo_list) + 1, "task": task_name}
                todo_list.append(task_entry)
                print(f"✓ Task '{task_name}' added successfully!")
            else:
                print("Task description cannot be empty.")

        elif choice == "3":
            # EXIT
            print("\nExiting To-Do List Application. Great work!")
            break

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()