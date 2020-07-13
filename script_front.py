""""
A program that stores book infortamitions:
Title, Author,
Year, ISBN

User can:
View all records
Search an entry
Add an entry
Update an entry
Delete
Close
"""

from tkinter import *
import script_back

def view_command():
    list1.delete(0,END)
    for row in script_back.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in script_back.search(e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get()):
        list1.insert(END, row)

def insert_command():
    script_back.insert(e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get())
    list1.delete(0,END)
    list1.insert(END,(e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get()))

def get_selected_row(event):
    global selected_tuple    #to be able to call the local variable in the global program
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)

def delete_command():
    script_back.delete(selected_tuple[0])

window = Tk()
window.title("Book storage")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=0, column=3)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=1, column=1)

e4_value=StringVar()
e4=Entry(window, textvariable=e4_value)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update selected", width=12)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()
