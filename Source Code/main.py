"""
Author      : Mostafa Sayed Ahmed Taha
Description : Motivation Application to track streaks for a single task.
Date        : 11/17/2024
Future Work : Extend functionality to track multiple task streaks.

General Notes:
    - Opt: Indicates areas for potential optimization.
    - adv/feature/: Denotes future improvements or features.
"""

import datetime  # Module to handle date and time operations
import sys       # Module for handling script/executable-specific operations and GUI event loop
import os        # Module for working with file system paths
from PyQt5.QtWidgets import QApplication, QMainWindow
# QApplication: Manages the main application loop
# QMainWindow: Provides the framework for creating GUI windows

from PyQt5.QtGui import QIcon  # (Unused) Allows customization of the window icon
from PyQt5.QtCore import QStringListModel  # Used to populate a list view widget with data
from PyQt5 import uic  # Connects the GUI layout (from Qt Designer) with the Python code dynamically

from taskmanager import taskmanager

# Retrieve today's date (format: year, month, day)
date = datetime.date.today()

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

# Global variables for streak tracking and data storage
read_list = []  # List to store lines read from the database file
count = 1       # Current streak count (Opt: Extend to track multiple streaks)

# Initialize database and backup files
try:
    # Create database and backup files if they don't exist
    database = open(backend_path + "\\database.txt", 'x')
    backupdatabase = open(backend_path + "\\backupdatabase.txt", 'x')
except FileExistsError:
    # If files already exist, open them for the appropriate operations
    backupdatabase = open(backend_path + "\\backupdatabase.txt", 'r')
    database = open(backend_path + "\\database.txt", 'w')

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
log_button_action
Purpose     : Perform operations when the "Log In" button is clicked:
              - Log today's date
              - Calculate and update the streak
Parameters  : None
Returns     : None
"""
def log_button_action():
    global window

    login = taskmanager(backend_path)
    login.streak_calculate()

    # Update GUI elements

    window.countDisplay.display(login.get_count())
    window.logList.setModel(QStringListModel(["Log Dates : ", "".join(login.readlist[1:])]))

    with open(backend_path + "\\backupdatabase.txt", 'w') as backupdatabaseGUI:
        backupdatabaseGUI.writelines(login.readlist)

"""
display_gui
Purpose     : Display the main GUI window and connect events to handlers.
Parameters  : None
Returns     : None
"""
def display_gui():
    global count, app, window
    app = QApplication(sys.argv)
    window = uic.loadUi(cur_path + "GUI\\MainApp.ui")  # Load the GUI design
    window.countDisplay.display(0)  # Display initial streak count
    with open(backend_path + "\\backupdatabase.txt", 'r') as init_database:
        window.logList.setModel(QStringListModel(["Log Dates : ","".join(init_database.readlines()[1:])]))  # Populate log list
    window.logIn.clicked.connect(log_button_action)  # Connect "Log In" button to its action
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

