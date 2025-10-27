from datetime import datetime

#Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
print("Welcome to simple Command line Task notifier")
print("tasknot --a (add tasks) --v (view tasks) --d (delete tasks) --q (exit simple commandline task notifier)")
hourmin = "00:00"
format = "%H:%M"
try:
    #The tasks should be stored in a Python list
    list = []
#Core Features
#Add tasks
    

    newuser = [input("Add task "),input("Add Time (hh:mm) ")]
    newu = len(newuser) % 2 == 0
    print("newuser"+newuser[newu])
    dt_object = datetime.strptime(newuser[newu],format)
    list.extend(newuser)
#View tasks
    taskamount = 0

    for task in newuser:
        taskamount += taskamount
        tasks  = str(taskamount)+" "+ task 
        print("Task ",tasks)
#Delete tasks
    print("Which task number to delete")

except ValueError as e:
    print("Value Error enter correct value: {e}")
    print("Expected Format: {format}")
    print("Example: {hourmin}")
else:
    print("No exceptions occured")
finally:
    print("tasknot --a (add tasks) --v (view tasks) --d (delete tasks) --q (exit simple commandline task notifier)")



#Quit the application
#User Interaction

#Use input() to capture user selections and ensure proper input validation to handle invalid choices.
#Error Handling

#Implement error handling using try, except, else, and finally blocks to catch errors
#Alert the user if they provide invalid input
#Alert the user if there are no tasks to view
#Alert the user if they try to delete a task that doesn't exist
#Alert the user if they select an option on the main menu that doesn't exist
#Code Organization

#Organize your code into functions to improve clarity and maintainability. 
#Use descriptive function names and add comments/docstrings where necessary.
#Testing and Debugging

#Thoroughly test your application, considering edge cases such as empty lists and invalid input.
#Submission Guidelines:

#Ensure the code is ready to run and that all functionality, such as loops, conditionals, and functions, works as expected when executed. The goal is to have fully tested and functional code.


