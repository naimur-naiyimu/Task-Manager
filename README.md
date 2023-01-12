# Task-Manager

##### I create a task management system that allows a user to add new tasks, view all tasks, view incomplete tasks, view completed tasks, update tasks, and mark tasks as complete.

##### This code defines a class called Task that represents a single task in a task management system. The Task class has several methods that allow the user to perform different actions on tasks, such as adding new tasks, viewing all tasks, viewing incomplete tasks, viewing completed tasks, updating tasks, and marking tasks as complete.
##### The __init__ method is the constructor of the Task class, and it is called every time a new Task object is created. This method initializes the task's attributes, such as task, created_time, and task_done, and stores the new task in a dictionary called tasks.
The update_task method updates the task's name, and the complete_task method marks the task as completed. The __str__ method returns a string representation of the task that includes its ID, name, and other attributes.
##### The show_tasks method is a class method that prints all tasks in the tasks dictionary. The show_tasks_with_No method is also a class method that prints all tasks along with their task number.
##### The update_task_by_No and complete_task_by_No methods are class methods that allow the user to update or mark a task as complete by specifying the task's number.
##### Finally, the show_incomplete_tasks and show_complete_tasks methods are class methods that print all incomplete tasks or all completed tasks, respectively.
##### There is also a while loop at the end of the code that presents a menu to the user and waits for their input. Based on the user's input, the code calls the appropriate method to perform the selected action.<h4>
