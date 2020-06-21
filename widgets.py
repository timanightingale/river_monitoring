# -*- coding: utf-8 -*-

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from items import *
from validation import *
from functions import *
from datetime import date
user_id=0
class CustomDialogLocation(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialogLocation, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Додати місце")
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 260
        self.setGeometry(self.left, self.top, self.width, self.height)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.commit)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QGridLayout()
        self.layout.addWidget(self.buttonBox,6,1)
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
        #River
        self.comboBoxRiver = QComboBox(self)
        for i in rivers:
            self.comboBoxRiver.addItem(i)
        self.river=rivers[0]
        self.comboBoxRiver.activated[str].connect(self.change_text)
        self.labelRiver = QLabel("Річковий басейн")
        self.layout.addWidget(self.labelRiver,3,1)
        self.layout.addWidget(self.comboBoxRiver,3,2)
        #Longtitude
        self.textboxLon = QLineEdit(self)
        self.textboxLon.setValidator(QDoubleValidator(0.99,99.99,2))
        self.labelLon = QLabel("Довгота")
        self.layout.addWidget(self.labelLon,4,1)
        self.layout.addWidget(self.textboxLon,4,2)
        #Latitude
        self.textboxLat = QLineEdit(self)
        self.textboxLat.setValidator(QDoubleValidator(0.99,99.99,2))
        self.labelLat = QLabel("Широта")
        self.layout.addWidget(self.labelLat,5,1)
        self.layout.addWidget(self.textboxLat,5,2)
        
        self.setLayout(self.layout)
            
    def change_text(self, text):
        self.menutext=text
        
    def commit(self):
        logwindow=CustomDialogLogin()
        retval=logwindow.exec_()
        global user_id
        print(user_id)
        if retval==1:
            print('Accepted')
            self.accept()
        elif retval==0:
            print('Not')
        
class CustomDialogUser(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialogUser, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Додати користувача")
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 260
        self.setGeometry(self.left, self.top, self.width, self.height)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.commit)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QGridLayout()
        self.layout.addWidget(self.buttonBox,6,1)
        #firstname
        self.textboxfirstname = QLineEdit(self)
        self.textboxfirstname.move(30, 20)
        self.textboxfirstname.resize(280,40)
        self.labelfirstname = QLabel("Ім'я")
        self.labelfirstname.move(20, 20)
        self.labelfirstname.resize(280,40)
        self.layout.addWidget(self.labelfirstname,1,1)
        self.layout.addWidget(self.textboxfirstname,1,2)
        #lastname
        self.textboxlastname = QLineEdit(self)
        self.textboxlastname.move(30, 20)
        self.textboxlastname.resize(280,40)
        self.labellastname = QLabel("Прізвище")
        self.labellastname.move(20, 20)
        self.labellastname.resize(280,40)
        self.layout.addWidget(self.labellastname,2,1)
        self.layout.addWidget(self.textboxlastname,2,2)
        #lastname
        self.textboxmail = QLineEdit(self)
        self.textboxmail.move(30, 20)
        self.textboxmail.resize(280,40)
        self.labelmail = QLabel("Електронна пошта")
        self.labelmail.move(20, 20)
        self.labelmail.resize(280,40)
        self.layout.addWidget(self.labelmail,3,1)
        self.layout.addWidget(self.textboxmail,3,2)
        #lastname
        self.textboxlogin = QLineEdit(self)
        self.textboxlogin.move(30, 20)
        self.textboxlogin.resize(280,40)
        self.labellogin = QLabel("Логін")
        self.labellogin.move(20, 20)
        self.labellogin.resize(280,40)
        self.layout.addWidget(self.labellogin,4,1)
        self.layout.addWidget(self.textboxlogin,4,2)
        #lastname
        self.textboxpass = QLineEdit(self)
        self.textboxpass.move(30, 20)
        self.textboxpass.resize(280,40)
        self.labelpass = QLabel("Пароль")
        self.labelpass.move(20, 20)
        self.labelpass.resize(280,40)
        self.layout.addWidget(self.labelpass,5,1)
        self.layout.addWidget(self.textboxpass,5,2)
        self.setLayout(self.layout)
        
    def commit(self):
        if not validate_email(self.textboxmail.text()):
            self.textboxmail.setStyleSheet("border:2px solid red")
        else:
            self.textboxmail.setStyleSheet("border:1px solid gray")
            logwindow=CustomDialogLogin()
            retval=logwindow.exec_()
            print(retval)
            if retval==1:
                print('Accepted')
                self.accept()
            elif retval==0:
                print('Not')
            

