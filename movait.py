import requests
from PyQt5 import QtCore, QtGui, QtWidgets

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

class Ui_MoviesInfo(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 706)
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(200, 20, 181, 51))
        self.headerText.setStyleSheet("color:black;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;")
        self.headerText.setObjectName("headerText")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 220, 481, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        self.time1330 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1330.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1330.setObjectName("time1330")
        self.gridLayout.addWidget(self.time1330, 5, 4, 1, 1)
        self.time1410 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1410.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1410.setObjectName("time1410")
        self.gridLayout.addWidget(self.time1410, 5, 2, 1, 1)
        self.time1430 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1430.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1430.setObjectName("time1430")
        self.gridLayout.addWidget(self.time1430, 5, 3, 1, 1)
        self.time1200 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1200.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1200.setObjectName("time1200")
        self.gridLayout.addWidget(self.time1200, 5, 5, 1, 1)
        self.time2030 = QtWidgets.QPushButton(self.layoutWidget)
        self.time2030.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time2030.setObjectName("time2030")
        self.gridLayout.addWidget(self.time2030, 2, 5, 1, 1)
        self.time1650 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1650.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1650.setObjectName("time1650")
        self.gridLayout.addWidget(self.time1650, 2, 4, 1, 1)
        self.time1045 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1045.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1045.setObjectName("time1045")
        self.gridLayout.addWidget(self.time1045, 3, 2, 1, 1)
        self.gladiator2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.gladiator2.setFont(font)
        self.gladiator2.setObjectName("gladiator2")
        self.gridLayout.addWidget(self.gladiator2, 3, 1, 1, 1)
        self.time1150 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1150.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1150.setObjectName("time1150")
        self.gridLayout.addWidget(self.time1150, 0, 3, 1, 1)
        self.moana2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.moana2.setFont(font)
        self.moana2.setObjectName("moana2")
        self.gridLayout.addWidget(self.moana2, 0, 1, 1, 1)
        self.time1030 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1030.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1030.setObjectName("time1030")
        self.gridLayout.addWidget(self.time1030, 0, 2, 1, 1)
        self.time1540 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1540.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1540.setObjectName("time1540")
        self.gridLayout.addWidget(self.time1540, 0, 4, 1, 1)
        self.venom3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.venom3.setFont(font)
        self.venom3.setObjectName("venom3")
        self.gridLayout.addWidget(self.venom3, 1, 1, 1, 1)
        self.time2000 = QtWidgets.QPushButton(self.layoutWidget)
        self.time2000.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time2000.setObjectName("time2000")
        self.gridLayout.addWidget(self.time2000, 0, 5, 1, 1)
        self.time1100 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1100.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1100.setObjectName("time1100")
        self.gridLayout.addWidget(self.time1100, 1, 2, 1, 1)
        self.time1335 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1335.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1335.setObjectName("time1335")
        self.gridLayout.addWidget(self.time1335, 1, 3, 1, 1)
        self.time1800 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1800.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1800.setObjectName("time1800")
        self.gridLayout.addWidget(self.time1800, 1, 5, 1, 1)
        self.time1640 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1640.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1640.setObjectName("time1640")
        self.gridLayout.addWidget(self.time1640, 1, 4, 1, 1)
        self.homeAlone = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.homeAlone.setFont(font)
        self.homeAlone.setObjectName("homeAlone")
        self.gridLayout.addWidget(self.homeAlone, 2, 1, 1, 1)
        self.time1000 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1000.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1000.setObjectName("time1000")
        self.gridLayout.addWidget(self.time1000, 2, 2, 1, 1)
        self.time1420 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1420.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1420.setObjectName("time1420")
        self.gridLayout.addWidget(self.time1420, 2, 3, 1, 1)
        self.time2105 = QtWidgets.QPushButton(self.layoutWidget)
        self.time2105.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time2105.setObjectName("time2105")
        self.gridLayout.addWidget(self.time2105, 3, 5, 1, 1)
        self.time1500 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1500.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1500.setObjectName("time1500")
        self.gridLayout.addWidget(self.time1500, 3, 3, 1, 1)
        self.time1755 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1755.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1755.setObjectName("time1755")
        self.gridLayout.addWidget(self.time1755, 3, 4, 1, 1)
        self.evil = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.evil.setFont(font)
        self.evil.setObjectName("evil")
        self.gridLayout.addWidget(self.evil, 5, 1, 1, 1)
        self.time1415 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1415.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1415.setObjectName("time1415")
        self.gridLayout.addWidget(self.time1415, 4, 2, 1, 1)
        self.time1810 = QtWidgets.QPushButton(self.layoutWidget)
        self.time1810.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time1810.setObjectName("time1810")
        self.gridLayout.addWidget(self.time1810, 4, 3, 1, 1)
        self.evil2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.evil2.setFont(font)
        self.evil2.setObjectName("evil2")
        self.gridLayout.addWidget(self.evil2, 4, 1, 1, 1)
        self.time2310 = QtWidgets.QPushButton(self.layoutWidget)
        self.time2310.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time2310.setObjectName("time2310")
        self.gridLayout.addWidget(self.time2310, 4, 5, 1, 1)
        self.time2130 = QtWidgets.QPushButton(self.layoutWidget)
        self.time2130.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(173, 216, 230); /* Светлый голубой цвет */\n"
