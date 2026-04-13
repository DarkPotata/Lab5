"""
Task Manager Application
Version 1.0
"""

class Task:
    def __init__(self, title, priority="normal"):
        self.title = title
        self.completed = False
        self.priority = priority  # high, normal, low
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, priority="normal"):
        task = Task(title, priority)
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self):
        return self.tasks
    
    def count_tasks(self):
        return len(self.tasks)


def main():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    
    print("All tasks:")
    for task in manager.get_all_tasks():
        print(f"  {task}")
    
    print(f"\nTotal tasks: {manager.count_tasks()}")

if __name__ == "__main__":
    main()