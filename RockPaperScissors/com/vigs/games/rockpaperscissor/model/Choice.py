from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @staticmethod
    def forValue(value: int):
        for item in Choice:
            if item.value == value:
                return item
        return None




