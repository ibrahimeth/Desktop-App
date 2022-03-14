import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ledyak2 import Ui_MainWindow
import sys

class SerialThreadlasss(QThread) :

    msg = pyqtSignal(str)

    def __init__(self):
        super(SerialThreadlasss,self).__init__()
        self.seriport = serial.Serial()
        self.stopflag = False

class Tasarla(QMainWindow) :
    def __init__(self) :
        super(Tasarla,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self) :
        self.ui.MessageKutusu.setReadOnly(True)
        self.ports = serial.tools.list_ports.comports()
        for i in self.ports :
            self.ui.ComSelect.addItem(str(i))
        baud = ["300", "1200", "2400", "4800", "9600", "19200", "38400", "57600", "74880", "115200", "230400", "250000",
                "500000", "1000000", "2000000"]
        for i in baud :
            self.ui.SerialBeginSelect.addItem(str(i))
        self.ui.SerialBeginSelect.setCurrentText(baud[4])

        self.mySerial = SerialThreadlasss()
        self.mySerial.msg.connect(self.messageTextEdit)
        self.mySerial.start()

        self.ui.Baglan.clicked.connect(self.serialConnect)          # Butona tıklandığında serialConnection isimli fonksiyona dallan.
        self.ui.baglantiyikes.clicked.connect(self.serialDisconnect)
        self.ui.Led1Yak.clicked.connect(self.Yakma)               
        self.ui.Led1Sondur.clicked.connect(self.sondur)

        self.show()
        
    def messageTextEdit(self) :              # Seri Porttan mesaj geldiğinde bu Fonksiyona dallanacak
        self.incomingMessage = str(self.mySerial.data.decode())
        self.ui.MessageKutusu.append(self.incomingMessage)

    def serialConnect(self) :
        self.portText = self.ui.ComSelect.currentText()                     # o anda hangi port okunmuşa Ççektik .
        self.port = self.portText.split()                                   # sadece COM kısmını çektik
        self.baudrate = self.ui.SerialBeginSelect.currentText() 
        self.mySerial.seriport.baudrate = int(self.baudrate)
        self.mySerial.seriport.port = self.port[0]
        try:
            self.mySerial.seriport.open() # seri porta bağlanma komutu verildi.
        except:
            self.ui.MessageKutusu.append("Bağlantı Hatası!!")

        if(self.mySerial.seriport.isOpen()):
            self.ui.ComState.setText('<font color=green>Bağlandı</font>')           # bağlantı sağlandıysa label1 yeşile dönsün.
            self.ui.Baglan.setEnabled(False)                                        # Bağlantı varken tekrar bağlan butonuna tıklanmasın diye butonu pasif ediyoruz.
            self.ui.ComSelect.setEnabled(False)
            self.ui.ComSelect.setEnabled(False)                                  # kullanıcının seçim yapmasını engelliyoruz.

    def serialDisconnect(self) :            # "Bağlantı Kes" butonuna tıklandığında bu fonksiyona dallanacak.
        if self.mySerial.seriport.isOpen():
            self.mySerial.seriport.close()
            if self.mySerial.seriport.isOpen()== False:
                self.ui.ComState.setText('<font color=red>Bağlantı Kesildi</font>')
                self.ui.Baglan.setEnabled(True)                                        # Bağlantı varken tekrar bağlan butonuna tıklanmasın diye butonu pasif ediyoruz.
                self.ui.ComSelect.setEnabled(True)
                self.ui.ComSelect.setEnabled(True)   
        else:
            self.ui.ComState.setText("<font color=red>Seri POrt Zaten Kapalı.</font>".center())
        
    
    
    def Yakma(self) :
        if self.mySerial.seriport.isOpen():
            self.mySerial.seriport.write("1".encode())  # seri porttan Arduino'ya 1 karakteri gönderildi.
            self.ui.MessageKutusu.append("1")
        else:
            self.ui.MessageKutusu.append("Seri Port Bağlı Değil.")
    def sondur(self) :
        if self.mySerial.seriport.isOpen():
            self.mySerial.seriport.write("2".encode())  # seri porttan Arduino'ya 1 karakteri gönderildi.
            self.ui.MessageKutusu.append("2")


        else:
            self.ui.MessageKutusu.append("Seri Port Bağlı Değil.")

def mainLOOP():
    app = QApplication(sys.argv)
    window = Tasarla()
    sys.exit(app.exec_())
mainLOOP()