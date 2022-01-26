import scipy.stats
import random
from com.vigs.games.rockpaperscissor.model.Choice import Choice
from typing import Final


class PredictionModel:

    __INPUT_OPTIONS: Final = [Choice.ROCK, Choice.PAPER, Choice.SCISSOR]

    def __init__(self):
        self.__userSelectionHistory = []
        self.__computerSelectionHistory = []
        self.__predictionHistory = []

    def updateStats(self, userSelection: Choice, computerSelection: Choice):
        if userSelection is not None:
            self.__userSelectionHistory.append(userSelection.value)

        if computerSelection is not None:
            self.__computerSelectionHistory.append(computerSelection.value)

    def __generateRandomChoice(self):
        randomNum = random.randint(0, 2)
        print(randomNum)
        randomChoice = self.__INPUT_OPTIONS[randomNum]
        print("randomNum:", randomNum, ", randomChoice:", randomChoice)
        return randomChoice

    def __modeAll(self):
        modeAll = None
        if len(self.__userSelectionHistory) > 0:
            print("MODE:", scipy.stats.mode(self.__userSelectionHistory))
            modeAll = Choice.forValue(scipy.stats.mode(self.__userSelectionHistory))
        return modeAll

    def predict(self):
        randomChoice = self.__generateRandomChoice()
        modeAll = self.__modeAll()
        return randomChoice

