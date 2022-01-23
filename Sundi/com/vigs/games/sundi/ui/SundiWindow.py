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
        self.gameOver = False

    def launch(self):
        self.build()
        self.registerEventHandlers()

        crawlSundiThread = threading.Thread(name="CrawlSundiThread", target=self.crawlSundi)
        crawlSundiThread.start()

        self.root.mainloop()

    def build(self):
        self.root = tkinter.Tk()
        self.root.title("Lets play Sundi!!")

        self.sundiGridFrame = tkinter.Frame(self.root, height=100, width=100, borderwidth=20)
        self.sundiGridFrame.grid(row=0, column=0)

        self.drawGrid()

        self.headCell = self.drawCell(color="red", position=(5, 5))
        self.targetCell = self.drawCell(color="blue", position=self.nextRandomTargetPosition())

        self.sundi.append(self.headCell)


    def drawGrid(self):
        for x in range(SundiWindow.MAX_X):
            for y in range(SundiWindow.MAX_Y):
                self.drawCell(color="gray", position=(x, y))

    def drawCell(self, color: str, position: (int, int)):
        sundiCell = tkinter.Label(self.sundiGridFrame, width=self.cellwidth, height=self.cellheight)
        sundiCell.configure(borderwidth=2, background=color, relief="groove")
        sundiCell.grid(row=position[0], column=position[1])
        return sundiCell

    def drawSundi(self):
        for sundiCell in self.sundi:
            pass

    def registerEventHandlers(self):
        self.root.bind("<KeyPress>", self.keyPressed)
        self.headCell.bind("<Configure>", self.headCellMoved)

    def keyPressed(self, event: tkinter.Event):
        print("Key Pressed", event)

        print(self.headCell.grid_info())

        self.gameStarted = True

        if not self.gameOver:
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


    def headCellMoved(self, event: tkinter.Event):
        row = self.headCell.grid_info()["row"]
        column = self.headCell.grid_info()["column"]
        self.detectGameOver(row=row, column=column)


    def nextRandomTargetPosition(self):
        return random.randint(0, SundiWindow.MAX_X-1), random.randint(0, SundiWindow.MAX_Y-1)

    def detectGameOver(self, row: int, column: int):
        if row < 0 or column < 0 or row >= SundiWindow.MAX_X or column >= SundiWindow.MAX_Y:
            print("GAME OVER!!!!")
            self.root.title("GAME OVER!!")
            self.gameOver = True
            return True # yes, the game is over

        return False #no, the game is not over


    def crawlSundi(self):
        while True:
            time.sleep(0.1) #100ms
            print(self.gameStarted)
            if self.gameStarted and not self.gameOver:
                row = self.headCell.grid_info()["row"]
                column = self.headCell.grid_info()["column"]

                newRow = row
                newColumn = column

                rowIncrement = 0
                columnIncrement = 0

                match self.currentDirection:
                    case tkinter.N:
                        newRow = row-1
                        rowIncrement = -1
                    case tkinter.S:
                        newRow = row+1
                        rowIncrement = 1
                    case tkinter.W:
                        newColumn = column+1
                        columnIncrement = 1
                    case tkinter.E:
                        newColumn = column-1
                        columnIncrement = -1

                if self.detectGameOver(row=newRow, column=newColumn) is not True:
                    for cellIndex in range(len(self.sundi)-1, 0, -1): ##headCell will be excluded and thats what we want
                        sundiCell: tkinter.Label = self.sundi[cellIndex]
                        sundiCellNext: tkinter.Label = self.sundi[cellIndex-1]
                        nextRow = sundiCellNext.grid_info()["row"]
                        nextColumn = sundiCellNext.grid_info()["column"]
                        sundiCell.grid(row=nextRow, column=nextColumn)

                    self.headCell.grid(row=newRow, column=newColumn) ##move the head forward


                if self.headCell.grid_info()["row"] == self.targetCell.grid_info()["row"] \
                        and self.headCell.grid_info()["column"] == self.targetCell.grid_info()["column"]:
                    self.consumeTarget()



    def consumeTarget(self):
        newTargetPosition: (int, int) = self.nextRandomTargetPosition()
        self.targetCell.grid(row=newTargetPosition[0], column=newTargetPosition[1])

        tailCell: tkinter.Label = self.sundi[len(self.sundi)-1]
        row_NewCell = tailCell.grid_info()["row"]
        column_NewCell = tailCell.grid_info()["column"]

        match self.currentDirection:
            case tkinter.N:
                row_NewCell -= 1
            case tkinter.S:
                row_NewCell += 1
            case tkinter.W:
                column_NewCell += 1
            case tkinter.E:
                column_NewCell -= 1

        newTailCell = self.drawCell(color="red", position=(row_NewCell, column_NewCell))
        self.sundi.append(newTailCell)







SundiWindow().launch()

