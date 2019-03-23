#!/usr/bin/env python3

import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# valueChanged did not like to be manually imported, resorted to using *
from slider import SliderDisplay
from random_graph import Grapher


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('A Slider')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

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
        self.slider1 = SliderDisplay('Mass', 1, 10000, 0.001, 1000)
        self.slider2 = SliderDisplay('Spring', 1, 10000, 0.001, 1000)
        self.slider3 = SliderDisplay('Damper', 1, 10000, 0.001, 1000)
        self.slider4 = SliderDisplay('Time (s)', 0, 100000, 0.0000, 10000)
        self.slider5 = SliderDisplay('Time step (s)', 1, 100000, 0.0001, 10000)

        # A layout
        layout = QVBoxLayout()

        # lab.setLayout(layout)
        widget.setLayout(layout)

        # Simulate button
        simulate_button = QPushButton('Simulate \n System')
        # magic_button = Grapher()
        # simulate_button.clicked.connect()

        # Quit button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # You probably want to add in other interface elements here

        # Add things to the layout
        layout.addWidget(self.lab)
        layout.addWidget(self.slider1)
        layout.addWidget(self.slider2)
        layout.addWidget(self.slider3)

        layout.addWidget(self.lab2)
        layout.addWidget(self.slider4)
        layout.addWidget(self.slider5)

        # layout.addWidget(magic_button)
        layout.addWidget(simulate_button)
        layout.addWidget(quit_button)
        # layout.addWidget(self.slider)

        # Add other widgets to the layout here.  Possibly other layouts.


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()
