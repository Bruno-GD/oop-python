from logging import getLogger as gL
LOGGER = gL(__name__)
class Yatzy:
    """
    Yahtzee game score calculator
    """
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SCORES = {
        "FULLHOUSE": 25,
        "SMALLSTRAIGHT": 30,
        "LARGESTRAIGHT": 40,
        "YAHTZEE": 50
    }

    def __init__(self, *dices: int) -> None:
        # PUBLIC
        self.dices = list(dices)
        self.dices.sort()
        # PRIVATE
        self.COUNTS = dict.fromkeys([1,2,3,4,5,6], 0)
        for die in self.dices:
            self.COUNTS[die] += 1
        self.__max = None
        self.__min = None

    # UPPER SECTION
    def aces(self) -> int:
        """
        The sum of dice with the number 1
        """
        return self.COUNTS[self.ONE] * self.ONE

    def twos(self) -> int:
        """
        The sum of dice with the number 2
        """
        return self.COUNTS[self.TWO] * self.TWO

    def threes(self) -> int:
        """
        The sum of dice with the number 3
        """
        return self.COUNTS[self.THREE] * self.THREE

    def fours(self) -> int:
        """
        The sum of dice with the number 4
        """
        return self.COUNTS[self.FOUR] * self.FOUR

    def fives(self) -> int:
        """
        The sum of dice with the number 5
        """
        return self.COUNTS[self.FIVE] * self.FIVE

    def sixes(self) -> int:
        """
        The sum of dice with the number 6
        """
        return self.COUNTS[self.SIX] * self.SIX

    # LOWER SECTION
    def three_of_a_kind(self) -> int:
        """
        At least three dice the same
        Sum of all dice
        """
        maxDieCount = self.__maxDieCount()
        if self.COUNTS[maxDieCount] >= 3:
            return sum(self.dices)
        return 0

    def four_of_a_kind(self) -> int:
        """
        At least four dice the same
        Sum of all dice
        """
        maxDieCount = self.__maxDieCount()
        if self.COUNTS[maxDieCount] >= 4:
            return sum(self.dices)
        return 0

    def full_house(self) -> int:
        """
        Three of one number and two of another
        Scores 25
        """
        values = self.COUNTS.values()
        if 3 in values and 2 in values:
            return self.SCORES["FULLHOUSE"]
        return 0

    def small_straight(self) -> int:
        """
        Four sequential dice:
        (1-2-3-4, 2-3-4-5 or 3-4-5-6)
        Scores 30
        """
        start = 0
        lastDie = self.dices[start]
        if lastDie == self.dices[start+1]:
            start += 1
        for die in self.dices[start+1:5]:
            if lastDie + 1 != die:
                return 0
            lastDie = die
        return self.SCORES["SMALLSTRAIGHT"]

    def large_straight(self) -> int:
        """
        Five sequential dice:
        (1-2-3-4-5 or 2-3-4-5-6)
        Score 40
        """
        if self.dices == [1, 2, 3, 4, 5]:
            return self.SCORES["LARGESTRAIGHT"]
        elif self.dices == [2, 3, 4, 5, 6]:
            return self.SCORES["LARGESTRAIGHT"]
        else:
            return 0

    def yahtzee(self) -> int:
        """
        All five dice the same
        Score 50
        """
        higherDie = self.__maxDieCount()
        if self.COUNTS[higherDie] == 5:
            return self.SCORES["YAHTZEE"]
        else:
            return 0

    def chance(self) -> int:
        """
        Any combination
        Sum of all dice
        """
        return sum(self.dices)

    # PRIVATE
    def __maxDieCount(self) -> int:
        if self.__max == None:
            self.__max = max(self.COUNTS, key=lambda die: self.COUNTS[die])
        return self.__max
