import random
from typing import Final
import tkinter

from com.vigs.games.rockpaperscissor.ui.ScrollableFrame import ScrollableFrame


class RockPaperScissor:
    ROCK: Final[str] = "ROCK"
    PAPER: Final[str] = "PAPER"
    SCISSOR: Final[str] = "SCISSOR"

    INPUT_OPTIONS: Final = [ROCK, PAPER, SCISSOR]

    COMPUTER: Final[str] = "COMPUTER"
    USER: Final[str] = "USER"



    def __init__(self):
        self.userScore: int = 0
        self.computerScore: int = 0

    def launch(self):
        self.build()

    def build(self):
        self.root = tkinter.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.grid(baseWidth=200, baseHeight=480, widthInc=200, heightInc=480)

        self.buildPlayerScorecardFrame()

        ################################################################

        self.buildPlayHistoryFrame_Scrollable()

        ################################################################

        self.frmEmpty = tkinter.Frame(self.root, height=20)
        self.frmEmpty.grid(row=2, column=0)

        ################################################################
        self.buildPlayButtonsFrame()

        self.setEventHandlers()
        self.root.mainloop()

    def buildPlayerScorecardFrame(self):
        self.frmPlayerNames = tkinter.Frame(self.root)
        self.lblPlayerName1 = tkinter.Label(self.frmPlayerNames, text="Player1\n(Computer)", width=20, font="bold")
        self.lblPlayerName2 = tkinter.Label(self.frmPlayerNames, text="Player2\n(You)", width=20, font="bold")
        self.lblPlayerScore1 = tkinter.Label(self.frmPlayerNames, text="0", width=20, font="bold")
        self.lblPlayerScore2 = tkinter.Label(self.frmPlayerNames, text="0", width=20, font="bold")

        self.lblPlayerName1.grid(row=0, column=0, sticky=tkinter.NSEW)
        tkinter.Frame(self.frmPlayerNames, width=50).grid(row=0, column=1, sticky=tkinter.NSEW)
        self.lblPlayerName2.grid(row=0, column=2, sticky=tkinter.NSEW)

        self.lblPlayerScore1.grid(row=1, column=0, sticky=tkinter.NSEW)
        tkinter.Frame(self.frmPlayerNames, width=50).grid(row=0, column=1, sticky=tkinter.NSEW)
        self.lblPlayerScore2.grid(row=1, column=2, sticky=tkinter.NSEW)
        self.frmPlayerNames.grid(row=0, column=0, sticky=tkinter.NSEW)

    def buildPlayButtonsFrame(self):
        self.frmOptions = tkinter.Frame(self.root)
        self.btnRock = tkinter.Button(self.frmOptions, text="Rock", font="bold")
        self.btnPaper = tkinter.Button(self.frmOptions, text="Paper", font="bold")
        self.btnScissor = tkinter.Button(self.frmOptions, text="Scissor", font="bold")

        self.btnRock.grid(row=0, column=0, sticky=tkinter.NSEW, padx=10)
        self.btnPaper.grid(row=0, column=1, sticky=tkinter.NSEW, padx=10)
        self.btnScissor.grid(row=0, column=2, sticky=tkinter.NSEW, padx=10)

        self.frmOptions.grid(row=3, column=0)

    def buildPlayHistoryFrame_V1(self, master):
        self.frmPlayInstance = tkinter.Frame(master, height=400, borderwidth=2, background="white")
        self.btnComputerSelection = tkinter.Button(self.frmPlayInstance, text="Rock", width=20, state="disabled",
                                                   justify=tkinter.CENTER)
        self.btnPlayerSelection = tkinter.Button(self.frmPlayInstance, text="Scissor", width=20, state="disabled",
                                                 justify=tkinter.CENTER)

        tkinter.Label(self.frmPlayInstance, height=20).grid(row=0, column=0, columnspan=3)
        self.btnComputerSelection.grid(row=1, column=0, sticky=tkinter.NSEW, padx=10)
        tkinter.Frame(self.frmPlayInstance, width=50).grid(row=1, column=1, sticky=tkinter.NSEW)
        self.btnPlayerSelection.grid(row=1, column=2, sticky=tkinter.NSEW, padx=10)
        self.frmPlayInstance.grid(row=1, column=0, sticky=tkinter.NSEW)
        return self.frmPlayInstance

    def buildPlayInstanceFrame(self, masterFrame, userSelection:str, computerSelection:str):
        self.frmPlayInstance = tkinter.Frame(master=masterFrame)
        self.btnComputerSelection = tkinter.Button(self.frmPlayInstance, text=computerSelection, width=20, state="normal",
                                                   justify=tkinter.CENTER)
        self.btnPlayerSelection = tkinter.Button(self.frmPlayInstance, text=userSelection, width=20, state="normal",
                                                 justify=tkinter.CENTER)

        self.btnComputerSelection.grid(row=0, column=0, sticky=tkinter.NSEW, padx=10)
        tkinter.Frame(self.frmPlayInstance, width=50).grid(row=0, column=1, sticky=tkinter.NSEW)
        self.btnPlayerSelection.grid(row=0, column=2, sticky=tkinter.NSEW, padx=10)

        return self.frmPlayInstance

    def buildPlayHistoryFrame_Scrollable(self):
        self.frmPlayHistory = tkinter.Frame(self.root, height=200, width=100)
        self.frmPlayHistory.grid(row=1, column=0)

        self.frmScrollable = ScrollableFrame(self.frmPlayHistory, ScrollableFrame.VERTICAL)

        for i in range(-1):
            #self.frmScrollable.add(self.buildPlayInstanceFrame(self.frmScrollable.frameForChildComponents))
            self.playGame(self.ROCK)

    def setEventHandlers(self):
        self.btnRock.bind("<Button-1>", self.rockPressed)
        self.btnPaper.bind("<Button-1>", self.paperPressed)
        self.btnScissor.bind("<Button-1>", self.scissorPressed)

    def rockPressed(self, event: tkinter.Event):
        print("Rock Pressed")
        self.playGame(self.ROCK)

    def paperPressed(self, event: tkinter.Event):
        print("Paper Pressed")
        self.playGame(self.PAPER)

    def scissorPressed(self, event: tkinter.Event):
        print("Scissor Pressed")
        self.playGame(self.SCISSOR)

    def playGame(self, userSelection: str):
        computerSelection = self.generateComputerSelection()
        winner = self.getWinner(userSelection, computerSelection)

        self.frmScrollable.add(self.buildPlayInstanceFrame(self.frmScrollable.frameForChildComponents, userSelection, computerSelection))

        if winner == self.USER:
            self.btnPlayerSelection.configure(background="green")
            self.btnComputerSelection.configure(background="red")
            self.userScore += 1
        elif winner == self.COMPUTER:
            self.btnPlayerSelection.configure(background="red")
            self.btnComputerSelection.configure(background="green")
            self.computerScore += 1
        else: ## game draw
            self.btnPlayerSelection.configure(background="grey")
            self.btnComputerSelection.configure(background="grey")

        self.lblPlayerScore1.configure(text=self.computerScore)
        self.lblPlayerScore2.configure(text=self.userScore)


    def getWinner(self, userSelection, computerSelection):
        if userSelection == computerSelection:
            return None
        elif userSelection == self.ROCK and computerSelection == self.PAPER:
            return self.COMPUTER
        elif userSelection == self.ROCK and computerSelection == self.SCISSOR:
            return self.USER
        elif userSelection == self.PAPER and computerSelection == self.SCISSOR:
            return self.COMPUTER
        elif userSelection == self.PAPER and computerSelection == self.ROCK:
            return self.USER
        elif userSelection == self.SCISSOR and computerSelection == self.ROCK:
            return self.COMPUTER
        elif userSelection == self.SCISSOR and computerSelection == self.PAPER:
            return self.USER

        print("REACHING HERE MEANS PROBLEM!!! , A CASE HAS BEEN MISSED")

    def generateComputerSelection(self):
        randomNum = random.randint(0, 2)
        print(randomNum)
        return self.INPUT_OPTIONS[randomNum]


