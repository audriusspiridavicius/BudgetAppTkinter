from MainForm import MainForm
from BalanceRecords import BalanceRecords
from NegativeBalance import NegativeBalance
from PositiveBalance import PositiveBalance
b = BalanceRecords()
b1 = b.balance


app = MainForm()

app.geometry("300x250+400+200")

app.display()

app.mainloop()