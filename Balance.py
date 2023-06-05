class Balance:
    def __init__(self, value=0):
        self.balance = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        try:
            value = float(value)
        except ValueError:
            value = 0
        except TypeError:
            value = 0
        self._balance = value

    def __str__(self):
        return f"{self.balance}"
