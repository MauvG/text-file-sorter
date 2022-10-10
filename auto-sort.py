import os
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Auto Sort Files")
window.geometry("300x350")

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    global file_name
    file_name = os.path.basename(file_path)
    global file_directory
    file_directory = os.path.dirname(file_path)

    file_label.config(text="File Opened: " + os.path.basename(file_path))
    

open_button = Button(text="Open File", command=open_file)
file_label = Label(window, text=window)

clicked = StringVar()
clicked.set("Choose File Type")
drop = OptionMenu(window, clicked, "Integer", "Real Numbers", "Characters")

sort_type = StringVar()

def sort():
    sort_type.set("sort")
    window.destroy()
  
sort_button = Button(window, text="Sort", command=sort)

def reverse_sort():
    sort_type.set("reverse")
    window.destroy()

reverse_sort_button = Button(window, text="Reverse Sort", command=reverse_sort)

open_button.pack(pady=10)
file_label.pack(pady=10)
drop.pack(pady=10)
sort_button.pack(pady=10)
reverse_sort_button.pack(pady=10)

window.mainloop()

print(file_name)
print(file_path)
print(file_directory)
print(clicked.get())
print(sort_type.get())

file = open(file_path, 'r')
data = file.read()
data_list = data.split("\n")
file.close()

type = clicked.get()
stype = sort_type.get()

print("Sorting....")

for i in range(len(data_list)):
    if type == "Integer":
        data_list[i] = int(data_list[i])
    elif type == "Real Numbers":
        data_list[i] = float(data_list[i])

if stype == "reverse":   
    data_list.sort(reverse=True)
else:
    data_list.sort()

file_name = file_name.strip(".txt")
print(file_name)
output_file = file_directory + "/" + file_name + "-sorted.txt"
print(output_file)

with open(output_file, 'w') as f:
    for element in data_list:
        f.write(f"{element}\n")

print("Sorting successful")