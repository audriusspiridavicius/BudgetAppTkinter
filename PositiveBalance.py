from Balance import Balance


class PositiveBalance(Balance):
    def __init__(self, balance = 0):
        super().__init__(balance)

    @property
    def balance(self):
        return super().balance

    @balance.setter
    def balance(self, value):
        # self._balance = abs(value)
        self._balance = abs(value)