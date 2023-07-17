
import sys
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x
import math
import sympy as sym

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
plt.ion()

matplotlib.use('Qt5Agg')

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPixmap
import re

class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QWidget { color: blue; font-weight: bold; }")
        self.setWindowTitle("Function Plotter")

        self.createIcon()
        self.resize(550, 820)

        # Set the background color using a style sheet
        self.setStyleSheet("background-color:   #1D355D;")



        self.layout = QVBoxLayout()

        # Function label and textbox
        self.label = self.create_Label("Function:", 10, 50)
        self.textbox = self.create_Textbox("Enter function of x e.g. 5*x^3 + 2*x..", 20, 85)

        # Minimum label and textbox
        self.label1 = self.create_Label("Minimum:", 10, 140)
        self.textbox1 = self.create_Textbox("Enter minimum value of x..", 20, 175)

        # Maximum label and textbox
        self.label2 = self.create_Label("Maximum:", 10, 230)
        self.textbox2 = self.create_Textbox("Enter maximum value of x..", 20, 265)

        # Plot button
        self.button1 = self.create_button("Plot", 600, 40, 80, 380)
        self.button1.clicked.connect(self.plot)

        # Error label
        self.error_label = self.create_Label("", 10, 400)
        self.error_label.setStyleSheet("color: red")

        # Create a FigureCanvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.canvas)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def createIcon(self):
        appIcon = QIcon(r"1200px-Icon_Mathematical_Plot.svg.png")
        self.setWindowIcon(appIcon)

    def create_button(self, text, setFixedWidth, setFixedHeight, movex, movey):
        # Add button
        btn = QPushButton(text, self)
        self.layout.addWidget(btn)
        btn.setIcon(QIcon(r"download (3).png"))
        #btn.setFixedSize(setFixedWidth, setFixedHeight)
        btn.setStyleSheet("background-color: lightgray;")
        btn.setIconSize(QSize(40, 40))
        btn.move(movex, movey)
        btn.resize(500, 20)
        return btn

    def create_Label(self, text, movex, movey):
        # Add label
        label = QLabel(text, self)
        self.layout.addWidget(label)
        label.move(movex, movey)
        font = QFont("Arial", 12)
        font.setBold(True)
        label.setFont(font)
        label.setStyleSheet("color: Black;")
        return label

    def create_Textbox(self, text, movex, movey):
        # Add textbox
        textbox = QLineEdit(self)
        self.layout.addWidget(textbox)
        textbox.move(movex, movey)
        textbox.setStyleSheet("background-color: lightgray;")
        textbox.resize(500, 40)
        textbox.setPlaceholderText(text)
        return textbox

    def plot(self):
        self.figure.clear()
        function_str = self.textbox.text()
        min_str = self.textbox1.text()
        max_str = self.textbox2.text()

        # Check for valid input
        if not function_str:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot()
            self.canvas.draw()
            self.error_label.setText("Please Enter valid Function.")
            return

        if not min_str or not max_str:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot()
            self.canvas.draw()
            self.error_label.setText("Please Enter Minimum and Maximum values of x.")
            return

        try:
            try:
                min_val = float(min_str)
            except RuntimeWarning:
                # Handle the warning here
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                ax.plot()
                self.canvas.draw()
                self.error_label.setText("Please Enter valid numbers for Minimum values of x.")
            try:
                max_val = float(max_str)
            except RuntimeWarning:
                # Handle the warning here
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                ax.plot()
                self.canvas.draw()
                self.error_label.setText("Please Enter valid numbers for Maximum values of x.")

        except ValueError:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot()
            self.canvas.draw()
            self.error_label.setText("Please Enter valid numbers for Minimum and Maximum values of x.")
            return
        if(float(min_str) > float(max_str)):
            self.figure.clear()
            self.error_label.setText("Please Enter valid numbers for Minimum and Maximum values of x.")
            return
        # Evaluate the function
        try:
            x_val = np.linspace(min_val, max_val, 1000)
            eq = function_str.replace('e', str(math.e))
            xa = sym.expand(eq)
            list_y = []
            self.error_label.setText("")
            for i in x_val:
                values = {x: i}
                res = xa.subs(values)
                list_y.append(res)

            # Clear the figure and plot the function
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x_val, list_y)
            self.canvas.draw()
        except :
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot()
            self.canvas.draw()
            self.error_label.setText("Please Enter valid Function.")

            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FunctionPlotter()
    ex.show()
    sys.exit(app.exec_())

