from PyQt6.QtWidgets import QGroupBox, QLabel, QFormLayout


class AnalysesGroupBox(QGroupBox):
    def __init__(self):

        super(AnalysesGroupBox, self).__init__("Analysis")
        self.quantity = 1
        self.purchase_cost = 0
        self.sale_cost = 0

        # Create QLabel to show the CryptoCurrency purchase total
        self.total_purchased = QLabel("$00.00")

        # Create QLabel to show the CryptoCurrency sell total
        self.total_sold = QLabel("$00.00")

        # Create QLabel to show the CryptoCurrency profit total
        self.total_profit = QLabel("$00.00")

        # Create QLabel to show the variance percentage
        self.total_variance = QLabel("00.00%")

        self.init_ui()

    def init_ui(self):

        # Set GroupBox layout
        analyses_layout = QFormLayout()
        analyses_layout.addRow("Total Purchased:", self.total_purchased)
        analyses_layout.addRow("Total Sold:", self.total_sold)
        analyses_layout.addRow("Total Profit:", self.total_profit)
        analyses_layout.addRow("Total Variance:", self.total_variance)

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
        total = self.quantity * self.purchase_cost
        self.total_purchased.setText('${:,.2f}'.format(total))
        self.__update_total_profit()
        self.__update_total_variance()

    def __update_total_sale(self):
        total = self.quantity * self.sale_cost
        self.total_sold.setText('${:,.2f}'.format(total))
        self.__update_total_profit()
        self.__update_total_variance()

    def __update_total_profit(self):
        total = self.quantity * (self.sale_cost - self.purchase_cost)
        self.total_profit.setText('${:,.2f}'.format(total))

    def __update_total_variance(self):
        total = self.sale_cost / self.purchase_cost - 1
        self.total_variance.setText('{:,.2f}%'.format(total))
