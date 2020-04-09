import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   IndicatorsButton = QPushButton(widget)
   IndicatorsButton.setText("Внести дані індикаторів")
   IndicatorsButton.move(64,32)
   IndicatorsButton.clicked.connect(menu2)

   UpdateButton = QPushButton(widget)
   UpdateButton.setText("Оновити дані")
   UpdateButton.move(64,64)
   UpdateButton.clicked.connect(button2_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("Menu")
   widget.show()
   sys.exit(app.exec_())


def indicators_menu():
  
   button1 = QPushButton(widget)
   button1.setText("1")
   button1.move(64,32)
   button1.clicked.connect(button2_clicked)


def button2_clicked():
   print("Button 2 clicked")   
def menu2():
    if __name__ == '__main__':
        indicators_menu()
if __name__ == '__main__':
   window()