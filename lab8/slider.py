#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class SliderDisplay(QWidget):
    def __init__(self, name, min, max, set, tick, parent=None):
        super(SliderDisplay, self).__init__(parent)
        self.name = name
        self.min = min
        self.max = max
        self.set = set
        self.tick = tick
        self.value = set

        # widget = QWidget()
        # self.setCentralWidget(widget)

        layout = QHBoxLayout()
        self.lab = QLabel("{}: {}".format(self.name, self.set))
        self.lab.setAlignment(Qt.AlignCenter)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.min)
        self.slider.setMaximum(self.max)
        self.slider.setValue(self.set)
        # print(self.slider.value())
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(self.tick)

        self.slider.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("Slider")

        # Add things to the layout
        layout.addWidget(self.lab)
        layout.addWidget(self.slider)

    def valuechange(self):
        value = self.slider.value()
        self.value = self.slider.value()/1000
        self.lab.setText('{}: {:.3f}'.format(self.name, value / 1000))


def main(name, min, max, set, tick):
    app = QApplication(sys.argv)
    ex = SliderDisplay(name, min, max, set, tick)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # this seems to not work in the actual script..?
    main('foo', 1, 1000, 0.001, 100)
