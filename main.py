import sys
import modul

from tkinter import *
num3 = ""

root = Tk()
root.title("калькультр")
root.geometry("400x300")

num1 = IntVar()
num2 = IntVar()
operation = StringVar()

message_entry_num1 = Entry(textvariable = num1)
message_entry_num1.place(relx=.5, rely=.1, anchor="c")

message_entry_operation = Entry(textvariable =  operation)
message_entry_operation.place(relx=.5, rely=.3, anchor="c")

message_entry_num2 = Entry(textvariable = num2)
message_entry_num2.place(relx=.5, rely=.5, anchor="c")

name_label = Label(text = "решение: " + num3)
name_label.place(relx=.5, rely=.6, anchor="c")

message_button = Button(root, text="решить", command=lambda: modul.slove(message_entry_num1.get(), message_entry_num2.get(), message_entry_operation.get()))
#message_button.place(relx=.5, rely=.0, anchor="c")

message_button.pack()


root.mainloop()
