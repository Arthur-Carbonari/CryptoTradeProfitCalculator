from PyQt6.QtWidgets import QGroupBox, QLabel, QFormLayout


class AnalysesBox(QGroupBox):
    def __init__(self):
        """
        Initializes the total purchase, sale, profit and variance QLabels widgets and calls the init_ui method to set up
        the layout
        """

        super(AnalysesBox, self).__init__("Analyses")
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

        self._init_ui()

    def _init_ui(self):
        """
        This method, initializes and sets up the UI layout for this Dialog
        :return: void
        """

        # Set box layout
        analyses_layout = QFormLayout()
        analyses_layout.addRow("Total Purchased:", self.total_purchased)
        analyses_layout.addRow("Total Sold:", self.total_sold)
        analyses_layout.addRow("Total Profit:", self.total_profit)
        analyses_layout.addRow("Total Variance:", self.total_variance)

        self.setLayout(analyses_layout)

    def update_quantity(self, quantity):
        """
        Updates the value of quantity and calls update_total_purchased and update_total_sale
        :param quantity: new purchase quantity of the coin
        :return: void
        """
        self.quantity = quantity
        self._update_total_purchased()
        self._update_total_sale()

    def update_purchase_cost(self, purchase_cost):
        """
        Updates the value of purchase_cost and calls update_total_purchased
        :param purchase_cost: new purchase cost of the coin
        :return: void
        """

        self.purchase_cost = purchase_cost
        self._update_total_purchased()

    def update_sale_cost(self, sale_cost):
        """
        Updates the value of sale_cost and calls update_total_sale
        :param sale_cost: new sale cost of the coin
        :return: void
        """

        self.sale_cost = sale_cost
        self._update_total_sale()

    def _update_total_purchased(self):
        """
        Calculates the total cost of the purchase and updates the total_purchased widget accordingly
        :return: void
        """

        total = self.quantity * self.purchase_cost

        # updates the total_purchase following the dollar format
        self.total_purchased.setText('${:,.2f}'.format(total))

        self._update_total_profit()
        self._update_total_variance()

    def _update_total_sale(self):
        """
        Calculates the total cost of the sale and updates the total_sale widget accordingly
        :return: void
        """

        total = self.quantity * self.sale_cost

        # updates the total_sold text following the dollar format
        self.total_sold.setText('${:,.2f}'.format(total))
        self._update_total_profit()
        self._update_total_variance()

    def _update_total_profit(self):
        """
        Calculates the total profit and updates the total_profit widget accordingly
        :return: void
        """

        total = self.quantity * (self.sale_cost - self.purchase_cost)
        self.total_profit.setText('${:,.2f}'.format(total))

    def _update_total_variance(self):
        """
        Calculates the total variance and updates the total_variance widget accordingly
        :return: void
        """

        total = self.sale_cost / self.purchase_cost - 1
        self.total_variance.setText('{:,.2f}%'.format(total))
