from PyQt6.QtWidgets import QGroupBox, QLabel, QFormLayout


class AnalysesGroupBox(QGroupBox):

    def __init__(self):

        super(AnalysesGroupBox, self).__init__("Purchase")

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