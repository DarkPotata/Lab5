"""
Task Manager Application
Version 1.0
"""

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
        self.tags = []  # list of tags
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        tags_info = f" #{' #'.join(self.tags)}" if self.tags else ""
        return f"[{status}] {self.title}{tags_info}"
        
    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
    
    def has_tag(self, tag):
        return tag in self.tags


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, tags=None):
        task = Task(title)
        if tags:
            task.tags = tags
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self):
        return self.tasks
    
    def count_tasks(self):
        return len(self.tasks)
        
    def get_tasks_by_tag(self, tag):
        filtered_tasks = []
        for task in self.tasks:
            if task.has_tag(tag):
                filtered_tasks.append(task)
        return filtered_tasks
    
    def get_tasks_by_multiple_tags(self, tags_list):
        filtered_tasks = []
        for task in self.tasks:
            if any(task.has_tag(tag) for tag in tags_list):
                filtered_tasks.append(task)
        return filtered_tasks
        
    def get_tag_statistics(self):
        tag_count = {}
        for task in self.tasks:
            for tag in task.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count
    
    def get_most_used_tags(self, limit=5):
        stats = self.get_tag_statistics()
        sorted_tags = sorted(stats.items(), key=lambda x: x[1], reverse=True)
        return sorted_tags[:limit]


def main():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    
    print("All tasks:")
    for task in manager.get_all_tasks():
        print(f"  {task}")
        
    task1 = manager.add_task("Study Git", ["study", "programming"])
    task2 = manager.add_task("Go to gym", ["health", "sport"])
    task3 = manager.add_task("Read book", ["study", "leisure"])
    
    print("\nTag statistics:")
    stats = manager.get_tag_statistics()
    for tag, count in stats.items():
        print(f"  {tag}: {count} tasks")
    
    print("\nStudy tasks:")
    for task in manager.get_tasks_by_tag("study"):
        print(f"  {task}")
    
    print(f"\nTotal tasks: {manager.count_tasks()}")

if __name__ == "__main__":
    main()