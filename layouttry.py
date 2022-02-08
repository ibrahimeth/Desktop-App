from PyQt5.QtWidgets import QWidget,QApplication ,QMainWindow
from PyQt5.QtGui import QColor ,QPalette
from PyQt5 import QtWidgets
import sys

from pandas import wide_to_long

class layout_creative(QMainWindow) :
    def __init__(self) :
        super(layout_creative,self).__init__()
        self.setGeometry(500,500,500,500)
        self.move(1000,1000)
        self.layout = QtWidgets.QGridLayout()
        self.initUI()
        
    def initUI(self) :
        pass
def App():
    app = QApplication(sys.argv)
    win = layout_creative()
    win.show()
    sys.exit(app.exec_())
    
App()