#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import *


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('I am an example window')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # Create a label
        self.lab = QLabel('0')
        # self.lab.setText('0')

        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.valuechange)

        # A layout
        layout = QVBoxLayout()

        # lab.setLayout(layout)
        widget.setLayout(layout)

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # You probably want to add in other interface elements here

        # Add things to the layout
        layout.addWidget(self.lab)
        layout.addWidget(self.slider)
        layout.addWidget(quit_button)

        # Add other widgets to the layout here.  Possibly other layouts.

    def valuechange(self):
        value = self.slider.value()
        self.lab.setText('{}'.format(value))


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

    # sys.exit(app.exec_()) # gives me a weird error, do not use it
