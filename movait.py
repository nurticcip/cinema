import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QScrollArea, QLineEdit, QVBoxLayout, QMessageBox,
    QWidget, QPushButton, QLabel, QMainWindow, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import sys
import random
import string
captcha_status = 0

main_user = ''
class Ui_Register(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(547, 713)
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setStyleSheet("backround-color:blue;\n"
"font-family:Noto Sans SC;")
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(170, 40, 221, 41))
        self.headerText.setStyleSheet("color:black;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;")
        self.headerText.setObjectName("headerText")
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(270, 550, 241, 51))
        self.registerButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(128, 128, 128); /* Серый цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 33px;\n"
"font-weight:500;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(169, 169, 169); /* Более светлый серый при нажатии */\n"
"}\n"
"")
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.register)
        self.main_frame = QtWidgets.QFrame(Dialog)
        self.main_frame.setGeometry(QtCore.QRect(40, 150, 471, 361))
        self.main_frame.setStyleSheet("backround-color:rgba(255,255,255,30);\n"
"border:1px solid rdba(255,255,255,40);\n"
"border-radius:7px;\n"
"")
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.usernameText = QtWidgets.QLabel(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        self.usernameText.setFont(font)
        self.usernameText.setStyleSheet("font-size:14pt;\n"
"background-color:none;\n"
"border:none;")
        self.usernameText.setObjectName("usernameText")
        self.verticalLayout_2.addWidget(self.usernameText)
        self.usernamInput = QtWidgets.QLineEdit(self.main_frame)
        self.usernamInput.setMinimumSize(QtCore.QSize(0, 50))
        self.usernamInput.setMaximumSize(QtCore.QSize(16777215, 20))
        self.usernamInput.setSizeIncrement(QtCore.QSize(0, 0))
        self.usernamInput.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        font.setKerning(True)
        self.usernamInput.setFont(font)
        self.usernamInput.setText("")
        self.usernamInput.setObjectName("usernamInput")
        self.verticalLayout_2.addWidget(self.usernamInput)
        self.passwordText = QtWidgets.QLabel(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        self.passwordText.setFont(font)
        self.passwordText.setStyleSheet("font-size:14pt;\n"
"background-color:none;\n"
"border:none;")
        self.passwordText.setObjectName("passwordText")
        self.verticalLayout_2.addWidget(self.passwordText)
        self.passwordInput = QtWidgets.QLineEdit(self.main_frame)
        self.passwordInput.setMinimumSize(QtCore.QSize(0, 50))
        self.passwordInput.setMaximumSize(QtCore.QSize(16777215, 20))
        self.passwordInput.setSizeIncrement(QtCore.QSize(0, 0))
        self.passwordInput.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        font.setKerning(True)
        self.passwordInput.setFont(font)
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.passwordInput)
        self.verifyPasswordText = QtWidgets.QLabel(self.main_frame)
        self.verifyPasswordText.setStyleSheet("font-size:14pt;\n"
"background-color:none;\n"
"border:none;")
        self.verifyPasswordText.setObjectName("verifyPasswordText")
        self.verticalLayout_2.addWidget(self.verifyPasswordText)
        self.verifyPasswordInput = QtWidgets.QLineEdit(self.main_frame)
        self.verifyPasswordInput.setMinimumSize(QtCore.QSize(0, 50))
        self.verifyPasswordInput.setMaximumSize(QtCore.QSize(16777215, 20))
        self.verifyPasswordInput.setSizeIncrement(QtCore.QSize(0, 0))
        self.verifyPasswordInput.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        font.setKerning(True)
        self.verifyPasswordInput.setFont(font)
        self.verifyPasswordInput.setText("")
        self.verifyPasswordInput.setObjectName("verifyPasswordInput")
        self.verifyPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.verifyPasswordInput)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "REGISTER"))
        self.registerButton.setText(_translate("Dialog", "register"))
        self.usernameText.setText(_translate("Dialog", "username:"))
        self.passwordText.setText(_translate("Dialog", "password:"))
        self.verifyPasswordText.setText(_translate("Dialog", "verify password:"))

    def register(self):
        name = self.usernamInput.text()
        password = self.passwordInput.text()
        confirm_password = self.verifyPasswordInput.text()
        if password == confirm_password:
            url = 'https://nurticcip.pythonanywhere.com/get_user'
            response = requests.get(url, params={'user': name})
            if response.json() != True:
                url = 'https://nurticcip.pythonanywhere.com/add_user'
                response = requests.get(url, params={'user': name, 'password': password})
                self.usernamInput.setText("")
                self.passwordInput.setText("")
                self.verifyPasswordInput.setText("")
                QtWidgets.QMessageBox.information(None, 'Success', "Succesfully added!")
                self.close()
            else:
                QtWidgets.QMessageBox.critical(None, 'Error', "Person already exist!")
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', "Passwords don't match!")
            self.passwordInput.setText("")
            self.verifyPasswordInput.setText("")

