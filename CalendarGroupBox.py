from PyQt6.QtCore import QDate, pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QLabel, QCalendarWidget, QSpinBox, QFormLayout, QSplitter, QHBoxLayout


class CalendarGroupBox(QGroupBox):

    purchase_quantity = 1
    purchase_quantity_updated = pyqtSignal()

    purchase_date: QDate
    purchase_date_update = pyqtSignal()

    sale_date: QDate
    sale_date_update = pyqtSignal()

    dates = []

    def __init__(self):

        super(CalendarGroupBox, self).__init__()

        # TODO: create CalendarWidgets for selection of purchase and sell dates
        purchase_date_label = QLabel("Date Purchased:")
        self.purchase_date_calendar = QCalendarWidget()
        self.purchase_date_calendar.setDisabled(True)

        sell_date_label = QLabel("Date Sold:")
        self.sale_date_calendar = QCalendarWidget()
        self.sale_date_calendar.setDisabled(True)

        # TODO: create QSpinBox to select CryptoCurrency quantity purchased
        quantity_purchased_label = QLabel("Quantity Purchased:")
        self.quantity_purchased_spinbox = QSpinBox()
        self.quantity_purchased_spinbox.setValue(1)

        # Connecting signals to slots to that a change in one control updates the UI
        self.purchase_date_calendar.selectionChanged.connect(self._update_purchase_date)
        self.sale_date_calendar.selectionChanged.connect(self._update_sale_date)
        self.quantity_purchased_spinbox.valueChanged.connect(self._update_purchase_quantity)

        groupbox_purchase = QGroupBox("Purchase")
        groupbox_sell = QGroupBox("Sale")

        # Set purchase GroupBox layout
        purchase_layout = QFormLayout()
        purchase_layout.addRow(quantity_purchased_label, self.quantity_purchased_spinbox)
        purchase_layout.addRow(purchase_date_label, self.purchase_date_calendar)

        groupbox_purchase.setLayout(purchase_layout)

        # Set sale GroupBox layout
        sale_layout = QFormLayout()
        # sale_layout.addRow(quantity_purchased_label, quantity_purchased_spinbox)
        sale_layout.addRow(sell_date_label, self.sale_date_calendar)

        groupbox_sell.setLayout(sale_layout)

        splitter = QSplitter()

        splitter.addWidget(groupbox_purchase)
        splitter.addWidget(groupbox_sell)

        group_layout = QHBoxLayout()
        group_layout.addWidget(splitter)
        self.setLayout(group_layout)

    def update_dates(self, dates):
        self.dates = dates

        self.purchase_date_calendar.setDisabled(False)
        self.sale_date_calendar.setDisabled(False)

        min_date: QDate = dates[0]
        max_date: QDate = dates[-1]

        self.purchase_date_calendar.setDateRange(min_date, max_date)

        if min_date <= self.purchase_date <= max_date:
            self.purchase_date_calendar.selectionChanged.emit()
        else:
            self.purchase_date_calendar.setSelectedDate(dates[-15])
