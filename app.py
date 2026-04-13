"""
Task Manager Application
Version 1.0
"""
from datetime import datetime

class Task:
    def __init__(self, title):
            self.title = title
            self.completed = False
            self.deadline = None  # string date "YYYY-MM-DD"
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        deadline_info = f" [due: {self.deadline}]" if self.deadline else ""
        return f"[{status}] {self.title}{deadline_info}"
        
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
        
    def get_overdue_tasks(self, current_date=None):
        if current_date is None:
            current_date = datetime.now().strftime("%Y-%m-%d")
        
        overdue = []
        for task in self.tasks:
            if not task.completed and task.deadline:
                if task.deadline < current_date:
                    overdue.append(task)
        return overdue


def main():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    manager.add_task("Report", "2026-04-01")
    manager.add_task("Presentation", "2026-04-15")
    manager.add_task("Meeting notes", "2026-04-05")
    
    print("\nOverdue tasks:")
    for task in manager.get_overdue_tasks("2026-04-10"):
        print(f"  {task}")
    
    print("All tasks:")
    for task in manager.get_all_tasks():
        print(f"  {task}")
    
    print(f"\nTotal tasks: {manager.count_tasks()}")

if __name__ == "__main__":
    main()