class Ui_SignUpWindow(QtWidgets.QWidget):
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(560, 681)
        self.headerText = QtWidgets.QLabel(SignUpWindow)
        self.headerText.setEnabled(True)
        self.headerText.setGeometry(QtCore.QRect(200, 30, 171, 45))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(24)
        font.setBold(True)
        self.headerText.setFont(font)
        self.headerText.setStyleSheet("color:black;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;\n"
"")
        self.headerText.setObjectName("headerText")
        self.main_frame = QtWidgets.QFrame(SignUpWindow)
        self.main_frame.setGeometry(QtCore.QRect(60, 140, 441, 271))
        self.main_frame.setStyleSheet("backround-color:rgba(255,255,255,30);\n"
"border:1px solid rdba(255,255,255,40);\n"
"border-radius:7px;\n"
"")
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.usernameText = QtWidgets.QLabel(self.main_frame)
        self.usernameText.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        self.usernameText.setFont(font)
        self.usernameText.setStyleSheet("font-size:14pt;\n"
"background-color:none;\n"
"border:none;")
        self.usernameText.setObjectName("usernameText")
        self.verticalLayout.addWidget(self.usernameText)
        self.usernameInput = QtWidgets.QLineEdit(self.main_frame)
        self.usernameInput.setMinimumSize(QtCore.QSize(0, 50))
        self.usernameInput.setMaximumSize(QtCore.QSize(16777215, 20))
        self.usernameInput.setSizeIncrement(QtCore.QSize(0, 0))
        self.usernameInput.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        font.setKerning(True)
        self.usernameInput.setFont(font)
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.verticalLayout.addWidget(self.usernameInput)
        self.passwordText = QtWidgets.QLabel(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        self.passwordText.setFont(font)
        self.passwordText.setStyleSheet("font-size:14pt;\n"
"background-color:none;\n"
"border:none;")
        self.passwordText.setObjectName("passwordText")
        self.verticalLayout.addWidget(self.passwordText)
        self.passwordInput = QtWidgets.QLineEdit(self.main_frame)
        self.passwordInput.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(12)
        self.passwordInput.setFont(font)
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.passwordInput)
        self.captchaCheckBox = QtWidgets.QCheckBox(SignUpWindow)
        self.captchaCheckBox.setGeometry(QtCore.QRect(220, 580, 121, 41))
        self.captchaCheckBox.setStyleSheet("font-size:16pt;\n"
"background-color:none;\n"
"border:none;\n"
"font-weight:500;")
        self.captchaCheckBox.setObjectName("captchaCheckBox")
        self.captchaCheckBox.clicked.connect(self.captcha_page)
        self.sign_inButton = QtWidgets.QPushButton(SignUpWindow)
        self.sign_inButton.setGeometry(QtCore.QRect(80, 510, 161, 51))
        self.sign_inButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(128, 128, 128); /* Серый цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 33px;\n"
"    font-weight: 500\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(169, 169, 169); /* Более светлый серый при нажатии */\n"
"}\n"
"")
        self.sign_inButton.setObjectName("sign_inButton")
        self.sign_inButton.clicked.connect(self.registerPage)
        self.sign_upButton = QtWidgets.QPushButton(SignUpWindow)
        self.sign_upButton.setGeometry(QtCore.QRect(320, 510, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setItalic(False)
        self.sign_upButton.setFont(font)
        self.sign_upButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 165, 0); /* Оранжевый цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 33px;\n"
"    font-weight: 500\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Темно-оранжевый цвет при нажатии */\n"
"}\n"
"")
        self.sign_upButton.setIconSize(QtCore.QSize(26, 26))
        self.sign_upButton.setObjectName("sign_upButton")
        self.sign_upButton.clicked.connect(self.checkPassword)

        self.retranslateUi(SignUpWindow)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "Form"))
        self.headerText.setText(_translate("SignUpWindow", "MOVAIT"))
        self.usernameText.setText(_translate("SignUpWindow", "username:"))
        self.passwordText.setText(_translate("SignUpWindow", "password:"))
        self.captchaCheckBox.setText(_translate("SignUpWindow", "captcha"))
        self.sign_inButton.setText(_translate("SignUpWindow", "sign in"))
        self.sign_upButton.setText(_translate("SignUpWindow", "sign up"))

        


    def registerPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkPassword(self):
        global main_user
        name = self.usernameInput.text()
        password = self.passwordInput.text()
        if len(name) > 0 and len(password) > 0:
            url = 'https://nurticcip.pythonanywhere.com/get_user'
            response = requests.get(url, params={'user': name})
            if response.json() == True:
                url = 'https://nurticcip.pythonanywhere.com/check_password'
                response = requests.get(url, params={'user': name, 'password': password})
                if response.json() == True:
                    if captcha_status == 1:
                        self.close()
                        main_user = name
                        self.window = MovieListApp()
                        self.window.show()
                    else:
                        QMessageBox.information(self, "Warning", "Check your captcha!")
                else:
                    QtWidgets.QMessageBox.critical(None, 'Error', 'Incorrect password!')
            else:
                QtWidgets.QMessageBox.critical(None, 'Error', "Can't find this person!")
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'Emplty input fields!')
            self.passwordInput.setText("")
            self.usernameInput.setText("")

    def captcha_page(self):
        self.window = CaptchaWindow()
        self.window.show()



