from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel, QSpinBox, QGridLayout, QFormLayout, QGroupBox


class CurrencyBox(QWidget):

    currency = None
    currency_update = pyqtSignal()

    quantity = 1
    quantity_update = pyqtSignal()

    def __init__(self, currencies):

        super(CurrencyBox, self).__init__()

        # Create QComboBox and populate it with a list of CryptoCurrencies
        self.select_currency_combobox = QComboBox()
        self.select_currency_combobox.setPlaceholderText("Please select a coin")
        self.select_currency_combobox.addItems(currencies)

        # Create QSpinBox to select CryptoCurrency quantity purchased
        self.quantity_purchased_spinbox = QSpinBox()
        self.quantity_purchased_spinbox.setValue(1)

        self.select_currency_combobox.currentTextChanged.connect(self.update_currency)
        self.quantity_purchased_spinbox.valueChanged.connect(self._update_purchase_quantity)

        self.init_ui()

    def init_ui(self):
        form_layout = QFormLayout()
        form_layout.setSpacing(20)
        form_layout.addRow(QLabel("Crypto-Currency Purchased:"), self.select_currency_combobox)
        form_layout.addRow(QLabel("Quantity Purchased:"), self.quantity_purchased_spinbox)

        wrapper_layout = QHBoxLayout()
        wrapper_layout.addLayout(form_layout, 4)
        wrapper_layout.addStretch(5)
        self.setLayout(wrapper_layout)

    def update_currency(self):
        self.currency = self.select_currency_combobox.currentText()
        self.currency_update.emit()

    def _update_purchase_quantity(self):
        self.quantity = self.quantity_purchased_spinbox.value()
        self.quantity_update.emit()