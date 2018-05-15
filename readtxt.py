import tkinter as tk
from tkinter import filedialog
def ReadTriangle():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    #txt = file_path.readlines()


    with open(file_path, "r") as ins:
        array = []
        for line in ins:
             array.append(line)

    temp = []
    temp_two = []
    for j in array:
        temp=[]
        for i in j.split(" "):
            try:
                temp.append(int(i))
            except:
                pass

        temp_two.append(temp)
    data_list = []
    data_list.append(temp_two)
    data_list.append(len(temp_two))
    return data_list
print(ReadTriangle()[1])












