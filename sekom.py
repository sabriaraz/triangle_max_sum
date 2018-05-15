import tkinter as tk
from tkinter import filedialog


def read_text():
    """ to read triangle text file """
    tree_list = []
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    with open(file_path, "r") as ins:
        array = []
        for line in ins:
            array.append(line)

    temp_two = []
    for j in array:
        temp = []
        for i in j.split(" "):
            try:
                temp.append(int(i))
            except Exception as e:
                print(e)
                pass

        temp_two.append(temp)

    tree_list.append(temp_two)
    tree_list.append(len(temp_two) - 1)
    return tree_list


def max_sum(tree, m):
    """ process to max sum triangle file """

    for i in range(m - 1, -1, -1):
        for j in range(i + 1):
            if (tree[i + 1][j] > tree[i + 1][j + 1]):
                tree[i][j] += tree[i + 1][j]
            else:
                tree[i][j] += tree[i + 1][j + 1]

    return tree[0][0]


print(max_sum(read_text()[0], read_text()[1]))