# -*- coding: utf-8 -*-

import sys
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMessageBox,QInputDialog, QLineEdit,QDialogButtonBox,QVBoxLayout,QGridLayout, QHBoxLayout, QMainWindow, QDialog, QLabel, QComboBox, QPushButton, QToolBar, QAction, QStatusBar
from items import *

class CustomDialogLocation(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialogLocation, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Додати місце")
        self.left = 30
        self.top = 30
        self.width = 600
        self.height = 260
        self.setGeometry(self.left, self.top, self.width, self.height)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.validate)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QGridLayout()
        self.layout.addWidget(self.buttonBox,5,1)
        #Name
        self.textboxName = QLineEdit(self)
        self.labelName = QLabel("Назва")
        self.layout.addWidget(self.labelName,1,1)
        self.layout.addWidget(self.textboxName,1,2)
        #Subgroup
        self.comboBoxGroup = QComboBox(self)
        for i in list(subgroups.keys()):
            self.comboBoxGroup.addItem(i)
        self.menutext=list(subgroups.keys())[0]
        self.comboBoxGroup.activated[str].connect(self.change_text)
        self.labelGroup = QLabel("Область")
        self.layout.addWidget(self.labelGroup,2,1)
        self.layout.addWidget(self.comboBoxGroup,2,2)
        #Longtitude
        self.textboxLon = QLineEdit(self)
        self.labelLon = QLabel("Довгота")
        self.layout.addWidget(self.labelLon,3,1)
        self.layout.addWidget(self.textboxLon,3,2)
        #Latitude
        self.textboxLat = QLineEdit(self)
        self.labelLat = QLabel("Широта")
        self.layout.addWidget(self.labelLat,4,1)
        self.layout.addWidget(self.textboxLat,4,2)
        
        self.setLayout(self.layout)
    def validate(self):
        if self.textboxName.text()=='1':
            self.commit()
        else:
            self.labelwar = QLabel("Text")
            self.labelwar.setStyleSheet("background-color: red")
            self.labelwar.move(20, 40)
            self.labelwar.resize(280,40)
            self.layout.addWidget(self.labelwar,1,3)
    def change_text(self, text):
        self.menutext=text        
    def commit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        print(self.textboxName.text()+self.textboxLon.text()+self.textboxLat.text()+self.menutext)
        #QMessageBox.question(self,'Warning',(self.textboxName.text()+self.textboxLon.text()+self.textboxLat.text()+self.textboxGroup.text()), QMessageBox.Ok, QMessageBox.Ok)
        msg.setWindowTitle("Warning")
        msg.setText((self.textboxName.text()+self.textboxLon.text()+self.textboxLat.text()+self.menutext))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval=msg.exec_()
        print(retval)
        if retval==1024:
            print('Accepted')
            self.accept()
           
            
        elif retval==4194304:
            print('Not')
        
class CustomDialogUser(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialogUser, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Додати місце")
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.commit)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        #firstname
        self.textboxfirstname = QLineEdit(self)
        self.textboxfirstname.move(30, 20)
        self.textboxfirstname.resize(280,40)
        self.labelfirstname = QLabel("Ім'я")
        self.labelfirstname.move(20, 20)
        self.labelfirstname.resize(280,40)
        self.layout.addWidget(self.labelfirstname)
        self.layout.addWidget(self.textboxfirstname)
        #lastname
        self.textboxlastname = QLineEdit(self)
        self.textboxlastname.move(30, 20)
        self.textboxlastname.resize(280,40)
        self.labellastname = QLabel("Прізвище")
        self.labellastname.move(20, 20)
        self.labellastname.resize(280,40)
        self.layout.addWidget(self.labellastname)
        self.layout.addWidget(self.textboxlastname)
        self.setLayout(self.layout)
        #lastname
        self.textboxmail = QLineEdit(self)
        self.textboxmail.move(30, 20)
        self.textboxmail.resize(280,40)
        self.labelmail = QLabel("Електронна пошта")
        self.labelmail.move(20, 20)
        self.labelmail.resize(280,40)
        self.layout.addWidget(self.labelmail)
        self.layout.addWidget(self.textboxmail)
        self.setLayout(self.layout)
        
    def commit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        print(self.textboxfirstname.text()+self.textboxlastname.text()+self.textboxmail.text())
        #QMessageBox.question(self,'Warning',(self.textboxName.text()+self.textboxLon.text()+self.textboxLat.text()+self.textboxGroup.text()), QMessageBox.Ok, QMessageBox.Ok)
        msg.setWindowTitle("Warning")
        msg.setText((self.textboxfirstname.text()+self.textboxlastname.text()+self.textboxmail.text()))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        retval=msg.exec_()
        print(retval)
        if retval==1024:
            print('Accepted')
            self.accept()
        elif retval==4194304:
            print('Not')
            
class CustomDialogOrganisation(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialogOrganisation, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("HELLO!")
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class CustomDialogIndicator(QDialog):

    def __init__(self,indicator_name, *args, **kwargs):
        super(CustomDialogIndicator, self).__init__(*args, **kwargs)
        
        self.setWindowTitle(indicator_name)
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.commit)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        #firstname
        self.textboxval = QLineEdit(self)
        self.textboxval.move(30, 20)
        self.textboxval.resize(280,40)
        self.labelval = QLabel("Value")
        self.labelval.move(20, 20)
        self.labelval.resize(280,40)
        self.layout.addWidget(self.labelval)
        self.layout.addWidget(self.textboxval)
       
        self.setLayout(self.layout)
        
    def commit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        print(self.textboxval.text())
        #QMessageBox.question(self,'Warning',(self.textboxName.text()+self.textboxLon.text()+self.textboxLat.text()+self.textboxGroup.text()), QMessageBox.Ok, QMessageBox.Ok)
        msg.setWindowTitle("Warning")
        msg.setText(self.textboxval.text())
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        retval=msg.exec_()
        print(retval)
        if retval==1024:
            print('Accepted')
            self.accept()
        elif retval==4194304:
            print('Not')
            
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        
        button_action = QAction("Додати", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        comboBox = QComboBox(self)
        for i in fields:
            comboBox.addItem(i)
        comboBox.move(50, 250)
        self.menutext=fields[0]
        comboBox.activated[str].connect(self.change_text)
        toolbar.addAction(button_action)
        toolbar.addWidget(comboBox)
        
        self.setStatusBar(QStatusBar(self))
        
        
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)
        print(self.menutext)
        if self.menutext=="Місця":
            dlg = CustomDialogLocation(self)
            dlg.exec_()
        elif self.menutext=="Користувачі":
            dlg = CustomDialogUser(self)
            dlg.exec_()
        elif self.menutext=="Організації":
            dlg = CustomDialogOrganisation(self)
            dlg.exec_()
        else:
            dlg = CustomDialogIndicator(self.menutext)
            dlg.exec_()
    def change_text(self, text):
        self.menutext=text
        
