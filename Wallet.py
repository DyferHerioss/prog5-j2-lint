from Size import Size

class wallet:
    def __init__(self, color: str, size: Size, money: int, lostState: bool):
        self.color = color
        self.size = size
        self.money = money
        self.lostState = lostState

    def add_money(self, amountToAdd) -> int:
        self.money += amountToAdd
        return self.money

    def isLost(self) -> bool:
        return self.lostState

    def checkMoney(self) -> int:
        return self.money