class SeatGenerator(QWidget):  # Replace QWidget with the correct base class
    def __init__(self, time, movie):
        super().__init__()  # Properly initialize the parent class
        self.time = time
        self.movie = movie
        self.seats_now = []
        self.setupUi()

    def setupUi(self):
        self.setGeometry(100, 100, 1000, 700)  
        self.setWindowTitle('Hall') 

        self.setStyleSheet("background-color: rgb(13, 44, 62);")
        
        self.buy = QtWidgets.QPushButton('Buy',self)
        self.buy.setGeometry(QtCore.QRect(390, 610, 226, 41))
        
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.buy.setFont(font)
        self.buy.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(124, 166, 144);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.buy.clicked.connect(self.buy_ticket)        
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(453, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(561, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(615, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(507, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(291, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(238, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(399, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(723, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(884, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(831, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(669, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(777, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(13, 44, 62);\n")
        
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(76, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(130, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(184, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(346, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")



        
        self.label = QtWidgets.QLabel('Screen',self)
        self.label.setGeometry(QtCore.QRect(47, 27, 905, 28))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(197, 158, 81);\n"
"border-radius: 14px;")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Screen</span></p></body></html>"))

        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(952, 104, 39, 428))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(8, 104, 39, 428))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">A</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">B</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">C</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">D</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">E</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">F</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">G</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">H</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">I</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">J</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">A</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">B</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">C</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">D</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">E</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">F</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">G</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">H</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">I</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">J</span></p></body></html>"))
        
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">1</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">2</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">3</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">6</span></p></body></html>"))
        
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">8</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">10</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">11</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">9</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">5</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">4</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">7</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">13</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">16</span></p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">15</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">12</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">14</span></p></body></html>"))





        # Создаем кнопки
        self.create_buttons()

    def create_buttons(self):
        booked_seats = requests.get('http://nurticcip.pythonanywhere.com/get_movie_booked_seats', 
                                params={'movie': self.movie, 'seance': self.time}).json()
        rows = 'abcdefg' 
        cols = 10  
        x_start, y_start = 76, 104  
        button_width, button_height = 41, 30  
        x_gap, y_gap = 54, 44 

        for i, row in enumerate(rows):
            for col in range(1, cols + 1):
                seat_id = f'{row}{col}'  
                x = x_start + (col - 1) * x_gap
                y = y_start + i * y_gap
                button = QtWidgets.QPushButton(self)
                button.setGeometry(x, y, button_width, button_height)
                button.setFont(QtGui.QFont('Arial', 10))

                button.clicked.connect(self.make_button_click_handler(seat_id, button))

                if seat_id not in booked_seats:
                     button.setStyleSheet(self.get_button_styles_free())  # Style for free seats
                else:
                     button.setStyleSheet(self.get_button_styles_booked())  # Style for booked seats
                     button.setEnabled(False)  # Disable booked buttons

    def make_button_click_handler(self, seat_id, button):
        def handler():
            self.toggle_seat(seat_id, button)
        return handler

    def toggle_seat(self, seat_id, button):
        if seat_id in self.seats_now:
            self.seats_now.remove(seat_id) 
            button.setStyleSheet(self.get_button_styles_free()) 
        else:
            self.seats_now.append(seat_id) 
            button.setStyleSheet(self.get_button_styles_selected()) 

    def get_button_styles_free(self):
        return ("QPushButton:hover{\n"
        "    background-color: rgb(23, 137, 143);\n"
        "    color: rgb(255, 255, 255);\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:rgb(14, 85, 89);\n"
        "    color: rgb(255, 255, 255);\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px\n"
        "}\n"
        "QPushButton{\n"
        "background-color: rgb(124, 166, 144);\n"
        "color: rgb(0, 0, 0);\n"
        "font-size: 30px;\n"
        "border-radius: 8px\n"
        "}\n"
        "")

    def get_button_styles_selected(self):
        return (
                "QPushButton:hover{\n"
                "background-color: #de0000;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 30px;\n"
                "    border-radius: 8px\n"
                "}\n"
                "QPushButton:pressed{\n"
                "background-color: #7f0000;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 30px;\n"
                "    border-radius: 8px\n"
                "}\n"
                "QPushButton{\n"
                "background-color: #ff5733;\n"
                "color: rgb(0, 0, 0);\n"
                "font-size: 30px;\n"
                "border-radius: 8px\n"
                "}\n"
                ""
        )

    def get_button_styles_booked(self):
        return ("\n"
        "QPushButton {\n"
        "    background-color:  rgb(61, 61, 61); /* Серый фон */\n"
        "    color: rgb(0, 0, 0); /* Черный текст */\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color:  rgb(61, 61, 61); /* Сохраняем серый фон при наведении */\n"
        "    color: rgb(0, 0, 0); /* Сохраняем черный цвет текста при наведении */\n"
        "}")

    def buy_ticket(self):
        args = ','.join(self.seats_now)
        requests.get('http://nurticcip.pythonanywhere.com/movie_seance_booking', params={'user': main_user, 'movie': self.movie, 'seance': self.time, 'seats': args})
        self.close()

class MovieListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollable Movie List")
        self.setGeometry(400, 100, 500, 600)
        
        # Main container
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        
        # Upper layout for additional buttons
        upper_layout = QHBoxLayout()
        
        history_button = QPushButton("History")
        history_button.clicked.connect(self.userHistory)
        
        movie_info_button = QPushButton("Movie Info")
        movie_info_button.clicked.connect(self.movieInfo)
        
        update_button = QPushButton("Update Movie")
        update_button.clicked.connect(self.updateMovie)
        
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.refreshPage)
        
        upper_layout.addWidget(history_button)
        upper_layout.addWidget(movie_info_button)
        upper_layout.addWidget(update_button)
        upper_layout.addWidget(refresh_button)

        # Scroll area setup
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Load initial movie list
        self.loadMovieList()

        # Add upper layout and scroll area to main layout
        self.main_layout.addLayout(upper_layout)
        self.main_layout.addWidget(self.scroll_area)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def loadMovieList(self):
        """Loads the movie list into the scroll area."""
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)  # Vertical layout for movie widgets

        try:
            movies = requests.get('http://nurticcip.pythonanywhere.com/get_movies').json()
        except Exception as e:
            movies = []
            print(f"Error fetching movies: {e}")

        for movie in movies:
            movie_widget = self.create_movie_widget(movie)
            scroll_layout.addWidget(movie_widget)

        scroll_content.setLayout(scroll_layout)
        self.scroll_area.setWidget(scroll_content)

    def refreshPage(self):
        """Refreshes the movie list."""
        self.loadMovieList()

    def create_movie_widget(self, movie_name):
        """Create a widget for a single movie with buttons."""
        widget = QWidget()
        layout = QHBoxLayout()

        # Movie name label
        movie_label = QLabel(movie_name)
        layout.addWidget(movie_label)

        # Scene buttons
        scene1_button = QPushButton("10:30")
        scene2_button = QPushButton("12:20")
        scene3_button = QPushButton("14:10")

        # Connect buttons to corresponding methods
        scene1_button.clicked.connect(lambda: self.openHall1(movie_name))
        scene2_button.clicked.connect(lambda: self.openHall2(movie_name))
        scene3_button.clicked.connect(lambda: self.openHall3(movie_name))

        layout.addWidget(scene1_button)
        layout.addWidget(scene2_button)
        layout.addWidget(scene3_button)

        widget.setLayout(layout)
        return widget

    def openHall1(self, movie):
        self.hall1_window = SeatGenerator('10:30', movie)
        self.hall1_window.show()

    def openHall2(self, movie):
        self.hall2_window = SeatGenerator('12:20', movie)
        self.hall2_window.show()

    def openHall3(self, movie):
        self.hall3_window = SeatGenerator('14:10', movie)
        self.hall3_window.show()

    def updateMovie(self):
        self.window = QtWidgets.QWidget()
        self.ui = UpdateMoviePage()
        self.ui.setupUi(self.window)
        self.window.show()

    def movieInfo(self):
        self.window = QtWidgets.QWidget()
        self.ui = MovieInfo()
        self.ui.setupUi(self.window)
        self.window.show()

    def userHistory(self):
        self.window = QtWidgets.QWidget()
        self.ui = UserHistory()
        self.ui.setupUi(self.window)
        self.window.show()

class Window(QtWidgets.QMainWindow, Ui_SignUpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

class UpdateMoviePage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 701)
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(190, 30, 181, 51))
        self.headerText.setStyleSheet("color:black;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;")
        self.headerText.setObjectName("headerText")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 140, 471, 191))
        self.frame.setStyleSheet("backround-color:rgba(255,255,255,30);\n"
"border:1px solid rdba(255,255,255,40);\n"
"border-radius:6px;\n"
"font-size:12pt;")
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.fILMLabel = QtWidgets.QLabel(self.frame)
        self.fILMLabel.setObjectName("fILMLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fILMLabel)
        self.filmInput = QtWidgets.QLineEdit(self.frame)
        self.filmInput.setText("")
        self.filmInput.setObjectName("filmInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filmInput)
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(50, 205, 50); /* Лаймово-зелёный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(34, 139, 34); /* Тёмно-зелёный цвет при нажатии */\n"
"}\n"
"\n"
"")
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.add_movie)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.addButton)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(40, 390, 471, 191))
        self.frame_2.setStyleSheet("backround-color:rgba(255,255,255,30);\n"
"border:1px solid rdba(255,255,255,40);\n"
"border-radius:6px;\n"
"font-size:12pt;")
        self.frame_2.setObjectName("frame_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.filmDel = QtWidgets.QLabel(self.frame_2)
        self.filmDel.setObjectName("filmDel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.filmDel)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.deleteButton = QtWidgets.QPushButton(self.frame_2)
        self.deleteButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 30px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"\n"
"")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.delete_movie)
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deleteButton)
        self.getMoviesList()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "UPDATE MOVIE"))
        self.fILMLabel.setText(_translate("Dialog", "FILM:"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.filmDel.setText(_translate("Dialog", "FILM:"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))

    def getMoviesList(self):
        self.comboBox.clear()
        movies_list = requests.get('http://nurticcip.pythonanywhere.com/get_movies').json()
        for i in movies_list:
            self.comboBox.addItem(i)


    def add_movie(self):
        movie = self.filmInput.text()
        requests.get('http://nurticcip.pythonanywhere.com/add_movie', params={'movie':movie})
        self.getMoviesList()
        self.filmInput.setText("")

    def delete_movie(self):
        movie = self.comboBox.currentText()
        requests.get('http://nurticcip.pythonanywhere.com/delete_movie', params={'movie':movie})
        self.getMoviesList()

class MovieInfo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 701)
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(190, 20, 141, 51))
        self.headerText.setStyleSheet("color:#fff;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;")
        self.headerText.setObjectName("headerText")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 160, 421, 261))
        self.frame.setStyleSheet("backround-color:rgba(255,255,255,30);\n"
"border:1px solid rdba(255,255,255,40);\n"
"border-radius:6px;\n"
"font-size:12pt;")
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.filmText = QtWidgets.QLabel(self.frame)
        self.filmText.setObjectName("filmText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.filmText)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.get_movie_history)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.peopleLabel = QtWidgets.QLabel(self.frame)
        self.peopleLabel.setObjectName("peopleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.peopleLabel)
        self.listUsers = QtWidgets.QListWidget(self.frame)
        self.listUsers.setObjectName("listUsers")
      
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.listUsers)
        self.getMoviesList()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "MOVIE INFO"))
        self.filmText.setText(_translate("Dialog", "FILM:"))
        self.peopleLabel.setText(_translate("Dialog", "PEOPLE:"))
        __sortingEnabled = self.listUsers.isSortingEnabled()
        self.listUsers.setSortingEnabled(False)
        self.listUsers.setSortingEnabled(__sortingEnabled)

    def getMoviesList(self):
        self.comboBox.clear()
        movies_list = requests.get('http://nurticcip.pythonanywhere.com/get_movies').json()
        for i in movies_list:

                self.comboBox.addItem(i)

    def get_movie_history(self):
        self.listUsers.clear()
        movie = self.comboBox.currentText()
        history = requests.get('http://nurticcip.pythonanywhere.com/get_movie_history', params={'movie':movie}).json()
        arr = set()
        for i in history:
            arr.add(tuple(i))
        text = []
        for i in list(arr):
            text.append(f'{i[0]} --> {i[1]}')
        for i in text:
            self.listUsers.addItem(i)

