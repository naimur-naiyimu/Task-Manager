import datetime
import uuid

class Task:
    tasks = {}
    task_count = 1

    def __init__(self, task, id=None):
        self.task = task
        self.created_time = datetime.datetime.now()
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False
        self.id = id or uuid.uuid4()
        Task.tasks[Task.task_count] = self

        Task.task_count += 1

    def update_task(self,task):
        self.task = task
        self.updated_time = datetime.datetime.now()

    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.datetime.now()

    def __str__ ( self ):
        return f"ID: {self.id}" \
               f"\nTask: {self.task}" \
               f"\nCreated Time: {self.created_time}" \
               f"\nUpdated Time: {self.updated_time}" \
               f"\nCompleted Time: {self.completed_time}" \
               f"\nTask Done: {self.task_done}\n"

    @classmethod
    def show_tasks(cls):
        for task_number,task in cls.tasks.items():
            print(task)

    @classmethod
    def show_tasks_with_No(cls):
        for task_number, task in cls.tasks.items ():
            if task.task_done == False:
                print(f"Task No - {task_number}\n{task}")

    @classmethod
    def update_task_by_No(cls, task_number,task):
        if task_number in cls.tasks:
            cls.tasks[task_number].update_task(task)
        else:
            print("Task not found")

    @classmethod
    def complete_task_by_No(cls, task_number):
        if task_number in cls.tasks:
            cls.tasks[task_number].complete_task()
        else:
            print("Task not found")

    @classmethod
    def show_incomplete_tasks(cls):
        have = False
        for task_number,task in cls.tasks.items():
            if task.task_done == False:
                print (task)
                have = True
        if not have:
            print ("All Tasks are Completed.")

    @classmethod
    def show_complete_tasks(cls):
        have = True
        for task_number,task in cls.tasks.items():
            if task.task_done == True:
                print (task)
                have = False
        if have:
            print("No task done yet.")

while True:
    print("\n1. Add New Task"
          "\n2. Show All Task"
          "\n3. Show Incomplete Task"
          "\n4. Show Complete Task"
          "\n5. Update Task"
          "\n6. Mark A Task Complete\n")

    option = int(input("Enter Option: "))

    if option == 1:
        Task(input("Enter New Task Name: "))
        print("Task Created Successfully\n")

    if option == 2:
        Task.show_tasks()

    if option == 3:
        Task.show_incomplete_tasks()

    if option == 4:
        Task.show_complete_tasks()

    if option == 5:
        print("\nSelect which task To Update\n")
        Task.show_tasks_with_No()
        no = int (input ("Enter task No: "))
        task = input("Enter New Task: ")

        Task.update_task_by_No(no, task)

    if option == 6:
        print ("\nSelect which task To Complete\n")
        Task.show_tasks_with_No()
        Task.complete_task_by_No(int(input("Enter task No: ")))
