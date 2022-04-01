
import modul
from tkinter import *
import sql

def st():
    i = 1
    #with open("history.txt", "r") as file:
        #hh1.set(file.readline())
        #hh2.set(file.readline())
        #hh3.set(file.readline())
        #hh4.set(file.readline())
        #hh5.set(file.readline())
    query_results = sql.select()
    hh1.set(query_results[0])
    hh2.set(query_results[1])
    hh3.set(query_results[2])
    hh4.set(query_results[3])
    hh5.set(query_results[4])
    print(hh1.get())


num3 = ""

root = Tk()
root.title("калькультр")
root.geometry("400x300")

num1 = IntVar()
num2 = IntVar()
operation = StringVar()
r = StringVar()
r.set("решение: {}".format(num3))



message_entry_num1 = Entry(textvariable = num1)
message_entry_num1.place(relx=.3, rely=.1, anchor="c")

message_entry_operation = Entry(textvariable =  operation)
message_entry_operation.place(relx=.3, rely=.3, anchor="c")

message_entry_num2 = Entry(textvariable = num2)
message_entry_num2.place(relx=.3, rely=.5, anchor="c")

name_label = Label(textvariable = r)
name_label.place(relx=.3, rely=.6, anchor="c")

message_button = Button(root, text="решить", command=lambda: sl())
message_button.place(x=50, y=100)


#history

hh1 = StringVar()
hh2 = StringVar()
hh3 = StringVar()
hh4 = StringVar()
hh5 = StringVar()

h1 = Label(textvariable = hh1)
h1.place(relx=.7, rely=.3, anchor="c")

h2 = Label(textvariable = hh2)
h2.place(relx=.7, rely=.4, anchor="c")

h3 = Label(textvariable = hh3)
h3.place(relx=.7, rely=.5, anchor="c")

h4 = Label(textvariable = hh4)
h4.place(relx=.7, rely=.6, anchor="c")

h5 = Label(textvariable = hh5)
h5.place(relx=.7, rely=.7, anchor="c")

st()

def sl():
    num3 = modul.slove(message_entry_num1.get(), message_entry_num2.get(), message_entry_operation.get())
    r.set("решение: {}".format(num3))
    hh5.set(hh4.get())
    hh4.set(hh3.get())
    hh3.set(hh2.get())
    hh2.set(hh1.get())
    hh1.set(message_entry_num1.get() + " " + message_entry_operation.get() + "" + message_entry_num2.get() + " " + "=" + "" + str(num3))
    sql.insert(hh1.get())

def writehistory():
    with open("history.txt", "w") as file:
        file.write(hh1.get())
        file.write("\n" + hh2.get())
        file.write("\n" + hh3.get())
        file.write("\n" + hh4.get())
        file.write("\n" + hh5.get())
        root.destroy()



message_button.pack()

root.protocol("WM_DELETE_WINDOW", writehistory)
root.mainloop()
