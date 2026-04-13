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
        priority_symbol = {"high": "🔴", "normal": "🟡", "low": "🟢"}.get(self.priority, "")
        return f"[{status}] {priority_symbol} {self.title}"


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
    
    def get_high_priority_tasks(self):
        high_priority = []
        for task in self.tasks:
            if task.priority == "high":
                high_priority.append(task)
        return high_priority
    
    def sort_by_priority(self):
        priority_order = {"high": 1, "normal": 2, "low": 3}
        self.tasks.sort(key=lambda t: priority_order.get(t.priority, 2))


def main():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    
    print("All tasks:")
    for task in manager.get_all_tasks():
        print(f"  {task}")
    
    manager.add_task("Urgent task", "high")
    manager.add_task("Important task", "high")
    
    print("\nHigh priority tasks:")
    for task in manager.get_high_priority_tasks():
        print(f"  {task}")
        
    manager.sort_by_priority()
    print("\nTasks sorted by priority:")
    for task in manager.get_all_tasks():
        print(f"  {task}")
    
    print(f"\nTotal tasks: {manager.count_tasks()}")

if __name__ == "__main__":
    main()