from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel


class CurrencyBox(QWidget):

    selected_currency = None
    currency_update = pyqtSignal()

    def __init__(self, currencies):

        super(CurrencyBox, self).__init__()

        # Create QComboBox and populate it with a list of CryptoCurrencies
        self.select_currency_combobox = QComboBox()
        self.select_currency_combobox.setPlaceholderText("Please select a coin")
        self.select_currency_combobox.addItems(currencies)

        self.set_up_ui()

    def set_up_ui(self):
        currency_layout = QHBoxLayout()
        currency_layout.setSpacing(10)
        currency_layout.addWidget(QLabel("Crypto-Currency Purchased:"))
        currency_layout.addWidget(self.select_currency_combobox, 3)
        currency_layout.addStretch(4)