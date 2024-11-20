from utils import *

class taskmanager :
    count    = 1
    readlist = []


    def __init__(self,datebasePath):
        self.database_path = datebasePath
        self.date_string = ""
        self.date_update()
        with open(datebasePath + "\\backupdatabase.txt",'r') as backupdatabase:
            self.readlist = list(backupdatabase.readlines())
            if self.readlist:
                self.set_count(int(self.readlist[0][8:].strip()))  # Extract streak count
                try:
                    self.readlist.remove("\n")  # Remove empty lines
                except ValueError:
                    pass
        with open(datebasePath + "\\database.txt",'w') as database:
            database.writelines(self.readlist)

    def get_count(self):
        return self.count
    def set_count(self,value):
        self.count = value
    def date_update(self):
        date = datetime.datetime.today()
        self.date_string = f"{date.day}-{date.month}-{date.year}"

    def streak_calculate(self):
        if not self.readlist:
            # First log entry
            line_modify(f"Count = {self.count}", 0,self.readlist,self.database_path)
            line_modify(self.date_string,-1,self.readlist,self.database_path)
        else:
            # Update streak if today's date is not already logged
            self.count = int(self.readlist[0][8:].strip())  # Extract current streak count
            if not (self.date_string + "\n") in self.readlist:
                line_modify(self.date_string,-1,self.readlist,self.database_path)
            check_streak(self,self.readlist)
            line_modify(f"Count = {self.count}", 0,self.readlist,self.database_path)
            print(f"You Logged In Today! Your Streak is at {self.count} Day(s)")
        with open(self.database_path + "\\database.txt",'r') as database:
            self.readlist = database.readlines()
