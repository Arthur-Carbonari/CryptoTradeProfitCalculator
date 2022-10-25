"""
Name: Arthur Carbonari Martins
Student Number: 3028568

Link to remote repository: https://github.com/Arthur-Carbonari/CryptoTradeProfitCalculator

EXTRA FEATURE:

For my extra feature I made a responsive graph that displays in a line graph the value fluctuation of the cryptocurrency
The graph has an X axis representing the time, and a Y axis representing the value of the crypto coin.
The graph displays data from the selected purchase date to the selected sale date.
Whenever the user changes the selected currency, the purchase date or the sale date the graph is updated accordingly.

You can see the code for the extra feature in the GraphBox.py file.
"""

# standard imports
import sys

# PyQt imports
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QGuiApplication, QIcon
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QHBoxLayout

# Local Imports
from AnalysesBox import AnalysesBox
from CalendarBox import CalendarBox
from CurrencyBox import CurrencyBox
from GraphBox import GraphBox


class CryptoTradeProfitCalculator(QDialog):
    """
    Provides the following functionality:

    - Allows the selection of the Crypto Coin to be purchased
    - Allows the selection of the quantity to be purchased
    - Allows the selection of the purchase date
    - Displays the purchase total
    - Allows the selection of the sell date
    - Displays the sell total
    - Displays the profit total
    - Additional functionality : Graph of the coin value variance
    """

    def __init__(self):
        """
        Initializes all the widget boxes, gets the data from the csv file and calls the init_ui method to set up the
        layout
        """
        super().__init__()

        # setting up dictionary of Crypto Coins
        self.data = self.make_data()
        '''Dictionary containing the all the data on the Crypto Coins'''

        # sorting the dictionary of Crypto Coins by the keys. The keys at the high level are dates, so we sort by date
        self.stocks = sorted(self.data.keys())
        '''List of names for the available crypto currencies.'''

        # Initializing the widget boxes
        self.currency_box = CurrencyBox(self.stocks)
        '''CurrencyBox object that contains the currency combobox and the quantity spinner widgets'''

        self.calendar_box = CalendarBox()
        '''CalendarBox object that contains the purchase calendar and the sale calendar widgets'''

        self.graph_box = GraphBox()
        '''GraphBox object that contains the plot widget'''

        self.analyses_box = AnalysesBox()
        '''
        AnalysesBox object that contains the labels widget responsible for displaying the results of the calculations
        '''

        # Connecting signals to slots to that a change in one control updates the UI
        self.currency_box.quantity_update.connect(self.update_purchase_quantity)
        self.currency_box.currency_update.connect(self.update_calendars)
        self.calendar_box.purchase_date_update.connect(self.update_purchase_cost)
        self.calendar_box.sale_date_update.connect(self.update_sale_cost)
        self.calendar_box.sale_date_update.connect(self.update_graph)

        self.init_ui()

    def init_ui(self):
        """
        This method, initializes and sets up the UI layout for this Dialog
        :return: void
        """

        # Initialize the layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        self.setLayout(main_layout)

        # Add currency box selection to layout : contains currency and quantity selection
        main_layout.addWidget(self.currency_box)

        # Add calendars box to layout : contains purchase and sale calendar widgets
        main_layout.addWidget(self.calendar_box)

        # Create results layout : contains analyses and graph sections
        results_layout = QHBoxLayout()

        # Adds graph box to the layout : Displays a graph of dates(x) by value of coin(y), dates(buy_date to sale_date)
        results_layout.addWidget(self.graph_box, 4)

        # Adds analyses box to the layout : Displays the processed data of the transactions (cost, profit, variance)
        results_layout.addWidget(self.analyses_box, 2)

        # Creates results group, a wrapper QWidget for the results_layout
        results_group = QWidget()
        results_group.setLayout(results_layout)
        results_group.setMinimumHeight(300)

        # Adds result group to the main layout
        main_layout.addWidget(results_group)

        # Readjusts the Dialog size
        screen_size = QGuiApplication.primaryScreen().geometry()

        self.resize(int(screen_size.width() * 0.7), int(screen_size.height()*0.85))

        # set the window title
        self.setWindowTitle("Crypto-Currency Profit Calculator")
        self.setWindowIcon(QIcon('./assets/icon.png'))  # https://www.flaticon.com/free-icons/cryptocurrency

    def update_purchase_quantity(self):
        """
        This method is called when a signal is sent that the value of the quantity spinbox is changed, it will then get
        the new quantity from the currency_box and pass it to the analyses_box object
        :return: void
        """
        self.analyses_box.update_quantity(self.currency_box.quantity)

    def update_calendars(self):
        """
        This method is called when a signal is sent that the value for the currency drop box has changed, it will then
        get the dates for the newly selected currency on the data dictionary and pass those dates to the calendar_box
        object
        :return: void
        """
        dates = sorted(self.data[self.currency_box.currency].keys())
        self.calendar_box.update_dates(dates)

    def update_purchase_cost(self):
        """
        This method is called when a signal is sent that the date of the purchase has been updated on the purchase
        calendar, it will then get the cost for the new selected date, and pass that cost to the analyses_box
        object
        :return: void
        """
        purchase_cost = self.data[self.currency_box.currency][self.calendar_box.purchase_date]

        self.analyses_box.update_purchase_cost(purchase_cost)

    def update_sale_cost(self):
        """
        This method is called when a signal is sent that the date of the sale has been updated on the sale calendar, it
        will then get the cost for the new sale date from data and pass that cost to the analyses_box object
        :return:
        """
        sale_cost = self.data[self.currency_box.currency][self.calendar_box.sale_date]
        self.analyses_box.update_sale_cost(sale_cost)

    def update_graph(self):
        """
        This method is called when a signal is sent that the sale date was updated, (whenever the currency or the
        purchase date is updated, the sale date is updated as well, so it is only required to watch for a sale date
        update) and then get the passes all dates and currency values between purchase and sale to the graph_box object
        :return:
        """

        # gets the data for the selected currency
        currency_data = self.data[self.currency_box.currency]

        # gets start and end date
        start_date = self.calendar_box.purchase_date
        end_date = self.calendar_box.sale_date

        # get list of all dates and of the values for the current currency
        dates = list(currency_data.keys())
        values = list(currency_data.values())

        # finds the index of the start and end date
        start_index = dates.index(start_date)
        end_index = dates.index(end_date)

        # using the found indexes splits the dates and values array and then passes them to the graph_box
        plot_dates = dates[start_index:end_index + 1]
        plot_values = values[start_index:end_index + 1]

        self.graph_box.update_plot(plot_dates, plot_values)

    # ================ YOU DO NOT HAVE TO EDIT CODE BELOW THIS POINT  ==================================================

    def make_data(self):
        """
        This code is complete
         Data source is derived from https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory but use the
         provided file to avoid confusion

         Stock   -> Date      -> Close
            BTC     -> 29/04/2013 -> 144.54
                    -> 30/04/2013 -> 139
                    .....
                    -> 06/07/2021 -> 34235.19345

                    ...

        Helpful tutorials to understand this
        - https://stackoverflow.com/questions/482410/how-do-i-convert-a-string-to-a-double-in-python
        - nested dictionaries https://stackoverflow.com/questions/16333296/how-do-you-create-nested-dict-in-python
        - https://www.tutorialspoint.com/python3/python_strings.htm
        :return: a dictionary of dictionaries
        """
        data = {}
        '''empty data dictionary (will store what we read from the file here)'''
        try:
            # open a CSV file for reading https://docs.python.org/3/library/functions.html#open
            file = open(".//combined.csv", "r")
            # empty list of file rows
            file_rows = []
            # add rows to the file_rows list
            for row in file:
                file_rows.append(row.strip())  # https://www.geeksforgeeks.org/python-string-strip-2/
            print("**************************************************************************")
            print("combined.csv read successfully. Rows read from file: " + str(len(file_rows)))

            # get the column headings of the CSV file
            print("____________________________________________________")
            print("Headings of file:")
            row0 = file_rows[0]
            line = row0.split(",")
            column_headings = line
            print(column_headings)

            # get the unique list of CryptoCurrencies from the CSV file
            non_unique_cryptos = []
            file_rows_from_row1_to_end = file_rows[1:len(file_rows) - 1]
            for row in file_rows_from_row1_to_end:
                line = row.split(",")
                non_unique_cryptos.append(line[6])
            cryptos = self.unique(non_unique_cryptos)
            print("____________________________________________________")
            print("Total Currencies found: " + str(len(cryptos)))
            print(str(cryptos))

            # build the base dictionary of CryptoCurrencies
            for crypto in cryptos:
                data[crypto] = {}

            # build the dictionary of dictionaries
            for row in file_rows_from_row1_to_end:
                line = row.split(",")
                date = self.string_date_into_QDate(line[0])
                crypto = line[6]
                close_price = line[4]
                # include error handling code if close price is incorrect
                data[crypto][date] = float(close_price)
        except:
            print("Error: combined.csv file not found. ")
            print("Make sure you have imported this file into your project.")
        # return the data
        print("____________________________________________________")
        print("Amount of Currencies stored in data:", len(data))  # will be 0 if empty/error
        print("**************************************************************************")
        return data

    @staticmethod
    def string_date_into_QDate(date_string):
        """
        This method is complete
        Converts a data in a string format like that in a CSV file to QDate Objects for use with QCalendarWidget
        :param date_string: data in a string format
        :return:
        """
        date_list = date_string.split("-")
        date_QDate = QDate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return date_QDate

    @staticmethod
    def unique(non_unique_list):
        """
        This method is complete
        Converts a list of non-unique values into a list of unique values
        Developed from https://www.geeksforgeeks.org/python-get-unique-values-list/
        :param non_unique_list: a list of non-unique values
        :return: a list of unique values
        """
        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in non_unique_list:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
                # print list
        return unique_list


# This is complete
if __name__ == '__main__':
    app = QApplication(sys.argv)
    currency_converter = CryptoTradeProfitCalculator()
    currency_converter.show()
    sys.exit(app.exec())
