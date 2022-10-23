'''
UPDATED VERSION - 2022
JLEBRON / B. FOGARTY
Please make sure you use the PEP guide for naming conventions in your submission
- detailed guide: https://www.python.org/dev/peps/pep-0008/
- some examples: https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names

This assignment is heavily based on
A Currency Converter GUI Program - Python PyQt5 Desktop Application Development Tutorial
- GitHub: https://github.com/DarBeck/PyQT5_Tutorial/blob/master/currency_converter.py
- YouTube: https://www.youtube.com/watch?v=weKpTw1SjM4 - detailed explanaton
- Keep in mind this example uses PyQt5 not PyQt6

- Layout
    - I would suggest QGridLayout
    - Use a QCalendarWidget which you will get from Zetcode tutorial called "Widgets" https://zetcode.com/pyqt6/widgets/

PyCharm Configuration Options
- Viewing Documentation when working with PyCharm https://www.jetbrains.com/help/pycharm/viewing-external-documentation.html
- Configuring Python external Documenation on PyCharm https://www.jetbrains.com/help/pycharm/settings-tools-python-external-documentation.html
'''

# TODO: Delete the above, and include in a comment your name and student number
# TODO: Remember to fully comment your code
# TODO: Include a comment 'EXTRA FEATURE' and explain what your Extra Feature does
# TODO: Don't forget to document your design choices in your UI Design Document


# standard imports
import sys
from PyQt6.QtCore import QDate, QDateTime, QTime
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QLabel, QComboBox, QCalendarWidget, QDialog, QApplication, QGridLayout, QGroupBox, \
    QFormLayout, QWidget, QVBoxLayout, QHBoxLayout
from decimal import Decimal
import pyqtgraph as pg
from pyqtgraph import DateAxisItem, PlotWidget, PlotItem

from AnalysesGroupBox import AnalysesGroupBox
from CalendarGroupBox import CalendarGroupBox
from CurrencyBox import CurrencyBox
from GraphBox import GraphBox


