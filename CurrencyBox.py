from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel, QSpinBox, QFormLayout


class CurrencyBox(QWidget):

    currency: str = None
    '''String corresponding to the code for the current selected currency on the combobox widget'''

    currency_update = pyqtSignal()
    '''Signal emitted when the currency variable has changed value'''

    quantity = 1
    '''Int value corresponding to the value in the quantity spinner-box widget'''

    quantity_update = pyqtSignal()
    '''Signal emitted when the quantity variable has changed value'''

    def __init__(self, currencies):
        """
        Initializes the combobox and spinbox widget, calls the init_ui method to set up the layout
        :param currencies: List containing the currencies options to be used in the combobox
        """

        super(CurrencyBox, self).__init__()

        # Create QComboBox and populate it with a list of CryptoCurrencies
        self.select_currency_combobox = QComboBox()
        self.select_currency_combobox.setPlaceholderText("Please select a coin")
        self.select_currency_combobox.addItems(currencies)

        # Create QSpinBox to select CryptoCurrency quantity purchased
        self.quantity_purchased_spinbox = QSpinBox()
        self.quantity_purchased_spinbox.setValue(1)

        # Connecting signals to slots to that a change in one control updates the corresponding class variables
        self.select_currency_combobox.currentTextChanged.connect(self._update_currency)
        self.quantity_purchased_spinbox.valueChanged.connect(self._update_purchase_quantity)

        self._init_ui()

    def _init_ui(self):
        """
        This method, initializes and sets up the UI layout for this Dialog
        :return: void
        """

        # Initializes the form layout
        form_layout = QFormLayout()
        form_layout.setSpacing(20)
        form_layout.addRow(QLabel("Crypto-Currency Purchased:"), self.select_currency_combobox)
        form_layout.addRow(QLabel("Quantity Purchased:"), self.quantity_purchased_spinbox)

        # Adds the form layout to a wrapper layout (used to add a stretch to it)
        wrapper_layout = QHBoxLayout()
        wrapper_layout.addLayout(form_layout, 4)
        wrapper_layout.addStretch(5)

        # Sets the class layout
        self.setLayout(wrapper_layout)

    def _update_currency(self):
        """
        This method updates the currency instance variable to the current one selected in the combobox, and emits this
        object's currency_update signal.
        This is called when the combobox currentTextChanged signal is emitted.
        :return: void
        """

        self.currency = self.select_currency_combobox.currentText()
        self.currency_update.emit()

    def _update_purchase_quantity(self):
        """
        This method updates the quantity instance variable to the current value of the spinbox, and emits this object's
        quantity_update signal.
        This is called when the spinbox valueChanged signal is emitted.
        :return: void
        """

        self.quantity = self.quantity_purchased_spinbox.value()
        self.quantity_update.emit()
