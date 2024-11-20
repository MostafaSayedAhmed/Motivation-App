import datetime

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
def calculate_date_diff(stringA, stringB,obj):
    flag = 0  # Default to streak maintained
    stringA = stringA.strip()
    stringB = stringB.strip()
    dateA = datetime.datetime.strptime(stringA, "%d-%M-%Y")
    dateB = datetime.datetime.strptime(stringB, "%d-%M-%Y")
    if (dateB - dateA).days == 1:
        obj.set_count(obj.get_count() + 1)  # Increment streak count
    else:
        flag = 1  # Indicate streak broken
    return flag

"""
check_streak
Purpose     : Calculate the current streak based on log entries.
Parameters  : None
Returns     : None
"""
def check_streak(obj,read_list):
    temp_list = read_list[::-1]  # Reverse the list for backward iteration
    obj.set_count(1)  # Reset count


    for i in range(len(temp_list) - 1):
        if 'Count' in temp_list[i + 1]:
            break
        else:
            flag = calculate_date_diff(temp_list[i + 1], temp_list[i],obj)
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
def line_modify(str="", line_index=-1 , read_list = [],backend_path = ""):
    if 0 <= line_index < len(read_list):
        read_list[line_index] = str + "\n"
    else:
        read_list.append(str + "\n")
    with open(backend_path + "\\database.txt", 'w') as database:
        database.writelines(read_list)