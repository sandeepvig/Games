from typing import Final
from tkinter import Frame
import tkinter


class ScrollableFrame:

    def __init__(self):
        self.root = tkinter.Tk()
        self.buildCanvas()
        self.root.mainloop()


    def buildCanvas(self):
        self.canvas = tkinter.Canvas(master=self.root, height=400, width=400, borderwidth=4, background="yellow")

        #self.canvas.create_oval(10, 10, 20, 20, fill="red")
        #self.canvas.create_oval(200, 200, 220, 220, fill="blue")


        self.frameForChildComponents = tkinter.Frame(self.canvas, background="green")
        #self.frameForChildComponents.grid(row=0, column=0)
        self.frameForChildComponents.pack()

        self.scroll_x = tkinter.Scrollbar(master=self.root, orient=tkinter.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_y = tkinter.Scrollbar(master=self.root, orient=tkinter.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        #self.scroll_x.grid(row=1, column=0, sticky=tkinter.EW)
        #self.scroll_y.grid(row=0, column=1, sticky=tkinter.NS)
        self.scroll_y.pack(fill="y" , side="right")
        self.scroll_x.pack(fill="y", side="bottom")

        self.add()
        self.refreshCanvas()
        #self.canvas.update_idletasks()

        #self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def refreshCanvas(self):
        self.canvas.create_window(0, 0, anchor="nw", window=self.frameForChildComponents)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def add(self):
        for i in range(500):
            frame = tkinter.Frame(master=self.frameForChildComponents)
            frame.pack(side="top")
            #frame.grid(row=i, column=0)
            #frame = self.frameForChildComponents
            bt1 = tkinter.Button(master=frame, text="Hello1_"+str(i))
            bt2 = tkinter.Button(master=frame, text="Hello2_"+str(i))
            #bt1.grid(row=i, column=0)
            #bt2.grid(row=i, column=1)

            bt1.pack(side="left")
            bt2.pack(side="right")
        self.canvas.create_window(0, 0, anchor="nw", window=self.frameForChildComponents)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')


ScrollableFrame()