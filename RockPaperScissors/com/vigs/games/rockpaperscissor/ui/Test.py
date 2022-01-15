import tkinter

root = tkinter.Tk()

f1 = tkinter.Frame()

btn = tkinter.Button(text="hello")

btn.master = f1

btn.grid(row=0, column=0)

f1.master = root

f1.grid(row=0, column=0)

root.mainloop()
