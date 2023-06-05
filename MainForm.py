import tkinter
from tkinter import *

from typing import List

from Balance import Balance
from BalanceRecords import BalanceRecords


class MainForm(Tk):
    def __init__(self):
        super().__init__()

        self.balance:BalanceRecords = BalanceRecords()

        # enter value section
        self.frame = tkinter.Frame(self)
        self.number_entry_label = Label(self.frame, text="Irasykite suma", anchor="e")
        self.number_entry = Entry(self.frame)
        self.calculate_button = Button(self.frame, text="Ivesti", anchor="w", command=self.add_balanceentry)
        self.number_entry.bind("<Return>", self.add_balanceentry)
        # balance form section

        self.balance_label = Label(self.frame, text="balansas")
        self.balance_value_label = Label(self.frame)
        self.clear_button = Button(self.frame, text="isvalyti")

        # entered balance values list

        self.balance_list = Listbox(self.frame, height=5)

    def display(self):
        self.frame.grid()

        self.number_entry_label.grid(row=0, column=0)
        self.number_entry.grid(row=0, column=1)
        self.calculate_button.grid(row=0, column=2)

        self.balance_label.grid(row=1, column=1)
        self.balance_value_label.grid(row=1, column=2)

        self.clear_button.grid(row=2, column=2)

        self.balance_list.grid(row=3, column=1, rowspan=3, pady=15)

    def add_balanceentry(self, *args):

        value = self.number_entry.get()
        try:
            value = float(value)
        except ValueError:
            value = 0
        except TypeError:
            value = 0
        self._balance = value




        self.balance.add_balance(value)
        self.balance_list.insert(END, value)
        print("function add balance entry called")
        print(self.balance.balance)
