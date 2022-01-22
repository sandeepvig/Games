import random
import time
import tkinter
import threading

class SundiWindow:
    MAX_X = 20
    MAX_Y = 30

    def __init__(self):
        self.cellwidth = 2
        self.cellheight = 1 #ideally these should be a single constant, cell is a square
        self.sundi = []
        self.currentDirection = tkinter.W ## anything would do as default
        self.gameStarted = False

    def launch(self):
        self.build()
        self.registerEventHandlers()

        crawlSundiThread = threading.Thread(name="CrawlSundiThread", target=self.crawlSundi)
        crawlSundiThread.start()

        self.root.mainloop()

    def build(self):
        self.root = tkinter.Tk()
        self.root.title("Lets play Sundi!!")

        #self.rootFrame = tkinter.Frame(self.root, height=100, width=100, borderwidth=20)
        #self.rootFrame.grid(row=0, column=0)

        self.drawGrid()

        self.headCell = self.drawCell(color="red", position=(5, 5))
        self.targetCell = self.drawCell(color="blue", position=self.nextRandomTargetPosition())

        self.sundi.append(self.headCell)


    def drawGrid(self):
        for x in range(SundiWindow.MAX_X):
            for y in range(SundiWindow.MAX_Y):
                self.drawCell(color="gray", position=(x, y))

    def drawCell(self, color: str, position: (int, int)):
        sundiCell = tkinter.Label(self.root, width=self.cellwidth, height=self.cellheight)
        sundiCell.configure(borderwidth=2, background=color, relief="groove")
        sundiCell.grid(row=position[0], column=position[1])
        return sundiCell

    def drawSundi(self):
        for sundiCell in self.sundi:
            pass

    def registerEventHandlers(self):
        self.root.bind("<KeyPress>", self.keyPressed)

    def keyPressed(self, event: tkinter.Event):
        print("Key Pressed", event)

        print(self.headCell.grid_info())

        self.gameStarted = True

        match event.keycode:
            case 37:
                self.currentDirection = tkinter.E
                self.headCell.grid(column=self.headCell.grid_info()["column"]-1)
            case 38:
                self.currentDirection = tkinter.N
                self.headCell.grid(row=self.headCell.grid_info()["row"]-1)
            case 39:
                self.currentDirection = tkinter.W
                self.headCell.grid(column=self.headCell.grid_info()["column"]+1)
            case 40:
                self.currentDirection = tkinter.S
                self.headCell.grid(row=self.headCell.grid_info()["row"]+1)

    def nextRandomTargetPosition(self):
        return random.randint(0, SundiWindow.MAX_X-1), random.randint(0, SundiWindow.MAX_Y-1)

    def crawlSundi(self):
        while True:
            print(self.gameStarted)
            if self.gameStarted:
                match self.currentDirection:
                    case tkinter.N:
                        self.headCell.grid(row=self.headCell.grid_info()["row"]-1)
                    case tkinter.S:
                        self.headCell.grid(row=self.headCell.grid_info()["row"]+1)
                    case tkinter.W:
                        self.headCell.grid(column=self.headCell.grid_info()["column"]+1)
                    case tkinter.E:
                        self.headCell.grid(column=self.headCell.grid_info()["column"]-1)

                if self.headCell.grid_info()["row"] == self.targetCell.grid_info()["row"] \
                        and self.headCell.grid_info()["column"] == self.targetCell.grid_info()["column"]:
                    newTargetPosition: (int, int) = self.nextRandomTargetPosition()
                    self.targetCell.grid(row=newTargetPosition[0], column=newTargetPosition[1])

            time.sleep(0.5) #500ms

SundiWindow().launch()