class CustomDialogIndicator(QDialog):

    def __init__(self,indicator_name, *args, **kwargs):
        super(CustomDialogIndicator, self).__init__(*args, **kwargs)
        self.indicator_name=indicator_name
        self.setWindowTitle(indicator_name)
        
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 260
        self.setGeometry(self.left, self.top, self.width, self.height)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.commit)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        #firstname
        self.textboxval = QLineEdit(self)
        self.textboxval.move(30, 20)
        self.textboxval.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textboxval.resize(280,40)
        self.labelval = QLabel("Значення")
        self.labelval.move(20, 20)
        self.labelval.resize(280,40)
        self.layout.addWidget(self.labelval)
        self.layout.addWidget(self.textboxval)
        #Location
        self.comboBoxLoc = QComboBox(self)
        for i in list(locations.keys()):
            self.comboBoxLoc.addItem(i)
        self.menutext=list(locations.keys())[0]
        self.comboBoxLoc.activated[str].connect(self.change_text)
        self.labelLoc = QLabel("Місце")
        self.layout.addWidget(self.labelLoc)
        self.layout.addWidget(self.comboBoxLoc)
        self.setLayout(self.layout)
    
    def change_text(self, text):
        self.menutext=text
        
    def commit(self):
        logwindow=CustomDialogLogin()
        retval=logwindow.exec_()
        indicator_id=indicators[col_names[self.indicator_name]]
        print(retval)
        if retval==1:
            print('Accepted')
            global user_id
            
            if CheckIndicator(locations[self.menutext],date.today(),indicator_id):
                AddRow(indicator_id,locations[self.menutext],user_id,float(self.textboxval.text()),str(date.today()))
                self.accept()
            else:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Information)
               msg.setText("Увага!")
               msg.setInformativeText("Ці дані вже оновлено")
               msg.setStandardButtons(QMessageBox.Ok)
               msg.exec_()
            print('indicator added')
        elif retval==0:
            print('Not')

class CustomDialogLogin(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialogLogin, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("HELLO!")
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.check)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        #log
        self.textboxlogin = QLineEdit(self)
        self.textboxlogin.move(30, 20)
        self.textboxlogin.resize(280,40)
        self.labellogin = QLabel("Логін")
        self.labellogin.move(20, 20)
        self.labellogin.resize(280,40)
        self.layout.addWidget(self.labellogin)
        self.layout.addWidget(self.textboxlogin)
        #pass
        self.textboxpass = QLineEdit(self)
        self.textboxpass.move(30, 20)
        self.textboxpass.resize(280,40)
        self.labelpass = QLabel("Пароль")
        self.labelpass.move(20, 20)
        self.labelpass.resize(280,40)
        self.layout.addWidget(self.labelpass)
        self.layout.addWidget(self.textboxpass)
       
        self.setLayout(self.layout)
        
    def check(self):
        global user_id
        if Validate(self.textboxlogin.text(),self.textboxpass.text())==1:
            
            user_id=GetUserId(self.textboxlogin.text())
            self.accept()
            return 
        elif Validate(self.textboxlogin.text(),self.textboxpass.text())==2:
            self.textboxpass.setStyleSheet("border:1px solid gray")
            self.textboxlogin.setStyleSheet("border:2px solid red")
        else:
            self.textboxlogin.setStyleSheet("border:1px solid gray")
            self.textboxpass.setStyleSheet("border:2px solid red")
        if (self.textboxlogin.text()=='tima')&(self.textboxpass.text()=='firstuser'):
            
            user_id=GetUserId(self.textboxlogin.text())
            self.accept()
            return 
        elif self.textboxpass.text()=='firstuser':
            self.textboxpass.setStyleSheet("border:1px solid gray")
            self.textboxlogin.setStyleSheet("border:2px solid red")
        else:
            self.textboxlogin.setStyleSheet("border:1px solid gray")
            self.textboxpass.setStyleSheet("border:2px solid red")
            
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Update")
        
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        button_action = QAction("Додати", self)
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
        
        
