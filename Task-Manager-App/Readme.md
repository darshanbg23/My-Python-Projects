# Task Manager App

## Overview
This is a simple command-line-based **Task Management Application** built using Python. It allows users to add, update, delete, and mark tasks as completed. Tasks are stored in a `tasks.txt` file, which is automatically created when a new task is added.

## Features
- Add new tasks
- Update existing tasks
- Mark tasks as completed
- Delete tasks
- View all tasks with their statuses (Pending/Completed)
- Data is saved automatically in `tasks.txt`

## How It Works
### Task Storage
- Tasks are stored in a file named `tasks.txt`.
- Each task is stored in the format: `Task Description | Status`.
- Status can be **Pending** or **Completed**.

### User Actions
1. **Adding a Task**
   - Users can add multiple tasks at once during startup.
   - Tasks can be added later via the menu option.

2. **Updating a Task**
   - Users can update the description of an existing task.

3. **Marking a Task as Completed**
   - Users can mark a specific task as completed.

4. **Deleting a Task**
   - Users can remove a task from the list.

5. **Viewing Tasks**
   - Displays all tasks with their current statuses.

6. **Exit**
   - Saves tasks before exiting the program.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Task-Manager-App.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Task-Manager-App
   ```
3. Run the Python script:
   ```bash
   python task_manager.py
   ```

## Example Output
```
---- WELCOME TO THE TASK MANAGEMENT APP ----
Do you want to clear existing tasks? (yes/no): no

Enter how many tasks you want to add: 2
Enter task: Complete Python project
Enter task: Submit assignment

Options:
1 - Add Task
2 - Update Task
3 - Mark Task as Completed
4 - Delete Task
5 - View Tasks
6 - Exit
Your choice: 5

Current Tasks:
1. Complete Python project [❌]
2. Submit assignment [❌]
```

## Notes
- If `tasks.txt` does not exist, it is created automatically when a task is added.
- Data is saved after each operation to ensure persistence.
- The application is entirely CLI-based.

## License
This project is open-source and free to use under the MIT License.
