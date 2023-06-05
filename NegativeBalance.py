from Balance import Balance


class NegativeBalance(Balance):

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value > 0:
            value = value * (-1)
        self._balance = value