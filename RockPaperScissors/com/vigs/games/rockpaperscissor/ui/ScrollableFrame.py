from typing import Final
from tkinter import Frame
import tkinter


class ScrollableFrame(Frame):

    class __Orientation:
        def __init__(self, type: str):
            self.type = type

        def __str__(self):
            return "Orientation[type: " + self.type + "]"

    Orientation = __Orientation

    VERTICAL: Final[Orientation] = Orientation(type="VERTICAL")  ## VIGS_RELEARN
    HORIZONTAL: Final[Orientation] = Orientation(type="HORIZONTAL")  ## VIGS_RELEARN


    def __init__(self, master, orientation: Orientation):
        self.master1 = master
        self.orientation = orientation
        self.__rows = {}
        self.__columns = {}
        self.non_private_variable_dummy = {}
        self.buildCanvas()
        #Frame.__init__(self, master=master)



    def buildCanvas(self):
        self.canvas = tkinter.Canvas(master=self.master1, height=280, width=400)
        self.canvas.grid(row=0, column=0)
        #self.canvas.create_oval(10, 10, 20, 20, fill="red")
        #self.canvas.create_oval(200, 200, 220, 220, fill="blue")


        self.scroll_x = tkinter.Scrollbar(master=self.master1, orient=tkinter.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_y = tkinter.Scrollbar(master=self.master1, orient=tkinter.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.scroll_x.grid(row=1, column=0, sticky=tkinter.EW)
        self.scroll_y.grid(row=0, column=1, sticky=tkinter.NS)


        self.frameForChildComponents = tkinter.Frame(self.canvas, height=400, width=400)
        self.frameForChildComponents.grid(row=0, column=0)

        self.refreshCanvas()

    def refreshCanvas(self):
        self.canvas.create_window(0, 0, anchor="nw", window=self.frameForChildComponents)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1.0) ## move the scrollbar to the bottom to display the latest played game


    def add(self, frame:Frame):
        if self.orientation == ScrollableFrame.VERTICAL:
            self.__addRow(frame=frame)
        elif self.orientation == ScrollableFrame.HORIZONTAL:
            self.__addColumn(frame=frame)


        self.refreshCanvas()


    def __addRow(self, frame: Frame):
        self.__rows[len(self.__rows)] = frame
        #frame.master = self.canvas
        frame.master = self.frameForChildComponents
        frame.grid(row=len(self.__rows)+1, column=0)
        print("Added Row:", len(self.__rows))

    def __addColumn(self, frame: Frame):
        #frame.master = self.canvas
        frame.master = self.frameForChildComponents
        frame.grid(row=0, column=len(self.__columns))



