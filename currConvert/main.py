import tkinter as tk
from forex_python.converter import CurrencyRates

common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'NZD']


class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('200x180')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('USD')