class CryptoTradeProfitCalculator(QDialog):
    '''
    Provides the following functionality:

    - Allows the selection of the Crypto Coin to be purchased
    - Allows the selection of the quantity to be purchased
    - Allows the selection of the purchase date
    - Displays the purchase total
    - Allows the selection of the sell date
    - Displays the sell total
    - Displays the profit total
    - Additional functionality

    '''

    def __init__(self):
        '''
        This method requires substantial updates
        Each of the widgets should be suitably initalized and laid out
        '''
        super().__init__()

        # setting up dictionary of Crypto Coins
        self.data = self.make_data()

        # sorting the dictionary of Crypto Coins by the keys. The keys at the high level are dates, so we are sorting by date
        self.stocks = sorted(self.data.keys())
        '''Array of names for the available crypto currencies.'''

        # -------- EXAMPLE --------

        # the following lines of code are for debugging purposes and show you how to access the self.data to get dates and prices
        # TODO: uncomment to print all the dates and close prices for BTC
        #print("all the dates and close prices for BTC", self.data['BTC'])
        # print the close price for BTC on 04/29/2013
        print("the close price for BTC on 04/29/2013", self.data['BTC'][QDate(2013, 4, 29)])

        # The data in the file is in the following range
        #     first date in dataset - 29th Apr 2013
        #     last date in dataset - 6th Jul 2021
        # When the calendars load we want to ensure that the default dates selected are within the date range above
        #     we can do this by setting variables to store suitable default values for sellCalendar and buyCalendar.
        self.sellCalendarDefaultDate = sorted(self.data['BTC'].keys())[-1]
        # Accessing the last element of a python list is explained with method 2 on https://www.geeksforgeeks.org/python-how-to-get-the-last-element-of-list/
        print("self.sellCalendarStartDate", self.sellCalendarDefaultDate)
        # self.buyCalendarDefaultDate = ???
        # print("self.buyCalendarStartDate", self.buyCalendarDefaultDate)

        # -------- END OF EXAMPLE --------

        self.init_ui()

    def init_ui(self):

        self.currency_box = CurrencyBox(self.stocks)

        self.groupbox_calendar = CalendarGroupBox()

        self.graph_box = GraphBox()

        # Create AnalysesGroupBox
        self.groupbox_analyses = AnalysesGroupBox()

        # TODO: initialize the layout - 6 rows to start
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        main_groupbox = QGroupBox()
        main_groupbox.setLayout(main_layout)
        wrapper_layout = QHBoxLayout()
        wrapper_layout.addWidget(main_groupbox)
        self.setLayout(wrapper_layout)

        # Add CryptoCurrency selection to layout
        main_layout.addWidget(self.currency_box)

        # Add group boxes to layout
        main_layout.addWidget(self.groupbox_calendar)

        h_layout = QGridLayout()
        h_layout.addWidget(self.graph_box, 0, 0)
        h_layout.addWidget(self.groupbox_analyses, 0, 1)
        h_layout.setColumnStretch(0, 4)
        h_layout.setColumnStretch(1, 2)
        h_layout.setRowMinimumHeight(0, 300)
        bottom_group = QWidget()
        bottom_group.setLayout(h_layout)

        widt = int(QGuiApplication.primaryScreen().geometry().width() * 0.8)
        self.resize(widt, self.height())

        main_layout.addWidget(bottom_group)

        # TODO: connecting signals to slots to that a change in one control updates the UI
        self.currency_box.currency_update.connect(self.update_calendars)
        self.groupbox_calendar.purchase_quantity_update.connect(self.update_purchase_quantity)
        self.groupbox_calendar.purchase_date_update.connect(self.update_purchase_cost)
        self.groupbox_calendar.sale_date_update.connect(self.update_sale_cost)
        self.groupbox_calendar.sale_date_update.connect(self.update_graph)

        # TODO: set the window title

        # TODO: update the UI

    def updateUi(self):
        '''
        This requires substantial development
        Updates the Ui when control values are changed, should also be called when the app initializes
        :return:
        '''
        try:
            print("Update UI")
            # TODO: get selected dates from calendars

            # TODO: perform necessary calculations to calculate totals

            # TODO: update the label displaying totals
        except Exception as e:
            print(e)

    def update_purchase_quantity(self):
        self.groupbox_analyses.update_quantity(self.groupbox_calendar.purchase_quantity)

    def update_calendars(self):
        dates = sorted(self.data[self.currency_box.selected_currency].keys())
        self.groupbox_calendar.update_dates(dates)

    def update_purchase_cost(self):
        purchase_cost = self.data[self.currency_box.selected_currency][self.groupbox_calendar.purchase_date]

        self.groupbox_analyses.update_purchase_cost(purchase_cost)

    def update_sale_cost(self):
        sale_cost = self.data[self.currency_box.selected_currency][self.groupbox_calendar.sale_date]
        self.groupbox_analyses.update_sale_cost(sale_cost)

    def update_graph(self):
        currency_data = self.data[self.currency_box.selected_currency]

        start_date = self.groupbox_calendar.purchase_date
        end_date = self.groupbox_calendar.sale_date

        dates = list(currency_data.keys())
        values = list(currency_data.values())

        start_index = dates.index(start_date)
        end_index = dates.index(end_date)

        plot_dates = dates[start_index:end_index+1]
        plot_values = values[start_index:end_index+1]

        self.graph_box.update_plot(plot_dates, plot_values)

    ################ YOU DO NOT HAVE TO EDIT CODE BELOW THIS POINT  ########################################################

    def make_data(self):
        '''
        This code is complete
         Data source is derived from https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory but use the provided file to avoid confusion

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
        '''
        data = {}  # empty data dictionary (will store what we read from the file here)
        try:
            file = open(".//combined.csv", "r")  # open a CSV file for reading https://docs.python.org/3/library/functions.html#open
            file_rows = []  # empty list of file rows
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
        #return the data
        print("____________________________________________________")
        print("Amount of Currencies stored in data:", len(data)) #will be 0 if empty/error
        print("**************************************************************************")
        return data

    def string_date_into_QDate(self, date_String):
        '''
        This method is complete
        Converts a data in a string format like that in a CSV file to QDate Objects for use with QCalendarWidget
        :param date_String: data in a string format
        :return:
        '''
        date_list = date_String.split("-")
        date_QDate = QDate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return date_QDate

    def unique(self, non_unique_list):
        '''
        This method is complete
        Converts a list of non-unique values into a list of unique values
        Developed from https://www.geeksforgeeks.org/python-get-unique-values-list/
        :param non_unique_list: a list of non-unique values
        :return: a list of unique values
        '''
        # intilize a null list
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
