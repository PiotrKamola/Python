from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.val1 = None
        self.val2 = None
        self.operand = None
        self.button = None
        self.sum = None
        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle("Test")
        self.initUI()

    def initUI(self):
        self.val1 = QtWidgets.QLineEdit(self)
        self.val2 = QtWidgets.QLineEdit(self)
        self.val2.move(200, 0)

        self.sum = QtWidgets.QLabel(self)
        self.sum.setText(" ")
        self.sum.move(50, 100)

        self.operand = QtWidgets.QComboBox(self)
        self.operand.addItem("+")
        self.operand.addItem("-")
        self.operand.addItem("*")
        self.operand.addItem("/")
        self.operand.addItem("%")
        self.operand.move(100, 0)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Calculate")
        self.button.move(100, 30)
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        try:
            if self.operand.currentText() == "+":
                result = int(self.val1.text()) + int(self.val2.text())
            elif self.operand.currentText() == "-":
                result = int(self.val1.text()) - int(self.val2.text())
            elif self.operand.currentText() == "*":
                result = int(self.val1.text()) * int(self.val2.text())
            elif self.operand.currentText() == "/":
                result = int(self.val1.text()) / int(self.val2.text())
            elif self.operand.currentText() == "%":
                result = int(self.val1.text()) % int(self.val2.text())
            self.sum.setText(str(result))
            self.update()
        except:
            self.sum.setText(" ")
            self.update()

    def update(self):
        self.sum.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
