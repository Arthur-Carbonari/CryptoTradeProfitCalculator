from PyQt6.QtCore import QDate, pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QLabel, QCalendarWidget, QSpinBox, QFormLayout, QHBoxLayout, QWidget


class CalendarGroupBox(QWidget):

    purchase_date = None
    purchase_date_update = pyqtSignal()

    sale_date = None
    sale_date_update = pyqtSignal()

    dates = []

    def __init__(self):

        super(CalendarGroupBox, self).__init__()

        # Create CalendarWidgets for selection of purchase and sell dates:
        self.purchase_date_calendar = QCalendarWidget()
        self.purchase_date_calendar.setDisabled(True)

        self.sale_date_calendar = QCalendarWidget()
        self.sale_date_calendar.setDisabled(True)

        # Connecting signals to slots to that a change in one control updates the UI
        self.purchase_date_calendar.selectionChanged.connect(self._update_purchase_date)
        self.sale_date_calendar.selectionChanged.connect(self._update_sale_date)

        self.init_ui()

    def init_ui(self):
        # Create inner groupboxes
        groupbox_purchase = QGroupBox("Purchase")
        groupbox_sell = QGroupBox("Sale")

        # Set purchase GroupBox layout
        purchase_layout = QFormLayout()
        purchase_layout.addRow(QLabel("Date Purchased:"), self.purchase_date_calendar)
        groupbox_purchase.setLayout(purchase_layout)

        # Set Sale GroupBox layout TODO: add sale quantity spinner and connect it to the rest of the application logic
        sale_layout = QFormLayout()
        sale_layout.addRow(QLabel("Date Sold:"), self.sale_date_calendar)
        groupbox_sell.setLayout(sale_layout)

        # Set the main layout for the GroupBox
        main_layout = QHBoxLayout()
        main_layout.addWidget(groupbox_purchase)
        main_layout.addWidget(groupbox_sell)
        self.setLayout(main_layout)

    def update_dates(self, dates):
        self.dates = dates

        min_date: QDate = dates[0]
        max_date: QDate = dates[-1]

        if not self.purchase_date:
            self.purchase_date_calendar.setDisabled(False)
            self.purchase_date_calendar.setDateRange(min_date, max_date)
            self.purchase_date_calendar.setSelectedDate(dates[-15])
            return

        old_date = self.purchase_date
        self.purchase_date_calendar.setDateRange(min_date, max_date)

        if min_date <= old_date <= max_date:
            self.purchase_date_calendar.selectionChanged.emit()

    def _update_purchase_date(self):
        self.purchase_date = self.purchase_date_calendar.selectedDate()
        self.purchase_date_update.emit()
        self._update_sale_dates()

    def _update_sale_dates(self):

        min_date = self.purchase_date
        max_date = self.dates[-1]

        if not self.sale_date:
            self.sale_date_calendar.setDisabled(False)
            self.sale_date_calendar.setDateRange(min_date, max_date)
            self.sale_date_calendar.setSelectedDate(max_date)
            return

        old_date = self.sale_date
        self.sale_date_calendar.setDateRange(min_date, max_date)

        if min_date <= old_date <= max_date:
            self.sale_date_calendar.selectionChanged.emit()

    def _update_sale_date(self):
        self.sale_date = self.sale_date_calendar.selectedDate()
        self.sale_date_update.emit()

