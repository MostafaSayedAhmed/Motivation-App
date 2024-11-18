"""
Author      : Mostafa Sayed Ahmed Taha
Description : Motivation Application to track streaks for a single task.
Date        : 11/17/2024
Future Work : Extend functionality to track multiple task streaks.

General Notes:
    - Opt: Indicates areas for potential optimization.
    - adv/feature/: Denotes future improvements or features.
"""

import datetime
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QStringListModel
from PyQt5 import uic

# Retrieve today's date (day, month, year)
date = datetime.date.today()

# Paths for application files
cur_path = "G:\\Works\\Application\\Motivation-App\\Source Code\\"
backend_path = cur_path + "backend"

# Global Variables (Opt)
read_list = []  # Stores data read from the file for all operations
count = 1       # Tracks the current streak count (adv/track multiple streaks/)

# File Initialization
try:
    # Create database and backup files if they don't exist
    database = open(backend_path + "\\database.txt", 'x')
    backupdatabase = open(backend_path + "\\backupdatabase.txt", 'x')
except FileExistsError:
    # Open existing files for reading (backup) and writing (database)
    backupdatabase = open(backend_path + "\\backupdatabase.txt", 'r')
    database = open(backend_path + "\\database.txt", 'w')
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Streak Tracking Program")
        self.setGeometry(960,440,500,500)
        self.setWindowIcon(QIcon(cur_path + "\\Images\\Icon.webp"))
        pass


def get_obj_methods(obj):
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    print(dir(obj))

def log_button_action():
    global read_list, database, count,app,window
    date_string = f"{date.day}-{date.month}-{date.year}"
    if not read_list:
        line_modify(f"Count = {count}",0)
        line_modify(str=date_string)
    else:
        count = int(read_list[0][8:].strip())
        if not((date_string + "\n") in  read_list):
            line_modify(date_string)
        check_streak()
        line_modify(f"Count = {count}", 0)
        print(f"You Logged In Today! Your Streak is at {count} Day(s)")
    window.countDisplay.display(count)
    window.logList.setModel(QStringListModel([ "Log Dates : ", "".join(read_list[1:])]))
def display_gui():
    global count,app,window
    app = QApplication(sys.argv)
    window = uic.loadUi(cur_path + "\\GUI\\MainApp.ui")
    window.countDisplay.display(count)
    window.logList.setModel(QStringListModel([ "Log Dates : ", "".join(read_list[1:])]))
    window.logIn.clicked.connect(log_button_action)

    window.show()
    app.exec_()

def check_streak():
    global count,read_list
    temp_list = read_list[-1::-1]
    count = 1
    for i in range(0, len(temp_list)):
        if ("Count" in temp_list[i + 1]):
            break
        else:
            result = True if (int(temp_list[i][0:2]) - int(temp_list[i + 1][0:2])) == 1 else False
            if (result):
                count += 1
            else:
                break
"""
line_modify
Purpose     : Modifies or appends a line in the database file.
Parameters  : 
    - line_index (int, default -1): Index of the line to modify (-1 to append).
    - str (string, default ""): Content to write to the line.
Returns     : None
"""
def line_modify(str="",line_index=-1):
    global read_list, database
    database.close()
    database = open(backend_path + "\\database.txt", 'w')
    if (0 <= line_index) and (line_index < len(read_list)):
        read_list[line_index] = str + "\n"
    else:
        read_list.append(str + "\n")
    database.writelines(read_list)


"""
program_start
Purpose     : Initializes the program by copying backup file data to the database file.
               - If the backup is empty, initializes with streak count and date.
               - Otherwise, retrieves the current streak count.
Parameters  : None
Returns     : None
"""
def program_start():
    global read_list, database, count
    print("Program Started")
    read_list = list(backupdatabase.readlines())
    database.writelines(read_list)
    if read_list:
        count = int(read_list[0][8:].strip())
        try:
            read_list.remove("\n")
        except ValueError:
            pass
    backupdatabase.close()

"""
program_end
Purpose     : Finalizes the program by copying the database file content to the backup.
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
Purpose     : Defines the main flow of the program (start -> end).
Parameters  : None
Returns     : None
"""
def main():
    program_start()
    display_gui()
    program_end()

# Entry point of the program
if __name__ == "__main__":
    main()

