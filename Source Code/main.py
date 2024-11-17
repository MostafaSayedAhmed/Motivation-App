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

"""
line_modify
Purpose     : Modifies or appends a line in the database file.
Parameters  : 
    - line_index (int, default -1): Index of the line to modify (-1 to append).
    - str (string, default ""): Content to write to the line.
Returns     : None
"""
def line_modify(line_index=-1, str=""):
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
    date_string = f"{date.day}-{date.month}-{date.year}"
    if not read_list:
        line_modify(0, f"Count = {count}")
        line_modify(str=date_string)
    else:
        count = int(read_list[0][8:].strip())
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
    program_end()

# Entry point of the program
if __name__ == "__main__":
    main()
