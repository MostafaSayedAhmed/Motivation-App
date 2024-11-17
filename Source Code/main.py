
import datetime

cur_path = "G:\\Works\\Application\\Motivation-App\\Source Code\\"
rel_path = cur_path+"backend"

date = datetime.date.today()
read_list = []
count = 1

try:
    database = open(rel_path + "\\database.txt", 'x')
    backupdatabase  = open(rel_path + "\\backupdatabase.txt", 'r')
except FileExistsError:
    backupdatabase  = open(rel_path + "\\backupdatabase.txt", 'r')
    database = open(rel_path + "\\database.txt", 'w')


def line_modify(line_index=-1, str =""):
    global read_list
    global database
    database.close()
    database = open(rel_path + "\\database.txt", 'w')
    if(line_index < len(read_list) and line_index != -1):
        read_list[line_index] = str + "\n"
    else:
        read_list.append(str + "\n")
    database.writelines(list(read_list))



def program_start():
    global read_list
    global database
    global count
    print("Program Started")
    read_list = list(backupdatabase.readlines())
    database.writelines(read_list)
    date_string = ''.join(f"{date.day}-{date.month}-{date.year}")
    if(read_list == []):
        line_modify(0,str=f"Count = {count}")
        line_modify(str=date_string)
    else:
        count = int(read_list[0][8:-1])

    backupdatabase.close()




def program_end():
    global database
    global backupdatabase
    database.close()
    database  = open(rel_path + "\\database.txt", 'r')
    read_list = database.readlines()
    backupdatabase = open(rel_path + "\\backupdatabase.txt", 'w')
    backupdatabase.writelines(read_list)
    database.close()
    backupdatabase.close()
    print("Program Exited")

def main():
    global read_list
    program_start()
    program_end()


if __name__ == "__main__":
    main()

