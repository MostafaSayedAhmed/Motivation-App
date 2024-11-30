"""
Author      : Mostafa Sayed Ahmed Taha
Description : Motivation Application to track streaks for a single task.
Date        : 11/17/2024
Future Work : Add Notifictaion

General Notes:
    - Opt: Indicates areas for potential optimization.
    - adv/feature/: Denotes future improvements or features.
"""

import json   # json package used to handle data and manipulate it
import time   # time package (Unused)
import datetime  # Module to handle date and time operations
from PyQt5.QtGui import QIcon  # (Unused) Allows customization of the window icon

import themes    # Python file include themes (Maybe replaced later with JSON file contain all themes)
import sys       # Module for handling script/executable-specific operations and GUI event loop
import os        # Module for working with file system paths
from PyQt5.QtWidgets import QApplication,QMessageBox, QMainWindow
# QApplication: Manages the main application loop
# QMainWindow : Provides the framework for creating GUI windows
# QMessageBox : Used to produce popup window for streak calculation and add/remove task operations

from PyQt5.QtCore import QStringListModel,QEvent  # Used to populate a list view widget with data
from PyQt5 import uic  # Connects the GUI layout (from Qt Designer) with the Python code dynamically

# Include taskmanager task which is used to manage task effectively in streak calculation operation
from taskmanager import *

"""
MainWindow Class:
Purpose    : used to ease dealing with GUI windows and customization of the GUI
Attributes : None
Methods    : None
"""
class MainWindow(QMainWindow):
    def __init__(self,path):
        super().__init__()
        uic.loadUi(path, self)  # Load main window UI


# Popup Window this block of code is repeated when ever popup window is needed (Encapsulation using function)
def popupWindow(popupWindowTitle="",messageStr=""):
    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setWindowTitle(popupWindowTitle)
    message.setText(messageStr)
    message.exec_()
"""
back_fun Method:
Purpose    : used to return from task management window to the main window
Parameters : 
    - windowObj : objcet instance of MainWindow class. Passed to display the main window
Returns    : None
"""
def back_fun(windowObj):
    display_gui(windowObj)

"""
add_fun Method:
Purpose    : add task to task list of task manager using name and description provided by the user
Parameters : 
    - windowObj : object instance of MainWindow class. Passed to display the main window elements
Returns    : None
"""
def add_fun(windowObj):
    # Initialize list of tasks as empty one
    taskLists = []
    # Enter Task List at the beginning to be displayed in list view
    taskLists.append("Task List : \n")
    # open JSON file to retrieve read list to add task to them and check if it already exists or not
    with open(cur_path + "\\backend\\database.json", 'r+') as file:
        # This block of try and except is repeated whenever a json.load() is done to avoid error in case of emply
        # JSON file
        try:
            read_list = json.load(file)
        except Exception as e:
            read_list = []

    # Append task element from list to task list in order to perform the manipulation of tasks in tasklists variable
    for i in [read_list[i]["Name"] + '\n' for i in range(0, len(read_list))]:
        taskLists.append(i)
    # Retrieve task Name from text line of GUI
    newTaskName = windowObj.name.text()
    # Retrieve task Description from text edit of GUI
    newTaskDescription = windowObj.description.toPlainText()
    # Check whether task name is already existed or not if so the new task cannot be added otherwise add the task
    if newTaskName + "\n" in [read_list[i]["Name"] + '\n' for i in range(0, len(read_list))]:
        print("Already Existing Task")
        # Popup Window
        popupWindow("Notification","Already Existing Task")
        return
    # Check whether the user entered name or not if not, notify him to enter valid task name
    elif str(newTaskName) == "":
        # Popup Window
        popupWindow("Notification", "Enter Valid Task Name")
        return
    # Valid new task name is entered and task will be added to the task list
    else:
        taskLists.append(newTaskName)
        with open(cur_path + "\\backend\\database.json", 'r+') as file:
            add_task(file, newTaskName, newTaskDescription)
        windowObj.taskList.setModel(QStringListModel(taskLists))
        # Popup Window
        popupWindow("Notification", "Task Added Successfully")

"""
remove_fun Method:
Purpose    : remove task from task list of task manager
Parameters : 
    - windowObj : object instance of MainWindow class. Passed to display the main window elements
Returns    : None
"""
def remove_fun(windowObj):
    # Retrieve number of selected item to be able to use it in removing task by its number
    try:
        taskNum = windowObj.taskList.selectionModel().selectedIndexes()[0].row()
    except Exception as e:
        # Error occur if no task is selected this is handled in this section
        # Popup Window
        popupWindow("Notification","Select the Task first")
        return
    if taskNum == 0:
        # the first index is for task list string which isn't a valid task so if selected by user it will notify him
        # to select valid task Popup Window
        popupWindow("Notification","Select a Real Task")
        return
    else:
        # If valid task is selected removing operation commence
        with open(cur_path + "\\backend\\database.json", 'r+') as file:
            readData = json.load(file)
            # Note : taskNum-1 as the zero index of this list isn't the first task but task list string which isn't a
            # valid task as forementioned
            taskNum = readData[taskNum-1]["Number"]
            # Removing task by number
            remove_task(file, taskNum)
        # Updating list view for task manager window
        taskLists = []
        taskLists.append("Task List : \n")
        with open(cur_path + "\\backend\\database.json", 'r+') as file:
            read_list = json.load(file)
        for i in [read_list[i]["Name"] + '\n' for i in range(0, len(read_list))]:
            taskLists.append(i)
        windowObj.taskList.setModel(QStringListModel(taskLists))

