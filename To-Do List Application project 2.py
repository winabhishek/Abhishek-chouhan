from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode
import sys

class ToDoApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.tasks = self.load_tasks()
        self.task_nodes = []
        self.create_task_nodes()

        
        self.setBackgroundColor(0.1, 0.1, 0.1)

        
        self.accept('escape', sys.exit)
        self.accept('a', self.add_task)
        self.accept('d', self.delete_task)
        self.accept('s', self.save_tasks)

    def create_task_nodes(self):
        for i, task in enumerate(self.tasks):
            text_node = TextNode(f'task_{i}')
            text_node.setText(task)
            text_node_path = self.aspect2d.attachNewNode(text_node)
            text_node_path.setScale(0.07)
            text_node_path.setPos(-0.9, 0, 0.8 - i * 0.2)
            self.task_nodes.append(text_node_path)

    def load_tasks(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as file:
                tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Tasks saved.")

    def add_task(self):
        task = input("Enter a new task: ")
        self.tasks.append(task)
        self.update_task_nodes()

    def delete_task(self):
        self.view_tasks()
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 0 < task_number <= len(self.tasks):
                self.tasks.pop(task_number - 1)
                self.update_task_nodes()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def update_task_nodes(self):
        for node in self.task_nodes:
            node.removeNode()
        self.task_nodes.clear()
        self.create_task_nodes()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

app = ToDoApp()
app.run()

