from Tkinter import *
master = Tk()
def callback():
    for x in data:
        print data[x].get()
b = Button(master, text="print to the console", width=15, command=callback)
b.pack()
b.grid(row=0, column=0)
data = {}
for n in range(1,6):
    for m in range(0,5):
        a = "a"+str(n)+str(m)
        data[a] = Entry(master)
        data[a].pack()
        data[a].grid(row=n, column=m)
mainloop()
