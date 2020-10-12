# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title 
        self.setWindowTitle("Python ")

        # setting geometry 
        self.setGeometry(100, 100, 600, 400)

        # calling method 
        self.UiComponents()

        # showing all the widgets 
        self.show()

        # method for widgets

    def UiComponents(self):
        # creating a combo box widget
        self.combo_box = QComboBox(self)

        # setting geometry of combo box 
        self.combo_box.setGeometry(200, 150, 120, 30)

        # geek list 
        geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]

        # adding list of items to combo box 
        self.combo_box.addItems(geek_list)

        # creating push button 
        button = QPushButton("Change content ", self)

        print(self.combo_box.count())

        # adding action to button 
        button.pressed.connect(self.find)

        # creating label 
        self.label = QLabel(self)

        # setting geometry of the label 
        self.label.setGeometry(200, 200, 200, 30)

        # old content at index 2 
        content = self.combo_box.itemText(2)

        # showing the old content 
        self.label.setText("old content  : content")

    def find(self):
        # index
        index = 2

        # changing the content 
        self.combo_box.setItemText(index, "New data")

    # create pyqt5 app


App = QApplication(sys.argv)

# create the instance of our Window 
window = Window()

# start the app 
sys.exit(App.exec()) 