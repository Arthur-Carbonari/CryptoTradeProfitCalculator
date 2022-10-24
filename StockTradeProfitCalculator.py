"""
Name: Arthur Carbonari Martins
Student Number: 3028568
"""

# TODO: Remember to fully comment your code
# TODO: Include a comment 'EXTRA FEATURE' and explain what your Extra Feature does
# TODO: Don't forget to document your design choices in your UI Design Document

# standard imports
import sys

# PyQt imports
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QGuiApplication
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
        This method gets and parses the data from the cvs file, initializes all the widget boxes and calls the init_ui
        method to set up the layout
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

        self.groupbox_calendar = CalendarBox()
        '''CalendarBox object that contains the purchase calendar and the sale calendar widgets'''

        self.graph_box = GraphBox()
        '''GraphBox object that contains the plot widget'''

        self.groupbox_analyses = AnalysesBox()
        '''
        AnalysesBox object that contains the labels widget responsible for displaying the results of the calculations
        '''

        # Connecting signals to slots to that a change in one control updates the UI
        self.currency_box.quantity_update.connect(self.update_purchase_quantity)
        self.currency_box.currency_update.connect(self.update_calendars)
        self.groupbox_calendar.purchase_date_update.connect(self.update_purchase_cost)
        self.groupbox_calendar.sale_date_update.connect(self.update_sale_cost)
        self.groupbox_calendar.sale_date_update.connect(self.update_graph)

        self.init_ui()

    def init_ui(self):
        """
        This method, initializes and sets up the UI for this Widget
        :return: void
        """

        # Initialize the layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        self.setLayout(main_layout)

        # Add currency box selection to layout : contains currency and quantity selection
        main_layout.addWidget(self.currency_box)

        # Add calendars box to layout : contains purchase and sale calendar widgets
        main_layout.addWidget(self.groupbox_calendar)

        # Create results layout : contains analyses and graph sections
        results_layout = QHBoxLayout()

        # Adds graph box to the layout : Displays a graph of dates(x) by value of coin(y), dates(buy_date to sale_date)
        results_layout.addWidget(self.graph_box, 4)

        # Adds analyses box to the layout : Displays the processed data of the transactions (cost, profit, variance)
        results_layout.addWidget(self.groupbox_analyses, 2)

        # Creates results group, a wrapper QWidget for the results_layout
        results_group = QWidget()
        results_group.setLayout(results_layout)
        results_group.setMinimumHeight(300)

        # Adds result group to the main layout
        main_layout.addWidget(results_group)

        # Increases the dialog width if needed
        screen_size = QGuiApplication.primaryScreen().geometry()

        if self.width() < screen_size.width() * 0.8:
            self.resize(int(screen_size.width() * 0.8), self.height())

            # set the window title
            self.setWindowTitle("Crypto-Currency Profit Calculator")

        # TODO: update the UI

    def update_ui(self):
        """
        This requires substantial development
        Updates the Ui when control values are changed, should also be called when the app initializes
        :return:
        """
        try:
            print(self)
            # TODO: get selected dates from calendars

            # TODO: perform necessary calculations to calculate totals

            # TODO: update the label displaying totals
        except Exception as e:
            print(e)

    def update_purchase_quantity(self):
        """
        This method is called when a signal is sent that the value of the quantity spinbox is changed, it will then get
        the new quantity from the currency_box and pass it to the analyses_box object
        :return: void
        """
        self.groupbox_analyses.update_quantity(self.currency_box.quantity)

    def update_calendars(self):
        """
        This method is called when a signal is sent that the value for the currency drop box has changed, it will then
        get the dates for the newly selected currency on the data dictionary and pass those dates to the calendar_box
        object
        :return: void
        """
        dates = sorted(self.data[self.currency_box.currency].keys())
        self.groupbox_calendar.update_dates(dates)

    def update_purchase_cost(self):
        """
        This method is called when a signal is sent that the date of the purchase has been updated on the purchase
        calendar, it will then get the cost for the new selected date, and pass that cost to the analyses_box
        object
        :return: void
        """
        purchase_cost = self.data[self.currency_box.currency][self.groupbox_calendar.purchase_date]

        self.groupbox_analyses.update_purchase_cost(purchase_cost)

    def update_sale_cost(self):
        """
        This method is called when a signal is sent that the date of the sale has been updated on the sale calendar, it
        will then get the cost for the new sale date from data and pass that cost to the analyses_box object
        :return:
        """
        sale_cost = self.data[self.currency_box.currency][self.groupbox_calendar.sale_date]
        self.groupbox_analyses.update_sale_cost(sale_cost)

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
        start_date = self.groupbox_calendar.purchase_date
        end_date = self.groupbox_calendar.sale_date

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
