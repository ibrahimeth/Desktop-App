import imp
from re import T
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from selenium.webdriver.common.keys import Keys
from PyQt5.QtCore import QPropertyAnimation
from soupsieve import select


class HesapMachine(QMainWindow) :
    def __init__(self) :
        super(HesapMachine,self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(400,400,300,450)
        self.move(1200,150)
        self.setToolTip("ibr_ethem1")
        self.setMinimumSize(310,490)
        self.setMaximumSize(310,490)
        self.firstnum = None
        self.secondnum = False
        self.initUI()

    def initUI(self):

        # Gerekli Butonlar yerleştirildi

        self.TextBx = QtWidgets.QLineEdit(self)
        self.TextBx.move(0,0)
        self.TextBx.resize(310,100)
        self.TextBx.setFont(QFont("Arial",25))

        self._cbtn = QtWidgets.QPushButton(self)
        self._cbtn.move(20,130)
        self._cbtn.resize(60,60)
        self._cbtn.setText("C")
        self._cbtn.clicked.connect(self.clear)

        self._yuzdebtn = QtWidgets.QPushButton(self)
        self._yuzdebtn.move(160,130)
        self._yuzdebtn.resize(60,60)
        self._yuzdebtn.setText("%")
        self._yuzdebtn.clicked.connect(self.yuzde)

        self.karekokbtn = QtWidgets.QPushButton(self)
        self.karekokbtn.move(90,130)
        self.karekokbtn.resize(60,60)
        self.karekokbtn.setText(" √ ")
        self.karekokbtn.clicked.connect(self.karekok)

        self._1btn = QtWidgets.QPushButton(self)
        self._1btn.move(20,200)
        self._1btn.resize(60,60)
        self._1btn.setText("1")
        self._1btn.clicked.connect(self.Basildi)

        self._2btn = QtWidgets.QPushButton(self)
        self._2btn.move(90,200)
        self._2btn.resize(60,60)
        self._2btn.setText("2")
        self._2btn.clicked.connect(self.Basildi)

        self._3btn = QtWidgets.QPushButton(self)
        self._3btn.move(160,200)
        self._3btn.resize(60,60)
        self._3btn.setText("3")
        self._3btn.clicked.connect(self.Basildi)

        self._4btn = QtWidgets.QPushButton(self)
        self._4btn.move(20,270)
        self._4btn.resize(60,60)
        self._4btn.setText("4")
        self._4btn.clicked.connect(self.Basildi)

        self._5btn = QtWidgets.QPushButton(self)
        self._5btn.move(90,270)
        self._5btn.resize(60,60)
        self._5btn.setText("5")
        self._5btn.clicked.connect(self.Basildi)

        self._6btn = QtWidgets.QPushButton(self)
        self._6btn.move(160,270)
        self._6btn.resize(60,60)
        self._6btn.setText("6")
        self._6btn.clicked.connect(self.Basildi)

        self._7btn = QtWidgets.QPushButton(self)
        self._7btn.move(20,340)
        self._7btn.resize(60,60)
        self._7btn.setText("7")
        self._7btn.clicked.connect(self.Basildi)

        self._8btn = QtWidgets.QPushButton(self)
        self._8btn.move(90,340)
        self._8btn.resize(60,60)
        self._8btn.setText("8")
        self._8btn.clicked.connect(self.Basildi)

        self._9btn = QtWidgets.QPushButton(self)
        self._9btn.move(160,340)
        self._9btn.resize(60,60)
        self._9btn.setText("9")
        self._9btn.clicked.connect(self.Basildi)

        self._virgbtn = QtWidgets.QPushButton(self)
        self._virgbtn.move(20,410)
        self._virgbtn.resize(60,60)
        self._virgbtn.setText(".")
        self._virgbtn.clicked.connect(self.ondalik)

        self._0btn = QtWidgets.QPushButton(self)
        self._0btn.move(90,410)
        self._0btn.resize(60,60)
        self._0btn.setText("0")
        self._0btn.clicked.connect(self.Basildi)

        self.toplabtn = QtWidgets.QPushButton(self)
        self.toplabtn.resize(60,60)
        self.toplabtn.move(230,130)
        self.toplabtn.setText("+")
        self.toplabtn.clicked.connect(self.aritmatik)
        self.toplabtn.setCheckable(True)

        self.cikarmabtn = QtWidgets.QPushButton(self)
        self.cikarmabtn.resize(60,60)
        self.cikarmabtn.move(230,200)
        self.cikarmabtn.setText("-")
        self.cikarmabtn.clicked.connect(self.aritmatik)
        self.cikarmabtn.setCheckable(True)

        self.carpmabtn = QtWidgets.QPushButton(self)
        self.carpmabtn.resize(60,60)
        self.carpmabtn.move(230,270)
        self.carpmabtn.setText("*")
        self.carpmabtn.clicked.connect(self.aritmatik)
        self.carpmabtn.setCheckable(True)

        self.bolmebtn = QtWidgets.QPushButton(self)
        self.bolmebtn.resize(60,60)
        self.bolmebtn.move(230,340)
        self.bolmebtn.setText("/")
        self.bolmebtn.clicked.connect(self.aritmatik)
        self.bolmebtn.setCheckable(True)

        self._Sendbtn = QtWidgets.QPushButton(self)
        self._Sendbtn.move(160,410)
        self._Sendbtn.resize(130,60)
        self._Sendbtn.setText("GEÇ")

    # # eşittir butona basıldığında
        self._Sendbtn.clicked.connect(self.sonuc)
        self._Sendbtn.setCheckable(True)

    def Basildi(Self) :
        Buton = Self.sender()
        if ((Self.secondnum) and (Self._Sendbtn.isChecked())) :
            # Self.TextBx.setText(format(Buton.text()),".15g")
            Self.secondnum = True
            Self._Sendbtn.setChecked(False)
        elif (Self.toplabtn.isChecked() or Self.cikarmabtn.isChecked() or Self.carpmabtn.isChecked() or Self.bolmebtn.isChecked()) and (not Self.secondnum):
            Self.TextBx.setText(format(float(Self.TextBx.text() + Buton.text()),'.15g'))
            Self.secondnum = True
        else :
            if (('.' in Self.TextBx.text()) and Buton.text() == "0"):
                Self.TextBx.setText(format(Self.TextBx.text()),".15")
            else :
                Self.TextBx.setText(format(float(Self.TextBx.text() + Buton.text()),'.15g'))


#    sil  fonksiyonu ekleyelim 

    def clear(self) :
        self.firstnum = 0 
        self.secondnum = False
        self.TextBx.setText("0")
        self.toplabtn.setChecked(False)
        self.cikarmabtn.setChecked(False)
        self.carpmabtn.setChecked(False)
        self.bolmebtn.setChecked(False)


    def ondalik(self) :
        self.TextBx.setText(self.TextBx.text() + ".")

    def karekok(self) :
        pass

    def yuzde(self) :
        pass

    def aritmatik(self) :
        buton = self.sender()
        self.firstnum = float(self.TextBx.text())
        print(self.firstnum)
        self.TextBx.setText("0")
        buton.setChecked(True)

    def sonuc(self) :
        second_value = float(self.TextBx.text())
        if self.toplabtn.isChecked() :
            new_value = self.firstnum + second_value
            self.TextBx.setText(format(float(new_value),".15g"))
            self.toplabtn.setChecked(False)
        elif self.cikarmabtn.isChecked() :
            new_value = self.firstnum  - second_value
            self.TextBx.setText(format(float(new_value),".15g"))
            self.cikarmabtn.setChecked(False)            
        elif self.carpmabtn.isChecked() :
            new_value = self.firstnum * second_value
            self.TextBx.setText(format(float(new_value),".15g"))
            self.carpmabtn.setChecked(False)
        elif self.bolmebtn.isChecked() :
            new_value = self.firstnum / second_value
            self.TextBx.setText(format(float(new_value),".15g"))
            self.bolmebtn.setChecked(False)

        self.firstnum = new_value

    def Random(self) :
        pass

def mainLOOP():
    app = QApplication(sys.argv)
    win = HesapMachine()
    win.show()
    sys.exit(app.exec_())

mainLOOP()