from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
from main import backend


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        # self.setStyleSheet("background-color: 'white';")
        # self.setStyleSheet = window {background-image()}
        self.resize(550, 700)
        self.setWindowTitle("Sentiment Analysis")
        self.label1 = QLabel("Sentiment Analysis", self)
        self.label1.setGeometry(200, 100, 500, 80)
        self.label1.move(100, 20)
        self.label1.setFont(QFont('Sans Serif', 25))
        self.label2 = QLabel("Enter Youtube video link:", self)
        self.label2.setGeometry(200, 100, 500, 80)
        self.label2.move(10, 200)
        self.label2.setFont(QFont('Sans Serif', 15))
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 270)
        self.textbox.resize(400, 75)
        self.textbox.setFont(QFont('Sans Serif', 20))
        self.textbox.setStyleSheet("border: 4px solid black;")
        self.button = QPushButton(self)
        self.button.move(10, 360)
        self.button.resize(100, 50)
        self.button.setText("Submit")
        self.button.setFont(QFont('Sans Serif', 15))
        self.button.setStyleSheet("color: black;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        link = self.textbox.text()
        backend(link)


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
