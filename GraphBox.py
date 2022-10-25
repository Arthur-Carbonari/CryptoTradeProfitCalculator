from PyQt6.QtCore import QDateTime, QTime
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout
from pyqtgraph import PlotWidget, DateAxisItem, ViewBox


class GraphBox(QGroupBox):

    def __init__(self):
        """
        Initializes the Plot widget, sets the bottom axis to represent time in seconds since unix epoch, and calls the
        init_ui method to set up the layout
        """

        super(GraphBox, self).__init__("Graph")

        # initializes Plot Widget and sets x-axis to represent time
        self.widget = PlotWidget()
        self.widget.setAxisItems({'bottom': DateAxisItem()})
        self.widget.setLabel('left', 'Coin Value', units='$')
        self.widget.setLabel('bottom', 'Date')
        self.widget.showGrid(x=True, y=True)

        # initializes fields
        self.plot = None
        self.dates = []
        self.values = []

        # calls init ui
        self._init_ui()

    def _init_ui(self):
        """
        This method, initializes and sets up the UI layout for this Dialog
        :return: void
        """

        graph_layout = QHBoxLayout()
        graph_layout.setContentsMargins(15, 15, 15, 15)
        graph_layout.addWidget(self.widget)

        self.setLayout(graph_layout)

    def update_plot(self, dates, values):
        """
        This method updates the plot displayed in the PlotWidget with the new one create using the passed parameters
        :param dates: dates to be displayed in the x-axis
        :param values: corresponding values to be displayed in the y-axis
        :return:
        """

        # Converting dates[] QDate values to seconds since unix epoch
        dates = [QDateTime(date, QTime(0, 0, 0)).toSecsSinceEpoch() for date in dates]

        # removes existing plot item if any
        if self.plot:
            self.widget.removeItem(self.plot)

        # Re-enables auto range if user has disabled it by interacting with the graph
        self.widget.enableAutoRange(ViewBox.XYAxes)

        # Draws new plot using the new values
        self.plot = self.widget.plot(dates, values)
