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



window.mainloop()
