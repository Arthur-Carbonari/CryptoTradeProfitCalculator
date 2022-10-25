from PyQt6.QtCore import QDate, pyqtSignal
from PyQt6.QtWidgets import QGroupBox, QLabel, QCalendarWidget, QFormLayout, QHBoxLayout, QWidget


class CalendarBox(QWidget):

    purchase_date = None
    '''QDate corresponding to the current selected date on the purchase calendar'''

    purchase_date_update = pyqtSignal()
    '''Signal emitted when the purchase_date variable has changed value'''

    sale_date = None
    '''QDate corresponding to the current selected date on the sale calendar'''

    sale_date_update = pyqtSignal()
    '''Signal emitted when the sale_date variable has changed value'''

    _dates = []
    '''Variable that stores all the dates'''

    def __init__(self):
        """Initializes the purchase and sale calendar widget, calls the init_ui method to set up the layout"""

        super(CalendarBox, self).__init__()

        # Create CalendarWidgets for selection of purchase and sell dates:
        self.purchase_date_calendar = QCalendarWidget()
        self.purchase_date_calendar.setDisabled(True)

        self.sale_date_calendar = QCalendarWidget()
        self.sale_date_calendar.setDisabled(True)

        # Connecting signals to slots to that a change in one control updates the UI
        self.purchase_date_calendar.selectionChanged.connect(self._update_purchase_date)
        self.sale_date_calendar.selectionChanged.connect(self._update_sale_date)

        self._init_ui()

    def _init_ui(self):
        """
        This method, initializes and sets up the UI layout for this Dialog
        :return: void
        """

        # Create inner groupboxes
        groupbox_purchase = QGroupBox("Purchase")
        groupbox_sell = QGroupBox("Sale")

        # Set purchase GroupBox layout
        purchase_layout = QFormLayout()
        purchase_layout.addRow(QLabel("Date Purchased:"), self.purchase_date_calendar)
        groupbox_purchase.setLayout(purchase_layout)

        # Set Sale GroupBox layout
        sale_layout = QFormLayout()
        sale_layout.addRow(QLabel("Date Sold:"), self.sale_date_calendar)
        groupbox_sell.setLayout(sale_layout)

        # Set the main layout for the GroupBox
        main_layout = QHBoxLayout()
        main_layout.addWidget(groupbox_purchase)
        main_layout.addWidget(groupbox_sell)
        self.setLayout(main_layout)

    def update_dates(self, dates):
        """
        This method will set this object dates var and update the max and min date of the purchase calendar accordingly
        :param dates: new dates
        :return: void
        """

        # Set dates var
        self._dates = dates

        # Get the min and max date
        min_date: QDate = dates[0]
        max_date: QDate = dates[-1]

        # If this was the first time this method was called this will enable the calendar and set the date to default
        if not self.purchase_date:
            self.purchase_date_calendar.setDisabled(False)
            self.purchase_date_calendar.setDateRange(min_date, max_date)
            self.purchase_date_calendar.setSelectedDate(dates[-15])
            return

        old_date = self.purchase_date
        self.purchase_date_calendar.setDateRange(min_date, max_date)

        # if the date hasn't changed this will still emit the selection changed signal
        if min_date <= old_date <= max_date:
            self.purchase_date_calendar.selectionChanged.emit()

    def _update_purchase_date(self):
        """
        This method sets the purchase_date variable to the current date in the purchase_calendar, then emits the
        purchase_date_update signal and calls the update_sale_dates method
        :return: void
        """
        self.purchase_date = self.purchase_date_calendar.selectedDate()
        self.purchase_date_update.emit()
        self._update_sale_dates()

    def _update_sale_dates(self):
        """
        This method updates the min and max dates of the sale_calendar
        if it was disabled it enables it and then sets the date to the max_date as default
        :return: void
        """

        # get the min and max date, min date is the date of purchase
        min_date = self.purchase_date
        max_date = self._dates[-1]

        # if this is the first time called it enables the calendar and sets the date to default
        if not self.sale_date:
            self.sale_date_calendar.setDisabled(False)
            self.sale_date_calendar.setDateRange(min_date, max_date)
            self.sale_date_calendar.setSelectedDate(max_date)
            return

        old_date = self.sale_date

        # sets the range
        self.sale_date_calendar.setDateRange(min_date, max_date)

        # if the date has not changed it manually emits the selectionChanged signal
        if min_date <= old_date <= max_date:
            self.sale_date_calendar.selectionChanged.emit()

    def _update_sale_date(self):
        """
        This method sets the sale_date variable to the current date in the sale_calendar, then emits the
        sale_date_update signal
        :return: void
        """
        self.sale_date = self.sale_date_calendar.selectedDate()
        self.sale_date_update.emit()

