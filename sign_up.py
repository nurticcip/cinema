

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpWindow(object):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpWindow = QtWidgets.QWidget()
    ui = Ui_SignUpWindow()
    ui.setupUi(SignUpWindow)
    SignUpWindow.show()
    sys.exit(app.exec_())
