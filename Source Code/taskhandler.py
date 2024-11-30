import json
import time
from main import display_gui

from filemanager import *
from PyQt5.QtWidgets import QApplication,QMessageBox, QMainWindow
import sys
from PyQt5 import uic
from PyQt5.QtCore import QStringListModel  # Used to populate a list view widget with data
import os
from PyQt5.QtGui import QIcon  # Allows customization of the window icon

# Determine the absolute path of the script or executable file
if getattr(sys, 'frozen', False):
    # If running as an executable (e.g., created using PyInstaller)
    current_file_path = os.path.dirname(sys.executable)
else:
    # If running as a script
    current_file_path = os.path.dirname(os.path.abspath(__file__))

# Define paths for application files
cur_path = current_file_path + "\\"

class MainWindow(QMainWindow):
    def __init__(self,path,secondWindowPath):
        super().__init__()
        uic.loadUi(path, self)  # Load main window UI
        # Initialize the second window
        self.second_window = TaskWindow(secondWindowPath)

    def open_second_window(self):
        self.second_window.show()
        self.hide()

class TaskWindow(QMainWindow):
    def __init__(self,path):
        super().__init__()
        uic.loadUi(path, self)  # Load second window UI

    def back_fun(self):
        global window
        window.second_window.go_back(window)

    def add_fun(self):
        global window, window
        secondWindow = window.second_window
        taskLists = []
        taskLists.append("Task List : \n")
        with open(cur_path + "\\backend\\database.json", 'r+') as file:
            read_list = json.load(file)
        for i in [read_list[i]["Name"] + '\n' for i in range(0, len(read_list))]:
            taskLists.append(i)
        newTaskName = secondWindow.name.text() + "\n"
        newTaskDescription = secondWindow.description.toPlainText()
        if newTaskName + "\n" in [read_list[i]["Name"] + '\n' for i in range(0, len(read_list))]:
            print("Already Existing Task")
            # Popup Window
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setWindowTitle("Notification")
            message.setText("Already Existing Task")
            message.exec_()
            return
        else:
            taskLists.append(newTaskName)
            with open(cur_path + "\\backend\\database.json", 'r+') as file:
                add_task(file, newTaskName, newTaskDescription)
            secondWindow.taskList.setModel(QStringListModel(taskLists))

    def remove_fun(self):
        global window
        secondWindow = window.second_window
        try:
            taskNum = secondWindow.taskList.selectionModel().selectedIndexes()[0].row()
        except Exception as e:
            # Popup Window
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setWindowTitle("Notification")
            message.setText("Select the Task first")
            message.exec_()
            return
        if taskNum == 0:
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setWindowTitle("Notification")
            message.setText("Select a Real Task")
            message.exec_()
            return
        else:
            with open(cur_path + "\\backend\\database.json", 'r+') as file:
                remove_task(file, taskNum)

            taskLists = []
            taskLists.append("Task List : \n")
            with open(cur_path + "\\backend\\database.json", 'r+') as file:
                read_list = json.load(file)
            for i in [read_list[i]["Name"] + '\n' for i in range(0, len(read_list))]:
                taskLists.append(i)
            secondWindow.taskList.setModel(QStringListModel(taskLists))

    def go_back(self,main_window):
        main_window.show()
        self.close()

