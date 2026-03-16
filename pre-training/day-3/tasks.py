import json
import sys
from datetime import datetime

class Task:
    def __init__(self, id, title, status="todo", created_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id         = data["id"],
            title      = data["title"],
            status     = data["status"],
            created_at = data["created_at"],
        )

class TaskManager:
    TASKS_FILE = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(TaskManager.TASKS_FILE, "r") as f:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            print("Unable to load tasks from the file.")
            return []

    def save_tasks(self):
        with open(TaskManager.TASKS_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title):
        task = Task(id=self.next_id(), title=title)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Added: [{task.id}] {task.title}")

    def delete_task(self, id):
        task = self.find_task(id)
        if task is None:
            print(f"No task with id '{id}'")
            return
        self.tasks.remove(task)
        self.save_tasks()
        print(f"Deleted: [{id}] {task.title}")

    def complete_task(self, id):
        task = self.find_task(id)
        if task is None:
            print(f"No task with id '{id}'")
            return

        task.status = "done"
        self.save_tasks()
        print(f"Marked done: [{task.id}] {task.title}")

    def list_tasks(self, filter=None):
        tasks = self.tasks
        if filter:
            tasks = [task for task in tasks if task.status == filter]
        if not tasks:
            print("No tasks found")
            return
        for task in tasks:
            print(f"{task.id:5} {task.status:8} {task.created_at:22} {task.title}")

    def next_id(self):
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def find_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

def main():
    manager = TaskManager()

    if len(sys.argv) < 2:
        print("Commands: add <title> | done <id> | delete <id> | list [--filter todo/done]")
        return
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:
            print("Commands: add <title> | done <id> | delete <id>")
            return
        manager.add_task(sys.argv[2])
        manager.list_tasks()
    elif command == "done":
        if len(sys.argv) < 3:
            print("Commands: add <title> | done <id> | delete <id>")
            return
        try:
            manager.complete_task(int(sys.argv[2]))
        except (IndexError, ValueError):
            print("Please provide a valid task id.")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Commands: add <title> | done <id> | delete <id>")
            return
        try:
            manager.delete_task(int(sys.argv[2]))
            manager.list_tasks()
        except (IndexError, ValueError):
            print("Please provide a valid task id.")
    elif command == "list":
        filter = None
        if "--filter" in sys.argv:
            index = sys.argv.index("--filter")
            try:
                filter = sys.argv[index + 1]
            except IndexError:
                print("Please provide a valid filter.")
                return
        manager.list_tasks(filter=filter)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()