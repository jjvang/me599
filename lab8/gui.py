#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import *
from testslider import sliderdemo
from slider import SliderDisplay
# valueChanged did not like to be manually imported, resorted to using *

class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('A Slider')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # Create a label
        self.lab = QLabel('0')
        # self.lab.setText('0')
        self.lab.setAlignment(Qt.AlignCenter)

        self.slider2 = sliderdemo(5)
        self.slider1 = SliderDisplay('foo',1,1000,0.001,100)


        # Create a Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setValue(0.5)
        print(self.slider.value()) # 0
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(0.5)
        self.slider.valueChanged.connect(self.valuechange)

        # self.slider2 = SliderDisplay('foo',1,1000,0.001,100)
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
        # layout.addWidget(self.slider2)
        # layout.addWidget(self.slider1)
        # layout.addWidget(self.slider)
        layout.addWidget(quit_button)
        # layout.addWidget(self.slider)

        # Add other widgets to the layout here.  Possibly other layouts.

    def valuechange(self):
          value = self.slider.value()
          self.lab.setText('{}'.format(value))


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()
