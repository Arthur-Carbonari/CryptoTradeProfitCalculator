from PyQt6.QtWidgets import QGroupBox, QLabel, QFormLayout


class AnalysesGroupBox(QGroupBox):
    def __init__(self):

        super(AnalysesGroupBox, self).__init__("Purchase")
        self.quantity = 1
        self.purchase_cost = 0
        self.sale_cost = 0

        # Create QLabels to show the CryptoCurrency purchase total
        total_purchased_label = QLabel("Total Purchased:")
        self.total_purchased = QLabel("$$.$$")

        # Create QLabels to show the CryptoCurrency sell total
        total_sold_label = QLabel("Total Sold:")
        self.total_sold = QLabel("$$.$$")

        # Create QLabels to show the CryptoCurrency profit total
        total_profit_label = QLabel("Total Profit:")
        self.total_profit = QLabel("$$.$$")

        # Set GroupBox layout
        analyses_layout = QFormLayout()
        analyses_layout.addRow(total_purchased_label, self.total_purchased)
        analyses_layout.addRow(total_sold_label, self.total_sold)
        analyses_layout.addRow(total_profit_label, self.total_profit)

        self.setLayout(analyses_layout)

    def update_quantity(self, quantity):
        self.quantity = quantity
        self.__update_total_purchased()
        self.__update_total_sale()

    def update_purchase_cost(self, purchase_cost):
        self.purchase_cost = purchase_cost
        self.__update_total_purchased()

    def update_sale_cost(self, sale_cost):
        self.sale_cost = sale_cost
        self.__update_total_sale()

    def __update_total_purchased(self):
        total = str(self.quantity * self.purchase_cost)
        self.total_purchased.setText("US$ " + total)
        self.__update_total_profit()

    def __update_total_sale(self):
        total = str(self.quantity * self.sale_cost)
        self.total_sold.setText("US$ " + total)
        self.__update_total_profit()

    def __update_total_profit(self):
        total = str(self.quantity * (self.sale_cost - self.purchase_cost))
        self.total_profit.setText("US$ " + total)
