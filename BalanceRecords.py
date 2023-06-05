from Balance import Balance
from NegativeBalance import NegativeBalance
from PositiveBalance import PositiveBalance


class BalanceRecords:
    def __init__(self, values=[]):
        self._balance = values

    @property
    def balance(self):
        return self._balance


    def add_balance(self, value:str):

        # if self._balance:
        #     balance = self._balance + list(value)
        if value >= 0:
            value = PositiveBalance(value)
        else:
            value = NegativeBalance(value)
        self._balance.append(value)
        # self._balance.append(value)