"    color: rgb(0, 0, 0); /* Черный цвет текста для контраста */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(135, 206, 250); /* Чуть более насыщенный голубой при нажатии */\n"
"}")
        self.time2130.setObjectName("time2130")
        self.gridLayout.addWidget(self.time2130, 4, 4, 1, 1)
        self.updateButton = QtWidgets.QPushButton(Dialog)
        self.updateButton.setGeometry(QtCore.QRect(380, 120, 141, 41))
        self.updateButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 165, 0); /* Оранжевый цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 20px;\n"
"    font-weight: 500\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Темно-оранжевый цвет при нажатии */\n"
"}\n"
"")
        self.updateButton.setObjectName("updateButton")
        self.movieInfoButton = QtWidgets.QPushButton(Dialog)
        self.movieInfoButton.setGeometry(QtCore.QRect(210, 120, 151, 41))
        self.movieInfoButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 165, 0); /* Оранжевый цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 20px;\n"
"    font-weight: 500\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Темно-оранжевый цвет при нажатии */\n"
"}\n"
"")
        self.movieInfoButton.setObjectName("movieInfoButton")
        self.historyButton = QtWidgets.QPushButton(Dialog)
        self.historyButton.setGeometry(QtCore.QRect(40, 120, 151, 41))
        self.historyButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 165, 0); /* Оранжевый цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 20px;\n"
"    font-weight: 500\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Темно-оранжевый цвет при нажатии */\n"
"}\n"
"")
        self.historyButton.setObjectName("historyButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "MOVIES"))
        self.time1330.setText(_translate("Dialog", "13:30"))
        self.time1410.setText(_translate("Dialog", "14:10"))
        self.time1430.setText(_translate("Dialog", "14:30"))
        self.time1200.setText(_translate("Dialog", "12:00"))
        self.time2030.setText(_translate("Dialog", "20:30"))
        self.time1650.setText(_translate("Dialog", "16:50"))
        self.time1045.setText(_translate("Dialog", "10:45"))
        self.gladiator2.setText(_translate("Dialog", "Gladiator 2"))
        self.time1150.setText(_translate("Dialog", "11:50"))
        self.moana2.setText(_translate("Dialog", " Moana 2"))
        self.time1030.setText(_translate("Dialog", "10:30"))
        self.time1540.setText(_translate("Dialog", "15:40"))
        self.venom3.setText(_translate("Dialog", "Venom 3"))
        self.time2000.setText(_translate("Dialog", "20:00"))
        self.time1100.setText(_translate("Dialog", "11:00"))
        self.time1335.setText(_translate("Dialog", "13:35"))
        self.time1800.setText(_translate("Dialog", "18:00"))
        self.time1640.setText(_translate("Dialog", "16:40"))
        self.homeAlone.setText(_translate("Dialog", "Home alone"))
        self.time1000.setText(_translate("Dialog", "10:00"))
        self.time1420.setText(_translate("Dialog", "14:20"))
        self.time2105.setText(_translate("Dialog", "21:05"))
        self.time1500.setText(_translate("Dialog", "15:00"))
        self.time1755.setText(_translate("Dialog", "17:55"))
        self.evil.setText(_translate("Dialog", "Evil"))
        self.time1415.setText(_translate("Dialog", "14:15"))
        self.time1810.setText(_translate("Dialog", "18:10"))
        self.evil2.setText(_translate("Dialog", "Evil"))
        self.time2310.setText(_translate("Dialog", "23:10"))
        self.time2130.setText(_translate("Dialog", "21:30"))
        self.updateButton.setText(_translate("Dialog", "Udate"))
        self.movieInfoButton.setText(_translate("Dialog", "Movie info"))
        self.historyButton.setText(_translate("Dialog", "History"))

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
        name = self.usernameInput.text()
        password = self.passwordInput.text()
        if len(name) > 0 and len(password) > 0:
            url = 'https://nurticcip.pythonanywhere.com/get_user'
            response = requests.get(url, params={'user': name})
            if response.json() == True:
                url = 'https://nurticcip.pythonanywhere.com/check_password'
                response = requests.get(url, params={'user': name, 'password': password})
                if response.json() == True:
                    self.close()
                    self.window = QtWidgets.QWidget()
                    self.ui = Ui_MoviesInfo()
                    self.ui.setupUi(self.window)
                    self.window.show()
                else:
                    QtWidgets.QMessageBox.critical(None, 'Error', 'Incorrect password!')
            else:
                QtWidgets.QMessageBox.critical(None, 'Error', "Can't find this person!")
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'Emplty input fields!')


            






class Window(QtWidgets.QMainWindow, Ui_SignUpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

