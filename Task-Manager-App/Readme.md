# Task Manager App

## Overview
The **Task Manager App** is a simple command-line Python application that helps users manage tasks efficiently. The app allows users to add, update, mark as completed, delete, and view tasks while ensuring data persistence using a text file.

## Features
✅ Add new tasks  
✅ Update existing tasks  
✅ Mark tasks as completed  
✅ Delete tasks  
✅ View all tasks with status indicators (✅ for completed, ❌ for pending)  
✅ Tasks are stored in `tasks.txt` for persistence, even after the program exits  

## How It Works
1. When you first run the program, it checks if `tasks.txt` exists. If not, it will be created automatically.
2. Users can add tasks, and they will be saved instantly in `tasks.txt`.
3. The program provides options to update, delete, mark tasks as completed, and view all tasks.
4. Tasks remain saved even after closing and reopening the application.

## Installation & Usage
### Prerequisites
- Python 3.x installed on your system

### Steps to Run the App
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/Task-Manager-App.git
   cd Task-Manager-App
   ```

2. **Run the Program**
   ```sh
   python task_manager.py
   ```

3. **Follow the On-Screen Instructions**
   - Enter tasks when prompted.
   - Choose options to update, mark as completed, delete, or view tasks.

## Notes
1. The `tasks.txt` file is **automatically created** when you add a task.
2. If you choose to reset tasks, the existing file content will be cleared.
3. The app runs in a loop until you choose to exit.

## Example Output
```
---- WELCOME TO THE TASK MANAGEMENT APP ----
Enter how many tasks you want to add: 3
Enter task: HTML Part
Enter task: CSS Part
Enter task: JS Part

Options:
1 - Add Task
2 - Update Task
3 - Mark Task as Completed
4 - Delete Task
5 - View Tasks
6 - Exit
Your choice: 5

Current Tasks:
1. HTML Part [❌]
2. CSS Part [❌]
3. JS Part [❌]
```

## License
This project is open-source and available under the [MIT License](LICENSE).

