from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import qontroller

class ExampleApp(QtWidgets.QMainWindow, qontroller.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        
        self.btnRefresh.clicked.connect(test)

def test():
    print("Hey")

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()



    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
