class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
            return []

    def save_tasks(self):
        try:
            with open(self.filename, "w") as file:
                for task in self.tasks:
                    file.write(f"{task}\n")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_index):
        try:
            self.tasks.pop(task_index)
            self.save_tasks()
        except IndexError:
            print("Task index is out of range.")

    def view_tasks(self):
        if not self.tasks:
            print("Your task list is empty.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}: {task}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            task_manager.add_task(task)
            print("Task added.")
        elif choice == "2":
            task_manager.view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                task_manager.remove_task(task_index)
                print("Task removed.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            task_manager.view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
