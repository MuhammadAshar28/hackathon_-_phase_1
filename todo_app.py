"""
Todo Console Application - Phase I Implementation

This is a simple, in-memory, console-based Todo application.
It allows a single user to manage tasks during a single runtime session.

Features included (Phase I only):
- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as complete or incomplete

Important:
- All data exists ONLY in memory
- No files, databases, or external services
- Data is lost when the application exits
"""

# -----------------------------
# Task Entity Definition
# -----------------------------

class Task:
    """
    Represents a single todo task.

    Each task contains:
    - id: Unique integer identifier
    - description: Task text entered by the user
    - completed: Boolean indicating completion status
    """

    def __init__(self, task_id, description):
        # Assign unique ID to the task
        self.id = task_id

        # Store task description
        self.description = description

        # Completion status (default is incomplete)
        self.completed = False

    def __str__(self):
        """
        Defines how a task is displayed when printed.
        Uses symbols to visually indicate completion state.
        """
        status = "✓" if self.completed else "○"
        return f"{self.id}. [{status}] {self.description}"


# -----------------------------
# Task Manager (Data Layer)
# -----------------------------

class TaskManager:
    """
    Manages all task-related data operations.

    Responsibilities:
    - Store tasks in memory
    - Generate unique task IDs
    - Add, retrieve, update, delete tasks
    - Modify task completion status
    """

    def __init__(self):
        # List to store all tasks in memory
        self.tasks = []

        # Sequential ID counter (never reused)
        self.next_id = 1

    def add_task(self, description):
        """
        Create a new task and store it in memory.
        """
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task_by_id(self, task_id):
        """
        Retrieve a task by its ID.
        Returns None if the task does not exist.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self):
        """
        Return the complete list of tasks.
        """
        return self.tasks

    def update_task(self, task_id, new_description):
        """
        Update the description of an existing task.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.description = new_description
            return True
        return False

    def delete_task(self, task_id):
        """
        Remove a task from memory.
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id):
        """
        Mark a task as completed.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_task_incomplete(self, task_id):
        """
        Mark a task as incomplete.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False


# -----------------------------
# CLI Menu Display
# -----------------------------

def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "=" * 40)
    print("TODO APPLICATION - MAIN MENU")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print("=" * 40)
    print("Choose an option (1-7): ", end="")


# -----------------------------
# Main Application Loop
# -----------------------------

def main():
    """
    Controls the overall flow of the application.

    - Displays menu
    - Reads user input
    - Routes control to appropriate handlers
    """
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input().strip()

        if is_valid_menu_choice(choice):
            if choice == "1":
                handle_add_task(task_manager)
            elif choice == "2":
                handle_view_tasks(task_manager)
            elif choice == "3":
                handle_update_task(task_manager)
            elif choice == "4":
                handle_delete_task(task_manager)
            elif choice == "5":
                handle_mark_complete(task_manager)
            elif choice == "6":
                handle_mark_incomplete(task_manager)
            elif choice == "7":
                print("\nThank you for using the Todo Application. Goodbye!")
                break
        else:
            print("\nInvalid choice. Please select a number between 1 and 7.")


# -----------------------------
# CLI Handler Functions
# -----------------------------

def handle_add_task(task_manager):
    """
    Handles adding a new task via user input.
    """
    print("\n--- ADD TASK ---")
    description = input("Enter task description: ").strip()

    if not is_valid_task_description(description):
        print("Error: Task description cannot be empty.")
        return

    task = task_manager.add_task(description)
    print(f"Task added successfully with ID {task.id}: {task.description}")


def handle_view_tasks(task_manager):
    """
    Displays all tasks to the user.
    """
    print("\n--- VIEW TASK LIST ---")
    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("Your task list is empty.")
        return

    print(f"Total tasks: {len(tasks)}")
    for task in tasks:
        print(task)


def handle_update_task(task_manager):
    """
    Allows the user to update an existing task.
    """
    print("\n--- UPDATE TASK ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty. Cannot update any tasks.")
        return

    try:
        task_id = int(input("Enter task ID to update: ").strip())
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    print(f"Current task: {task}")
    new_description = input("Enter new task description: ").strip()

    if not is_valid_task_description(new_description):
        print("Error: Task description cannot be empty.")
        return

    task_manager.update_task(task_id, new_description)
    print(f"Task {task_id} updated successfully.")


def handle_delete_task(task_manager):
    """
    Allows the user to delete a task.
    """
    print("\n--- DELETE TASK ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty. Cannot delete any tasks.")
        return

    try:
        task_id = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    print(f"Task to delete: {task}")
    confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()

    if confirm in ["y", "yes"]:
        task_manager.delete_task(task_id)
        print(f"Task {task_id} deleted successfully.")
    else:
        print("Task deletion cancelled.")


def handle_mark_complete(task_manager):
    """
    Marks a task as completed.
    """
    print("\n--- MARK TASK COMPLETE ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty.")
        return

    try:
        task_id = int(input("Enter task ID to mark as complete: ").strip())
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if task.completed:
        print("Task is already complete.")
        return

    task_manager.mark_task_complete(task_id)
    print(f"Task {task_id} marked as complete.")


def handle_mark_incomplete(task_manager):
    """
    Marks a task as incomplete.
    """
    print("\n--- MARK TASK INCOMPLETE ---")

    if not task_manager.get_all_tasks():
        print("Your task list is empty.")
        return

    try:
        task_id = int(input("Enter task ID to mark as incomplete: ").strip())
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if not task.completed:
        print("Task is already incomplete.")
        return

    task_manager.mark_task_incomplete(task_id)
    print(f"Task {task_id} marked as incomplete.")


# -----------------------------
# Validation Helpers
# -----------------------------

def is_valid_menu_choice(choice):
    """
    Validate menu input is a number between 1 and 7.
    """
    try:
        return 1 <= int(choice) <= 7
    except ValueError:
        return False


def is_valid_task_description(description):
    """
    Ensure task description is not empty.
    """
    return description.strip() != ""


# -----------------------------
# Application Entry Point
# -----------------------------

if __name__ == "__main__":
    main()
