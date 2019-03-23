#!/usr/bin/env python3


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from slider import SliderDisplay

from random import random


class Grapher(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Grapher')

        # Control buttons for the interface
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        graph_button = QPushButton('Simulate \n System')
        graph_button.clicked.connect(self.graph)

        # The display for the graph
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

        # Create a label
        self.lab = QLabel('System Parameter')
        self.lab2 = QLabel('Simulation Parameters')
        # self.lab.setText('0')
        self.lab.setAlignment(Qt.AlignLeft)
        self.lab2.setAlignment(Qt.AlignLeft)

        # app = QApplication([])
        # SliderDisplay = SliderDisplay('foo',1,1000,0.001,100)
        # SliderDisplay.show()
        # app.exec_()
        self.slider1 = SliderDisplay('Mass', 0, 10000, 0.000, 1000)
        self.slider2 = SliderDisplay('Spring', 0, 10000, 0.000, 1000)
        self.slider3 = SliderDisplay('Damper', 0, 10000, 0.000, 1000)
        self.slider4 = SliderDisplay('Time (s)', 0, 100000, 0.0000, 10000)
        self.slider5 = SliderDisplay('Time step (s)', 1, 100000, 0.0001, 10000)

        # The layout of the interface
        widget = QWidget()
        self.setCentralWidget(widget)

        top_level_layout = QHBoxLayout()
        widget.setLayout(top_level_layout)
        left_side_layout = QVBoxLayout()

        # Add things to the layout
        left_side_layout.addWidget(self.lab)
        left_side_layout.addWidget(self.slider1)
        left_side_layout.addWidget(self.slider2)
        left_side_layout.addWidget(self.slider3)

        left_side_layout.addWidget(self.lab2)
        left_side_layout.addWidget(self.slider4)
        left_side_layout.addWidget(self.slider5)
        left_side_layout.addWidget(graph_button)
        # left_side_layout.addStretch()
        left_side_layout.addWidget(quit_button)

        top_level_layout.addLayout(left_side_layout)
        top_level_layout.addWidget(self.display)

    def graph(self):
        self.draw([random() for i in range(25)])

    def draw(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.plot(data)
        # ax.set_title('EHH')
        ax.set_title(
            'Graph \n k={:.3f}, m={:.3f}, c={:.3f}, dt={:.3f}'.format(self.slider2.value, self.slider1.value,
                                                                      self.slider3.value, self.slider5.value))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        self.display.draw()


if __name__ == '__main__':
    app = QApplication([])

    gui = Grapher()

    gui.show()

    app.exec_()
