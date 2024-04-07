import tkinter

import pandas as pd
from tkinter import *

students = pd.read_csv('Students.csv')
classes = pd.read_csv('Classes.csv')
classlist = pd.read_csv('Classlist.csv')
classlist['student'] = classlist['student'].str.strip()
classlist = classlist.iloc[:, :2]
student1 = students.iloc[1][5]
print(student1)
print('\n\n\n\n')
print('student1 is in the following classes:\n')
c = classlist[classlist['student'] == student1]
print(c['class'])

def display_classes():
    lst1Set.delete(0, tkinter.END)
    name = str(entValue.get())
    x = classlist[classlist['student'] == name]
    for i in x['class']:
        lst1Set.insert(0, i)


def show_assignments():
    selectionIndex = lst1Set.curselection()
    selection = [lst1Set.get(x) for x in selectionIndex]
    print(selection)
    #for c in selection:


root = Tk()
root.geometry("600x600")
root.title("MGIS Midterm Exam")

Label(root, text="RIT username:").grid(row=0, column=0, sticky=W)
entValue = Entry(root)
entValue.grid(row=0, column=1, sticky=W)
btnSubmit = Button(root, text="Submit", command=display_classes)
btnSubmit.grid(row=0, column=2, sticky=W)


frm1Set = Frame(root)
frm1Set.grid(row=4, column=0, rowspan=8)
Label(frm1Set, text="Classes:").grid(row=0, column=0, sticky=W)
scr1Set = Scrollbar(frm1Set)
scr1Set.grid(row=1, column=1, sticky=N+W+S)
lst1Set = Listbox(frm1Set, height=8, yscrollcommand=scr1Set.set)
lst1Set.grid(row=1, column=0)
scr1Set.config(command=lst1Set.yview)
showAssignmentsBtn = Button(frm1Set, text="Show Assignments", command=show_assignments)
showAssignmentsBtn.grid(row=2, column=0, sticky=W)




root.mainloop()