import datetime
import filemanager

"""
calculate_date_diff
Purpose     : Calculate the difference between two dates and determine if the streak is maintained.
Parameters  :
    - stringA : The previous date (string format)
    - stringB : The current date (string format)
    - taskObj : Object use to manipulate tasking operation (Task Object format)
Returns     :
    - flag: Indicates streak status:
        - 0: Streak is maintained
        - 1: Streak is broken
"""
def calculate_date_diff(stringA, stringB,taskObj):
    flag = 0                    # Default to streak maintained
    stringA = stringA.strip()   # To removes spaces if there are any
    stringB = stringB.strip()   # To removes spaces if there are any
    dateA = datetime.datetime.strptime(stringA, "%d-%M-%Y")     # Make datetime object from first string
    dateB = datetime.datetime.strptime(stringB, "%d-%M-%Y")     # Make datetime object from second string
    # If difference in date is one , the streak is maintained
    if (dateB - dateA).days == 1:
        taskObj.set_count(taskObj.get_count() + 1)  # Increment streak count
    # Otherwise the streak is not maintained
    else:
        flag = 1  # Indicate streak broken
    return flag

"""
check_streak
Purpose     : Calculate the current streak based on log entries.
Parameters  : None
Returns     : None
"""
def check_streak(taskObj):
    temp_list = taskObj.logList[::-1]  # Reverse the list for backward iteration
    taskObj.set_count(1)               # Reset count
    # Calculate Count of streak by finding whether difference between dates is one or more
    for i in range(len(temp_list) - 1):
        if calculate_date_diff(temp_list[i + 1], temp_list[i], taskObj):
            break
