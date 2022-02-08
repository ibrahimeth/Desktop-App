#from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtCore import pyqtSignal, QThread
class first_GUI(QWidget):
    def __init__(self):
        #super(first_GUI, self).__init__()
        #super().__init__()
        QWidget.__init__(self)

        self.label_text = QLabel("Merhaba PyQt5")
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setStyleSheet("color: rgb(0,0,255);font-weight: bold; font-size: 16pt")

        pushButton_clear = QPushButton("Temizle")
        pushButton_clear.setMinimumHeight(40)
        pushButton_clear.setStyleSheet("font-weight: bold; font-size: 16pt")
        pushButton_show = QPushButton("Göster")
        pushButton_show.setMinimumHeight(40)
        pushButton_show.setStyleSheet("font-weight: bold; font-size: 16pt")
        
        pushButton_clear.clicked.connect(self.clear_text)
        pushButton_show.clicked.connect(self.show_text)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_text)
        vertical_layout.addWidget(pushButton_clear)
        vertical_layout.addWidget(pushButton_show)

        self.setLayout(vertical_layout)
        self.setWindowTitle("HUMA AR-GE TF DT 22")
        self.resize(400,300)

    def button_pushed():
        pass


    def clear_text(self):
        self.label_text.clear()

    def show_text(self):
        self.label_text.setText("Merhaba PyQt5")
        
app = QApplication([])
widget = first_GUI()
widget.show()
app.exec_()