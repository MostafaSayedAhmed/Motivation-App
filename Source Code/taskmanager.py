# package include all auxillary functions needed to perform streak checking and date difference operations
from utils import *

# task manager used to perform all task related operation including calculating streak , adding/removing tasks and
# updating tasks. It will be used later to export csv file
from filemanager import *


class TaskManager():
    # Initialization taskmanager with list of all tasks stored in JSON File and Date
    def __init__(self, databasepath=""):
        # Initialize Data nad Database Path
        self.database_path = databasepath
        self.date_string = ""
        self.date_update()

        with open(self.database_path + "\\database.json", 'r+') as database:
            self.readlist = json.load(database)

    # Get Number of count for certain task
    def get_count(self, taskObj):
        return taskObj.get_count()

    # Updating the date of today (used to solve edge case (User Logged at 11:59 and Again at 12:00))
    def date_update(self):
        date = datetime.datetime.today()
        self.date_string = f"{date.day}-{date.month}-{date.year}\n"

    # Main function used to calculate streak for certain task
    def streak_calculate(self, taskObj):
        # If JSON file is empty
        if not taskObj.logList:
            # First log entry
            # Set Count of the Task to 1
            taskObj.set_count(1)
            # Add date log at end of list
            taskObj.logList.append(self.date_string)
            # Include Task in JSON File if empty
            self.readlist.append(taskObj.to_dict())
            pass
        # If JSON file is not empty
        else:
            # Check if today's date is not already logged
            if self.date_string in taskObj.logList:
                print(f"Task : \'{taskObj.taskName}\' is already logged ")
                # Check streak for the selected tasks
                check_streak(taskObj)
                pass
            # Put date in task log list if not already logged
            else:
                # Add today's date to tasks log list
                taskObj.logList.append(self.date_string)
                # Sort the dates in log list of the task
                taskObj.logList.sort()
                # Check streak for the selected tasks
                check_streak(taskObj)
                # Print the current task name and streak count
                print(f"You Logged In Today! Your Streak for  is Task : \'{taskObj.taskName}\' "
                      f"at {taskObj.get_count()} Day(s)")
        # Save any updates in readlist to JSON Database file
        with open(self.database_path + "\\database.json", 'r+') as database:
            # Update Task Data
            update_task(database, taskObj)