#######################################This Block of code need improvements#############################################
# Determine the absolute path of the script or executable file
if getattr(sys, 'frozen', False):
    # If running as an executable (e.g., created using PyInstaller)
    current_file_path = os.path.dirname(sys.executable)
else:
    # If running as a script
    current_file_path = os.path.dirname(os.path.abspath(__file__))

# Define paths for application files
cur_path = current_file_path + "\\"
backend_path = cur_path + "backend"

# Initialize database and backup files
try:
    # Create database and backup files if they don't exist
    open(backend_path + "\\database.json", 'x')
except FileExistsError:
    # If files already exist, open them for the appropriate operations
    pass
########################################################################################################################
"""
get_obj_methods
Purpose     : Display all methods available for a given object (used for debugging/testing).
Parameters  :
    - obj: The object whose methods are to be listed.
Returns     : None
"""
def get_obj_methods(obj):
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    print(methods)

"""
data_integrity_check method:
Purpose    : main goal of function is to check integrity of data in log list of given task
Parameters :
    - taskObj : current selected task in combo box 
Return     : None
"""
def data_integrity_check(taskObj):
    # Check Data Integrity with taskObj log list file
    datalist = taskObj.logList
    # Remove the duplication
    dataSet = set(datalist)
    datalist = list(dataSet)
    # Check the format of date whether it is valid or not
    for i in range(0, len(datalist)):
        # Replace / , : , ; in date to - which is suitable format
        for j in ['/', ':', ';']:
                datalist[i] = datalist[i].replace(j, '-')
        # Convert each element in log list to list of strings to test each one of day and months separately
        dateStringList = datalist[i].split('-')
        # If months are September or November or March or June then maximum number of days is 30
        if int(dateStringList[1]) in [3, 6, 9, 11]:
            if 0 < int(dateStringList[0]) <= 30:
                pass
            else:
                # Replace incorrect dates with spaces
                datalist[i] = "\n"
        # Days in other months range from 1 to 31
        elif int(dateStringList[1]) in [1, 4, 5, 7, 8, 10, 12]:
            if 0 < int(dateStringList[0]) <= 31:
                pass
            else:
                # Replace incorrect dates with spaces
                datalist[i] = "\n"
        # If months are Feburary then maximum number of days is 28 if it is not leap year if it is leap year then 29
        elif int(dateStringList[1]) == 2:
            # Check whether it is leap year or not
            if int(dateStringList[2]) % 4 == 0:
                if 0 < int(dateStringList[0]) <= 29:
                    pass
                else:
                    # Replace incorrect dates with spaces
                    datalist[i] = "\n"
            else:
                if 0 < int(dateStringList[0]) <= 28:
                    pass
                else:
                    # Replace incorrect dates with spaces
                    datalist[i] = "\n"
        # if months other than 1,2,3,4,5,6,7,8,9,10,11,12 are used discard this date.
        else:
            datalist[i] = "\n"

        # Add end line character to each date
        if datalist[i][-1] != "\n":
            datalist[i] = datalist[i] + "\n"
    # Remove all empty elements whether there was error or it is wrongly formatted
    try:
        datalist.remove("\n")
    except ValueError:
        pass
    # Sorting dates in the list by doing :
    # Initializing empty list
    templist = []
    # first reverse format for each date from day-month-year to year-month-day to be order to perform sorting correctly
    for i in range(0,len(datalist)):
        Interlist = datalist[i].split('-')[-1::-1]
        Interstring = f"{Interlist[0]}-{Interlist[1]}-{Interlist[2]}"
        templist.append(Interstring)
    # Sort list ascendingly
    templist.sort()
    # Perform revesrse formating again to retrieve the original format
    OutputList = []
    for i in range(0,len(templist)):
        Interlist = templist[i].split('-')[-1::-1]
        Interstring = f"{Interlist[0]}-{Interlist[1]}-{Interlist[2]}"
        OutputList.append(Interstring)
    # Finalizing the list that will be updating the original log list
    datalist = OutputList
    taskObj.logList = datalist

"""
log_button_action
Purpose     : Perform operations when the "Log In" button is clicked:
              - Log today's date
              - Calculate and update the streak
Parameters  : None
Returns     : None
"""
def log_button_action():
    global window
    # Retrieve index of current item selected in combo box
    taskNum = window.taskSelector.currentIndex()
    # Retrieve task from JSON file by number
    with open(backend_path + "\\database.json", 'r+') as file:
        try:
            taskObj = retrieve_by_Num(file,taskNum)
        except Exception as e:
            print("Error Not Added Task")
            # Popup Window
            popupWindow("Empty Task List","No Tasks Found")
            return
    # Perform Data Integrity Check for current selected item
    data_integrity_check(taskObj)
    # Create TaskManager object to perform streak calculations
    login = TaskManager(backend_path)
    login.streak_calculate(taskObj)
    # Update GUI elements
    streakNumber = taskObj.get_count()
    window.countDisplay.display(streakNumber)
    window.countDisplay.setStyleSheet(f"color:hsl({((streakNumber)*10)%360},100%,50%);")
    window.logList.setModel(QStringListModel(["Log Dates : ", "".join(taskObj.logList)]))
    # Popup Window
    popupWindow("Log In Notification","You logged in successfully!")

