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
calculate_date_diff
Purpose     : Calculate the difference between two dates and determine if the streak is maintained.
Parameters  : 
    - stringA: The previous date (string format)
    - stringB: The current date (string format)
Returns     : 
    - flag: Indicates streak status:
        - 0: Streak is maintained
        - 1: Streak is broken
"""
def calculate_date_diff(stringA, stringB):
    global count
    flag = 0  # Default to streak maintained
    dateA = datetime.datetime.strptime(stringA.strip(), "%d-%M-%Y")
    dateB = datetime.datetime.strptime(stringB.strip(), "%d-%M-%Y")
    if (dateB - dateA).days == 1:
        count += 1  # Increment streak count
    else:
        flag = 1  # Indicate streak broken
    return flag

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
    global read_list, database, count, app, window
    date_string = f"{date.day}-{date.month}-{date.year}"
    if not read_list:
        # First log entry
        line_modify(f"Count = {count}", 0)
        line_modify(date_string)
    else:
        # Update streak if today's date is not already logged
        count = int(read_list[0][8:].strip())  # Extract current streak count
        if not (date_string + "\n") in read_list:
            line_modify(date_string)
            check_streak()
        line_modify(f"Count = {count}", 0)
        print(f"You Logged In Today! Your Streak is at {count} Day(s)")

    # Update GUI elements
    window.countDisplay.display(count)
    window.logList.setModel(QStringListModel(["Log Dates : ", "".join(read_list[1:])]))

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
    window.countDisplay.display(count)  # Display initial streak count
    window.logList.setModel(QStringListModel(["Log Dates : ", "".join(read_list[1:])]))  # Populate log list
    window.logIn.clicked.connect(log_button_action)  # Connect "Log In" button to its action
    window.show()
    app.exec_()  # Execute the application loop

"""
check_streak
Purpose     : Calculate the current streak based on log entries.
Parameters  : None
Returns     : None
"""
def check_streak():
    global count, read_list
    temp_list = read_list[::-1]  # Reverse the list for backward iteration
    count = 1  # Reset count
    for i in range(len(temp_list) - 1):
        if 'Count' in temp_list[i + 1]:
            break
        else:
            flag = calculate_date_diff(temp_list[i + 1], temp_list[i])
            if flag == 1:  # Stop if the streak is broken
                break

"""
line_modify
Purpose     : Modify or append lines in the database file.
Parameters  : 
    - str (string): The content to write to the file.
    - line_index (int): The line to modify (-1 for append).
Returns     : None
"""
def line_modify(str="", line_index=-1):
    global read_list, database
    database.close()
    database = open(backend_path + "\\database.txt", 'w')
    if 0 <= line_index < len(read_list):
        read_list[line_index] = str + "\n"
    else:
        read_list.append(str + "\n")
    database.writelines(read_list)

"""
program_start
Purpose     : Initialize the program, load data from the backup file, and set up initial streak state.
Parameters  : None
Returns     : None
"""
def program_start():
    global read_list, database, count
    print("Program Started")
    read_list = list(backupdatabase.readlines())  # Load backup data
    database.writelines(read_list)  # Copy backup data to the database
    if read_list:
        count = int(read_list[0][8:].strip())  # Extract streak count
        try:
            read_list.remove("\n")  # Remove empty lines
        except ValueError:
            pass
    backupdatabase.close()

"""
program_end
Purpose     : Finalize the program by saving the database to the backup file.
Parameters  : None
Returns     : None
"""
def program_end():
    global database, backupdatabase
    database.close()
    database = open(backend_path + "\\database.txt", 'r')
    read_list = database.readlines()
    backupdatabase = open(backend_path + "\\backupdatabase.txt", 'w')
    backupdatabase.writelines(read_list)
    database.close()
    backupdatabase.close()
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
