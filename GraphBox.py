from PyQt6.QtCore import QDateTime, QDate, QTime
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout
from pyqtgraph import PlotWidget, DateAxisItem, ViewBox


class GraphBox(QGroupBox):

    def __init__(self):

        super(GraphBox, self).__init__("Graph")

        self.widget = PlotWidget()
        self.widget.setAxisItems({'bottom': DateAxisItem()})

        self.plot = None
        self.dates = []
        self.values = []

        self.init_ui()

    def init_ui(self):
        graph_layout = QHBoxLayout()
        graph_layout.setContentsMargins(15, 15, 15, 15)
        graph_layout.addWidget(self.widget)

        self.setLayout(graph_layout)

    def update_plot(self, dates, values):

        # Converting dates[] QDate values to seconds since unix epoch
        dates = [QDateTime(date, QTime(0, 0, 0)).toSecsSinceEpoch() for date in dates]

        if self.plot:
            self.widget.removeItem(self.plot)

        self.widget.enableAutoRange(ViewBox.XYAxes)
        self.plot = self.widget.plot(dates, values)