class UserHistory(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 705)
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(200, 20, 181, 61))
        self.headerText.setStyleSheet("color:black;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;")
        self.headerText.setObjectName("headerText")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(60, 190, 421, 311))
        self.frame.setStyleSheet("backround-color:rgba(255,255,255,30);\n"
"border:1px solid rdba(255,255,255,40);\n"
"border-radius:6px;\n"
"font-size:12pt;")
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.clientLabel = QtWidgets.QLabel(self.frame)
        self.clientLabel.setObjectName("clientLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.clientLabel)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.get_user_history)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.infoLabel = QtWidgets.QLabel(self.frame)
        self.infoLabel.setObjectName("infoLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.infoLabel)
        self.listInfo = QtWidgets.QListWidget(self.frame)
        self.listInfo.setObjectName("listInfo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.listInfo)



        self.get_users_list()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "USER HISTORY"))
        self.clientLabel.setText(_translate("Dialog", "client:"))
        self.infoLabel.setText(_translate("Dialog", "movie:"))
        __sortingEnabled = self.listInfo.isSortingEnabled()
        self.listInfo.setSortingEnabled(False)
        self.listInfo.setSortingEnabled(__sortingEnabled)

    def get_users_list(self):
        self.comboBox.clear()
        users = requests.get('http://nurticcip.pythonanywhere.com/get_users_list').json()
        for i in users:
            self.comboBox.addItem(i)

    def get_user_history(self):
        self.listInfo.clear()
        user = self.comboBox.currentText()
        history = requests.get('http://nurticcip.pythonanywhere.com/get_user_history', params={'user':user}).json()
        arr = set()
        for i in history:
            arr.add(tuple(i))
        text = []
        for i in list(arr):
            text.append(f'{i[0]} --> {i[1]}')
        for i in text:
            self.listInfo.addItem(i)

class CaptchaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAPTCHA")
        self.captcha_text = self.generate_captcha()

        # CAPTCHA Label
        self.captcha_label = QLabel(self)
        self.captcha_label.setPixmap(self.generate_captcha_image(self.captcha_text))

        # CAPTCHA Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter CAPTCHA here")

        # CAPTCHA Checkbox
        self.captcha_checkbox = QCheckBox("I am not a robot", self)

        # Submit Button
        self.submit_button = QPushButton("Sign Up", self)
        self.submit_button.clicked.connect(self.validate_signup)

        # Layout Setup
        layout = QVBoxLayout()
        layout.addWidget(self.captcha_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.captcha_checkbox)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def generate_captcha(self):
        """Generate a random CAPTCHA string."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def generate_captcha_image(self, text):
        """Create a CAPTCHA image from text."""
        image = QImage(200, 50, QImage.Format_RGB32)
        image.fill(QColor("white"))

        painter = QPainter(image)
        painter.setFont(QFont("Arial", 22))
        painter.setPen(QColor("black"))

        # Randomly distort the text
        for i, char in enumerate(text):
            x = 30 + i * 25
            y = random.randint(20, 40)
            painter.drawText(x, y, char)

        painter.end()

        return QPixmap.fromImage(image)

    def validate_signup(self):
        """Validate CAPTCHA and checkbox."""
        user_input = self.input_field.text().strip()
        checkbox_checked = self.captcha_checkbox.isChecked()

        if not checkbox_checked:
            QMessageBox.warning(self, "Error", "Please confirm the checkbox to prove you're not a robot.")
        elif user_input != self.captcha_text:
            QMessageBox.warning(self, "Error", "Invalid CAPTCHA. Please try again.")
            # Regenerate CAPTCHA
            self.captcha_text = self.generate_captcha()
            self.captcha_label.setPixmap(self.generate_captcha_image(self.captcha_text))
            self.input_field.clear()
        else:
            QMessageBox.information(self, "Success", "Sign up successful!")
            global captcha_status
            captcha_status = 1
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

