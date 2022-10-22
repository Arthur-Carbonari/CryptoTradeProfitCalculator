from PyQt6.QtWidgets import QGroupBox, QLabel, QCalendarWidget, QSpinBox, QFormLayout, QSplitter, QHBoxLayout


class CalendarGroupBox(QGroupBox):

    def __init__(self):

        super(CalendarGroupBox, self).__init__()

        # TODO: create CalendarWidgets for selection of purchase and sell dates
        purchase_date_label = QLabel("Date Purchased:")
        self.purchase_date_calendar = QCalendarWidget()
        self.purchase_date_calendar.setDisabled(True)

        sell_date_label = QLabel("Date Sold:")
        self.sell_date_calendar = QCalendarWidget()
        self.sell_date_calendar.setDisabled(True)

        # TODO: create QSpinBox to select CryptoCurrency quantity purchased
        quantity_purchased_label = QLabel("Quantity Purchased:")
        quantity_purchased_spinbox = QSpinBox()
        quantity_purchased_spinbox.setValue(1)

        groupbox_purchase = QGroupBox("Purchase")
        groupbox_sell = QGroupBox("Sale")

        # Set purchase GroupBox layout
        purchase_layout = QFormLayout()
        purchase_layout.addRow(quantity_purchased_label, quantity_purchased_spinbox)
        purchase_layout.addRow(purchase_date_label, self.purchase_date_calendar)

        groupbox_purchase.setLayout(purchase_layout)

        # Set sale GroupBox layout
        sale_layout = QFormLayout()
        # sale_layout.addRow(quantity_purchased_label, quantity_purchased_spinbox)
        sale_layout.addRow(sell_date_label, self.sell_date_calendar)

        groupbox_sell.setLayout(sale_layout)

        splitter = QSplitter()

        splitter.addWidget(groupbox_purchase)
        splitter.addWidget(groupbox_sell)

        group_layout = QHBoxLayout()
        group_layout.addWidget(splitter)
        self.setLayout(group_layout)
