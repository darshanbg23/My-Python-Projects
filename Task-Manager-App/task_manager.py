import os

def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task, status = line.strip().rsplit(" | ", 1)
                tasks.append({"task": task, "completed": status == "Completed"})
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            file.write(f"{task['task']} | {status}\n")

def display_tasks(tasks):
    if tasks:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")
    else:
        print("No tasks available.")

def task_management_app():
    tasks = load_tasks()
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")
    
    reset_choice = input("Do you want to clear existing tasks? (yes/no): ").strip().lower()
    if reset_choice == "yes":
        tasks.clear()
        save_tasks(tasks)
    
    try:
        total_task = int(input("\nEnter how many tasks you want to add: "))
        for _ in range(total_task):
            task_name = input("Enter task: ").strip()
            if task_name:
                tasks.append({"task": task_name, "completed": False})
                save_tasks(tasks)
            else:
                print("Task cannot be empty! Try again.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    while True:
        try:
            print("\nOptions:")
            print("1 - Add Task")
            print("2 - Update Task")
            print("3 - Mark Task as Completed")
            print("4 - Delete Task")
            print("5 - View Tasks")
            print("6 - Exit")
            operation = int(input("Your choice: "))
            
            if operation == 1:
                add = input("Enter the task you want to add: ").strip()
                if add:
                    tasks.append({"task": add, "completed": False})
                    save_tasks(tasks)
                    print(f"Task '{add}' has been successfully added.")
                else:
                    print("Task cannot be empty!")
            
            elif operation == 2:
                if not tasks:
                    print("No tasks available to update!")
                    continue
                
                display_tasks(tasks)
                try:
                    task_num = int(input("Enter task number to update: ")) - 1
                    if 0 <= task_num < len(tasks):
                        new_task = input("Enter the new task: ").strip()
                        if new_task:
                            tasks[task_num]["task"] = new_task
                            save_tasks(tasks)
                            print("Task updated successfully.")
                        else:
                            print("Task cannot be empty!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
            
            elif operation == 3:
                if not tasks:
                    print("No tasks available to mark as completed!")
                    continue
                
                display_tasks(tasks)
                try:
                    task_num = int(input("Enter task number to mark as completed: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["completed"] = True
                        save_tasks(tasks)
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
            
            elif operation == 4:
                if not tasks:
                    print("No tasks available to delete!")
                    continue
                
                display_tasks(tasks)
                try:
                    task_num = int(input("Enter task number to delete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        removed_task = tasks.pop(task_num)
                        save_tasks(tasks)
                        print(f"Task '{removed_task['task']}' deleted successfully.")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
            
            elif operation == 5:
                display_tasks(tasks)
            
            elif operation == 6:
                print("Tasks saved successfully! Closing the program... Thank you for using the Task Management App!")
                break
            
            else:
                print("Invalid input! Please enter a number between 1 and 6.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

task_management_app()
