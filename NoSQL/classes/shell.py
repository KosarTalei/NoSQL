import string
import connection
import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
# root['bg'] = '#ffbf00'
lbl = tk.Label(root, text="Write the qestion nmber > ")
lbl2 = tk.Label(root, text="")
lbl.place(x=100, y=25)
lbl2.place(x=100, y=300)
entry = tk.Text(root)
entry.place(x=150, y=25, width=200,
            height=200)


def bas():
    connection.saveAll()

    result = ""
    lbl2.configure(text="")
    tx = entry.get("1.0", "end-1c")
    for t in tx.split("\n"):
        if t != "":
            entry.delete(1.0, "end-1c")
    if (tx == 1):
        lbl2.configure(text="Enter the date time: d/m/y")
        dateEntered = entry.get("1.0", "end-1c")
        result = connection.first(dateEntered)
    elif (tx == 2):
        lbl2.configure(text="Enter the min cost: ")
        minCost = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the max cost: ")
        maxCost = entry.get("1.0", "end-1c")
        result = connection.second(minCost, maxCost)
    elif (tx == 3):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        result = connection.forth(dep, des)
    elif (tx == 4):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        result = connection.forth(dep, des)
    elif (tx == 5):
        lbl2.configure(text="Enter the flight class : ")
        type = dep = entry.get("1.0", "end-1c")
        result = connection.fifth(type)
    elif (tx == 6):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the min cost: ")
        minCost = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the max cost: ")
        maxCost = entry.get("1.0", "end-1c")
        result = connection.sixth(dep, des, minCost, maxCost)
    elif (tx == 7):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the flight capacity : ")
        cap = dep = entry.get("1.0", "end-1c")
        result = connection.seventh(dep, des, cap)
    elif (tx == 8):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the min cost: ")
        minCost = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the max cost: ")
        maxCost = entry.get("1.0", "end-1c")
        result = connection.eagth(dep, des, minCost, maxCost)
    elif (tx == 9):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the date time: YYYY-MM-DD")
        dateEntered = entry.get("1.0", "end-1c")
        result = connection.ninth(dep, des, dateEntered)
    elif (tx == 10):
        lbl2.configure(text="Enter airline name: ")
        airline = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the date time: YYYY-MM-DD")
        dateEntered = entry.get("1.0", "end-1c")
        result = connection.tenth(airline, dateEntered)
    elif (tx == 11):
        lbl2.configure(text="Enter flight capacity number: ")
        cap = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter new capacity number: ")
        new = entry.get("1.0", "end-1c")
        result = connection.eleventh(cap, new)
    elif (tx == 12):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the date time: YYYY-MM-DD")
        dateEntered = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter flight capacity number: ")
        cap = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter new capacity number: ")
        new = entry.get("1.0", "end-1c")
        result = connection.twelveth(dep, des, dateEntered, cap, new)
    elif (tx == 13):
        lbl2.configure(text="Enter the departures: ")
        dep = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the destination : ")
        des = entry.get("1.0", "end-1c")
        lbl2.configure(text="Enter the date time: YYYY-MM-DD")
        dateEntered = entry.get("1.0", "end-1c")
        result = connection.theerteenth(dep, des, dateEntered)

    for i in result:
        lbl2.configure(text=lbl2.cget("text") + str(i) + "\n")


button = tk.Button(root, text="enter", command=bas)
button.place(x=150, y=250)

root.mainloop()
