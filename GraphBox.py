from PyQt6.QtWidgets import QGroupBox, QHBoxLayout
from pyqtgraph import PlotWidget, DateAxisItem


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
