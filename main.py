import tkinter

import pandas as pd
from tkinter import *
from tkinter import ttk

from pandas import to_datetime

students = pd.read_csv('Students.csv')
classes = pd.read_csv('Classes.csv')
assignments = pd.read_csv('Assignments.csv')
classlist = pd.read_csv('Classlist.csv')
classlist['RIT Username'] = classlist['RIT Username'].str.strip()
classlist = classlist.iloc[:, :2]
student1 = students.iloc[1][5]

def display_classes():
    lst1Set.delete(0, tkinter.END)
    name = str(entValue.get()).lower()
    x = classlist[classlist['RIT Username'] == name]
    for i in x['Class Code']:
        lst1Set.insert(0, i)


def show_assignments():
    selection_index = lst1Set.curselection()
    if not selection_index:  # If no class is selected
        return
    selection = lst1Set.get(selection_index[0])  # Get the selected class
    assignment_treeview.delete(*assignment_treeview.get_children())  # Clear previous assignments
    assignments_for_class = assignments[assignments['Class Code'] == selection]
    assignments_for_class['Due date'] = to_datetime(assignments_for_class['Due date'])
    assignments_for_class_sorted = assignments_for_class.sort_values(by='Due date')
    for index, row in assignments_for_class_sorted.iterrows():
        assignment_treeview.insert('', 'end', values=(row['Assignment name'], row['Class Code'], row['Due date']))


root = Tk()
root.geometry("900x500")
root.title("MGIS Midterm Exam")

Label(root, text="RIT username:").grid(row=0, column=0, sticky=W)
entValue = Entry(root)
entValue.grid(row=0, column=1, sticky=W)
btnSubmit = Button(root, text="Submit", command=display_classes)
btnSubmit.grid(row=0, column=1)


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


frm2Set = Frame(root)
frm2Set.grid(row=4, column=1, rowspan=8)
assignment_treeview = ttk.Treeview(frm2Set, columns=('Assignment name', 'Class Code', 'Due date'), show='headings')
assignment_treeview.heading('Assignment name', text='Assignment Name')
assignment_treeview.heading('Class Code', text='Class Code')
assignment_treeview.heading('Due date', text='Due Date')
assignment_treeview.grid(row=0, column=0, sticky='nsew')
assignment_scrollbar = ttk.Scrollbar(frm2Set, orient="vertical", command=assignment_treeview.yview)
assignment_scrollbar.grid(row=0, column=1, sticky='ns')
assignment_treeview.configure(yscrollcommand=assignment_scrollbar.set)


root.mainloop()
