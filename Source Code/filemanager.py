import json
import csv

class Task:
    def __init__(self, Name="", Description="", Number=1,log_List=[]):
        self.taskCount = 0
        self.taskName = Name
        self.taskDes = Description
        self.taskNum = Number
        self.logList = log_List

    def __str__(self):
        return f"Task {self.taskNum} Name: {self.taskName} " \
               f"Description : {self.taskDes} Task Count : {self.taskCount}"

    def get_count(self):
        return self.taskCount

    def set_count(self, value):
        self.taskCount = value

    def to_dict(self):
        return {"Name": self.taskName,
                "Description": self.taskDes,
                "Count": self.taskCount,
                "Log": self.logList,
                "Number": self.taskNum
                }

    def from_dict(self, dictObj):
        self.taskCount = dictObj["Count"]
        self.taskName = dictObj["Name"]
        self.taskDes = dictObj["Description"]
        self.logList = dictObj["Log"]
        self.taskNum = dictObj["Number"]
        return self



def export_to_csv(file):
    try:
        file.seek(0)
        csv_list = json.load(file)
        if not csv_list:
            raise ValueError("No tasks to export.")  # Handle empty list
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error exporting to CSV: {e}")
        return

    try:
        with open("csvData.csv", 'w', newline='') as mycsvfile:
            fields = csv_list[0].keys()
            csv_writer = csv.DictWriter(mycsvfile, fieldnames=fields)
            csv_writer.writeheader()
            csv_writer.writerows(csv_list)
        print("Data exported successfully to csvData.csv")
        file.seek(0)
    except Exception as e:
        print(f"Failed to write to CSV: {e}")


def add_task(file, name, description):
    try:
        file.seek(0)
        read_data = json.load(file)
    except json.JSONDecodeError:
        read_data = []  # Initialize as an empty list if the file is empty or invalid

    # Find the first missing number in the sequence
    existing_numbers = sorted([task['Number'] for task in read_data])
    next_number = 1  # Start with 1
    for number in existing_numbers:
        if number != next_number:
            break
        next_number += 1

    # Create and append the new task
    new_task = Task(name, description, next_number)
    read_data.append(new_task.to_dict())

    # Sort tasks by number to maintain sequential order
    read_data.sort(key=lambda x: x['Number'])

    # Write the updated data back to the file
    file.seek(0)
    json.dump(read_data, file, indent=4)
    file.truncate()  # Remove any leftover data
    file.seek(0)


def remove_task(file, task_num):
    try:
        file.seek(0)
        read_data = json.load(file)
    except json.JSONDecodeError:
        print("No Data Found")
        return

    original_length = len(read_data)
    read_data = [task for task in read_data if task['Number'] != task_num]

    if len(read_data) == original_length:
        print(f"Task number {task_num} not found.")
    else:
        print(f"Task number {task_num} removed.")

    # Sort tasks by number to maintain sequential order
    read_data.sort(key=lambda x: x['Number'])
    for i in range(0,len(read_data)):
        read_data[i]["Number"] = i+1

    # Write the updated data back to the file
    file.seek(0)
    json.dump(read_data, file, indent=4)
    file.truncate()  # Remove any leftover data
    file.seek(0)

def update_task(file,taskObj):
    # Reset file pointer to the beginning of the file
    file.seek(0)
    # load JSON data using JSON module
    read_data = json.load(file)
    # Update task data for read data that will be load to JSON file
    read_data[taskObj.taskNum - 1] = taskObj.to_dict()
    # Reset file pointer to the start of the file
    file.seek(0)
    # Save data to the file and Set indent to 4 to make it readable
    json.dump(read_data, file, indent=4)
    # Remove any leftover data
    file.truncate()
    # Reset file pointer to the start of the file
    file.seek(0)

def retrieve_by_Num(file,taskNum):
    # Check TaskNum
    if(taskNum < 0):
        taskNum = 0
    # Reset file pointer to the beginning of the file
    file.seek(0)
    # load JSON data using JSON module
    read_data = json.load(file)
    # Retrieve task by Number
    try:
        taskObj = Task().from_dict(read_data[taskNum])
    except Exception as e:
        print(str(e) + "\nTask Not Found!!")
        raise e
    # Reset file pointer to the start of the file
    file.seek(0)
    # Return task object
    return taskObj