"""
get_obj_methods
Purpose     : Display all methods available for a given object (used for debugging/testing).
Parameters  :
    - obj: The object whose methods are to be listed.
Returns     : None
"""
def get_obj_methods(obj):
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    print(methods)


"""
add_remove_button_action Method
Purpose     : Switch window from Main Window to Task Manager Window
Parameters  : None
Returns     : None
"""
def add_remove_button_action():
    global window,app
    TaskHandlerWin = window
    uic.loadUi(cur_path + "GUI\\TaskHander.ui", TaskHandlerWin)
    # TaskHandlerWin = window.second_window
    tasklists = []
    tasklists.append("Task List : \n")
    with open(cur_path + "\\backend\\database.json",'r+') as file:
        try:
            read_list = json.load(file)
        except Exception as e:
            read_list = []
    for i in [read_list[i]["Name"] + '\n' for i in range(0,len(read_list))]:
        tasklists.append(i)

    TaskHandlerWin.taskList.setModel(QStringListModel(tasklists))  # Populate log list
    TaskHandlerWin.addTask.clicked.connect(lambda: add_fun(TaskHandlerWin))
    TaskHandlerWin.backButton.clicked.connect(lambda: back_fun(TaskHandlerWin))
    TaskHandlerWin.removeTask.clicked.connect(lambda: remove_fun(TaskHandlerWin))
    TaskHandlerWin.show()
    app.exec_()

def change_selection():
    global window
    taskNum = window.taskSelector.currentIndex()
    with open(backend_path + "\\database.json", 'r+') as file:
        try:
            taskObj = retrieve_by_Num(file, taskNum)
            # Update GUI elements
            streakNumber = taskObj.get_count()
            window.countDisplay.display(streakNumber)
            window.countDisplay.setStyleSheet(f"color:hsl({((streakNumber) * 10) % 360},100%,50%);")
            window.logList.setModel(QStringListModel(["Log Dates : ", "".join(taskObj.logList)]))  # Populate log list
        except Exception as e:
            window.logList.setModel(QStringListModel(["Log Dates : "]))


"""
display_gui
Purpose     : Display the main GUI window and connect events to handlers.
Parameters  : None
Returns     : None
"""
def display_gui(windowObj = None):
    global count, app, window
    if(windowObj == None):
        app = QApplication(sys.argv)
        window = MainWindow(cur_path + "GUI\\MainApp.ui") # Load the GUI design
    else:
        uic.loadUi(cur_path + "GUI\\MainApp.ui",windowObj)
        window = windowObj
    window.countDisplay.display(0)  # Display initial streak count
    # Connect "Log In" button to its action
    window.logIn.clicked.connect(log_button_action)
    window.addRemove.clicked.connect(add_remove_button_action)
    window.taskSelector.currentIndexChanged.connect(change_selection)

    if( 17 <= datetime.datetime.now().hour or  datetime.datetime.now().hour < 5 ):
        window.setStyleSheet(themes.nightStyle)
    else:
        window.setStyleSheet(themes.morningStyle)

    taskNum = window.taskSelector.currentIndex()
    with open(backend_path + "\\database.json", 'r+') as file:
        try:
            taskObj = retrieve_by_Num(file, taskNum)
            # Update GUI elements
            streakNumber = taskObj.get_count()
            window.countDisplay.display(streakNumber)
            window.countDisplay.setStyleSheet(f"color:hsl({((streakNumber) * 10) % 360},100%,50%);")
            window.logList.setModel(QStringListModel(["Log Dates : ", "".join(taskObj.logList)])) # Populate log list
        except Exception as e:
            window.logList.setModel(QStringListModel(["Log Dates : "]))
        try:
            readList = json.load(file)
        except Exception as e:
            readList = []
        for items in readList:
            window.taskSelector.addItem(items["Name"])
    # Scanning Available Methods In Certain Widget
    # get_obj_methods(window.countDisplay)

    window.show()
    app.exec_()  # Execute the application loop


"""
program_start
Purpose     : Initialize the program, load data from the backup file, and set up initial streak state.
Parameters  : None
Returns     : None
"""
def program_start():
    print("Program Started")




"""
program_end
Purpose     : Finalize the program by saving the database to the backup file.
Parameters  : None
Returns     : None
"""
def program_end():
    print("Program Exited")

"""
main
Purpose     : Define the main program flow (start -> GUI -> end).
Parameters  : None
Returns     : None
"""
def main():
    program_start()
    print(os.path.abspath(__file__))  # Debug: Print current file path
    display_gui()
    program_end()

# Entry point of the program
if __name__ == "__main__":
    main()



