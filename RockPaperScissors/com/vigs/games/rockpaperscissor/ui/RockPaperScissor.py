import tkinter

from com.vigs.games.rockpaperscissor.ui.ScrollableFrame import ScrollableFrame


class RockPaperScissor:
    def __init__(self):
        pass

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
        self.btnComputerSelection = tkinter.Button(self.frmPlayInstance, text="Rock", width=20, state="disabled", justify=tkinter.CENTER)
        self.btnPlayerSelection = tkinter.Button(self.frmPlayInstance, text="Scissor", width=20, state="disabled", justify=tkinter.CENTER)

        tkinter.Label(self.frmPlayInstance, height=20).grid(row=0, column=0, columnspan=3)
        self.btnComputerSelection.grid(row=1, column=0, sticky=tkinter.NSEW, padx=10)
        tkinter.Frame(self.frmPlayInstance, width=50).grid(row=1, column=1, sticky=tkinter.NSEW)
        self.btnPlayerSelection.grid(row=1, column=2, sticky=tkinter.NSEW, padx=10)
        self.frmPlayInstance.grid(row=1, column=0, sticky=tkinter.NSEW)
        return self.frmPlayInstance

    def buildPlayInstanceFrame(self, masterFrame):
        frmPlayInstance = tkinter.Frame(master=masterFrame)
        btnComputerSelection = tkinter.Button(frmPlayInstance, text="Rock", width=20, state="disabled", justify=tkinter.CENTER)
        btnPlayerSelection = tkinter.Button(frmPlayInstance, text="Scissor", width=20, state="disabled", justify=tkinter.CENTER)

        btnComputerSelection.grid(row=0, column=0, sticky=tkinter.NSEW, padx=10)
        tkinter.Frame(frmPlayInstance, width=50).grid(row=0, column=1, sticky=tkinter.NSEW)
        btnPlayerSelection.grid(row=0, column=2, sticky=tkinter.NSEW, padx=10)

        return frmPlayInstance

    def buildPlayHistoryFrame_Scrollable(self):
        self.frmPlayHistory = tkinter.Frame(self.root, height=200, width=100)
        self.frmPlayHistory.grid(row=1, column=0)

        self.frmScrollable = ScrollableFrame(self.frmPlayHistory, ScrollableFrame.VERTICAL)

        for i in range(40):
            self.frmScrollable.add(self.buildPlayInstanceFrame(self.frmScrollable.frameForChildComponents))


RockPaperScissor().build()