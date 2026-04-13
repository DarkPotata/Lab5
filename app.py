"""
Task Manager Application
Version 1.0
"""

class Task:
    def __init__(self, title):
            self.title = title
            self.completed = False
            self.deadline = None  # string date "YYYY-MM-DD"
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"
        
    def set_deadline(self, date_string):
        self.deadline = date_string
        

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, deadline=None):
        task = Task(title)
        task.deadline = deadline
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self):
        return self.tasks
    
    def count_tasks(self):
        return len(self.tasks)
        
    def set_task_deadline(self, index, deadline):
        if 0 <= index < len(self.tasks):
            self.tasks[index].set_deadline(deadline)
            return True
        return False


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