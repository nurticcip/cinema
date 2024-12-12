# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seats.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(547, 708)
        self.buyButton = QtWidgets.QPushButton(Dialog)
        self.buyButton.setGeometry(QtCore.QRect(330, 560, 151, 51))
        self.buyButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(50, 205, 50); /* Лаймово-зелёный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 30px;\n"
"    font-weight: 500\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(34, 139, 34); /* Тёмно-зелёный цвет при нажатии */\n"
"}")
        self.buyButton.setObjectName("buyButton")
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(210, 30, 141, 41))
        self.headerText.setStyleSheet("color:black;\n"
"font-weight:bold;\n"
"font-size:24pt;\n"
"background-color:none;\n"
"border:none;")
        self.headerText.setObjectName("headerText")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 120, 441, 361))
        self.frame.setStyleSheet("font-size:14pt;\n"
"background-color:none;\n"
"border:none;")
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.A2 = QtWidgets.QPushButton(self.frame)
        self.A2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.A2.setText("")
        self.A2.setObjectName("A2")
        self.gridLayout.addWidget(self.A2, 1, 2, 1, 1)
        self.B5 = QtWidgets.QPushButton(self.frame)
        self.B5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.B5.setText("")
        self.B5.setObjectName("B5")
        self.gridLayout.addWidget(self.B5, 3, 5, 1, 1)
        self.B7 = QtWidgets.QPushButton(self.frame)
        self.B7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.B7.setText("")
        self.B7.setObjectName("B7")
        self.gridLayout.addWidget(self.B7, 3, 8, 1, 1)
        self.C3 = QtWidgets.QPushButton(self.frame)
        self.C3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.C3.setText("")
        self.C3.setObjectName("C3")
        self.gridLayout.addWidget(self.C3, 4, 3, 1, 1)
        self.C1 = QtWidgets.QPushButton(self.frame)
        self.C1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.C1.setText("")
        self.C1.setObjectName("C1")
        self.gridLayout.addWidget(self.C1, 4, 1, 1, 1)
        self.C2 = QtWidgets.QPushButton(self.frame)
        self.C2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.C2.setText("")
        self.C2.setObjectName("C2")
        self.gridLayout.addWidget(self.C2, 4, 2, 1, 1)
        self.C6 = QtWidgets.QPushButton(self.frame)
        self.C6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.C6.setText("")
        self.C6.setObjectName("C6")
        self.gridLayout.addWidget(self.C6, 4, 6, 1, 1)
        self.C4 = QtWidgets.QPushButton(self.frame)
        self.C4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.C4.setText("")
        self.C4.setObjectName("C4")
        self.gridLayout.addWidget(self.C4, 4, 4, 1, 1)
        self.D1 = QtWidgets.QPushButton(self.frame)
        self.D1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D1.setText("")
        self.D1.setObjectName("D1")
        self.gridLayout.addWidget(self.D1, 5, 1, 1, 1)
        self.D2 = QtWidgets.QPushButton(self.frame)
        self.D2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D2.setText("")
        self.D2.setObjectName("D2")
        self.gridLayout.addWidget(self.D2, 5, 2, 1, 1)
        self.D4 = QtWidgets.QPushButton(self.frame)
        self.D4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D4.setText("")
        self.D4.setObjectName("D4")
        self.gridLayout.addWidget(self.D4, 5, 4, 1, 1)
        self.C7 = QtWidgets.QPushButton(self.frame)
        self.C7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.C7.setText("")
        self.C7.setObjectName("C7")
        self.gridLayout.addWidget(self.C7, 4, 8, 1, 1)
        self.C5 = QtWidgets.QPushButton(self.frame)
        self.C5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.C5.setText("")
        self.C5.setObjectName("C5")
        self.gridLayout.addWidget(self.C5, 4, 5, 1, 1)
        self.D6 = QtWidgets.QPushButton(self.frame)
        self.D6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D6.setText("")
        self.D6.setObjectName("D6")
        self.gridLayout.addWidget(self.D6, 5, 6, 1, 1)
        self.D7 = QtWidgets.QPushButton(self.frame)
        self.D7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D7.setText("")
        self.D7.setObjectName("D7")
        self.gridLayout.addWidget(self.D7, 5, 8, 1, 1)
        self.D5 = QtWidgets.QPushButton(self.frame)
        self.D5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.D5.setText("")
        self.D5.setObjectName("D5")
        self.gridLayout.addWidget(self.D5, 5, 5, 1, 1)
        self.D3 = QtWidgets.QPushButton(self.frame)
        self.D3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D3.setText("")
        self.D3.setObjectName("D3")
        self.gridLayout.addWidget(self.D3, 5, 3, 1, 1)
        self.D8 = QtWidgets.QPushButton(self.frame)
        self.D8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.D8.setText("")
        self.D8.setObjectName("D8")
        self.gridLayout.addWidget(self.D8, 5, 9, 1, 1)
        self.number4 = QtWidgets.QLabel(self.frame)
        self.number4.setObjectName("number4")
        self.gridLayout.addWidget(self.number4, 0, 4, 1, 1)
        self.C8 = QtWidgets.QPushButton(self.frame)
        self.C8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.C8.setText("")
        self.C8.setObjectName("C8")
        self.gridLayout.addWidget(self.C8, 4, 9, 1, 1)
        self.number2 = QtWidgets.QLabel(self.frame)
        self.number2.setObjectName("number2")
        self.gridLayout.addWidget(self.number2, 0, 2, 1, 1)
        self.number1 = QtWidgets.QLabel(self.frame)
        self.number1.setObjectName("number1")
        self.gridLayout.addWidget(self.number1, 0, 1, 1, 1)
        self.number5 = QtWidgets.QLabel(self.frame)
        self.number5.setObjectName("number5")
        self.gridLayout.addWidget(self.number5, 0, 5, 1, 1)
        self.number8 = QtWidgets.QLabel(self.frame)
        self.number8.setObjectName("number8")
        self.gridLayout.addWidget(self.number8, 0, 9, 1, 1)
        self.letterH = QtWidgets.QLabel(self.frame)
        self.letterH.setObjectName("letterH")
        self.gridLayout.addWidget(self.letterH, 11, 0, 1, 1)
        self.number6 = QtWidgets.QLabel(self.frame)
        self.number6.setObjectName("number6")
        self.gridLayout.addWidget(self.number6, 0, 6, 1, 1)
        self.number7 = QtWidgets.QLabel(self.frame)
        self.number7.setObjectName("number7")
        self.gridLayout.addWidget(self.number7, 0, 8, 1, 1)
        self.letterC = QtWidgets.QLabel(self.frame)
        self.letterC.setObjectName("letterC")
        self.gridLayout.addWidget(self.letterC, 4, 0, 1, 1)
        self.letterF = QtWidgets.QLabel(self.frame)
        self.letterF.setObjectName("letterF")
        self.gridLayout.addWidget(self.letterF, 9, 0, 1, 1)
        self.letterB = QtWidgets.QLabel(self.frame)
        self.letterB.setObjectName("letterB")
        self.gridLayout.addWidget(self.letterB, 3, 0, 1, 1)
        self.letterA = QtWidgets.QLabel(self.frame)
        self.letterA.setObjectName("letterA")
        self.gridLayout.addWidget(self.letterA, 1, 0, 1, 1)
        self.letterE = QtWidgets.QLabel(self.frame)
        self.letterE.setObjectName("letterE")
        self.gridLayout.addWidget(self.letterE, 8, 0, 1, 1)
        self.letterD = QtWidgets.QLabel(self.frame)
        self.letterD.setObjectName("letterD")
        self.gridLayout.addWidget(self.letterD, 5, 0, 1, 1)
        self.letterG = QtWidgets.QLabel(self.frame)
        self.letterG.setObjectName("letterG")
        self.gridLayout.addWidget(self.letterG, 10, 0, 1, 1)
        self.H4 = QtWidgets.QPushButton(self.frame)
        self.H4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.H4.setText("")
        self.H4.setObjectName("H4")
        self.gridLayout.addWidget(self.H4, 11, 4, 1, 1)
        self.H6 = QtWidgets.QPushButton(self.frame)
        self.H6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.H6.setText("")
        self.H6.setObjectName("H6")
        self.gridLayout.addWidget(self.H6, 11, 6, 1, 1)
        self.G8 = QtWidgets.QPushButton(self.frame)
        self.G8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.G8.setText("")
        self.G8.setObjectName("G8")
        self.gridLayout.addWidget(self.G8, 10, 9, 1, 1)
        self.H7 = QtWidgets.QPushButton(self.frame)
        self.H7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.H7.setText("")
        self.H7.setObjectName("H7")
        self.gridLayout.addWidget(self.H7, 11, 8, 1, 1)
        self.number3 = QtWidgets.QLabel(self.frame)
        self.number3.setObjectName("number3")
        self.gridLayout.addWidget(self.number3, 0, 3, 1, 1)
        self.H5 = QtWidgets.QPushButton(self.frame)
        self.H5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.H5.setText("")
        self.H5.setObjectName("H5")
        self.gridLayout.addWidget(self.H5, 11, 5, 1, 1)
        self.H8 = QtWidgets.QPushButton(self.frame)
        self.H8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.H8.setText("")
        self.H8.setObjectName("H8")
        self.gridLayout.addWidget(self.H8, 11, 9, 1, 1)
        self.B4 = QtWidgets.QPushButton(self.frame)
        self.B4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.B4.setText("")
        self.B4.setObjectName("B4")
        self.gridLayout.addWidget(self.B4, 3, 4, 1, 1)
        self.B2 = QtWidgets.QPushButton(self.frame)
        self.B2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.B2.setText("")
        self.B2.setObjectName("B2")
        self.gridLayout.addWidget(self.B2, 3, 2, 1, 1)
        self.B8 = QtWidgets.QPushButton(self.frame)
        self.B8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.B8.setText("")
        self.B8.setObjectName("B8")
        self.gridLayout.addWidget(self.B8, 3, 9, 1, 1)
        self.A8 = QtWidgets.QPushButton(self.frame)
        self.A8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.A8.setText("")
        self.A8.setObjectName("A8")
        self.gridLayout.addWidget(self.A8, 1, 9, 1, 1)
        self.A3 = QtWidgets.QPushButton(self.frame)
        self.A3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.A3.setText("")
        self.A3.setObjectName("A3")
        self.gridLayout.addWidget(self.A3, 1, 3, 1, 1)
        self.A7 = QtWidgets.QPushButton(self.frame)
        self.A7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.A7.setText("")
        self.A7.setObjectName("A7")
        self.gridLayout.addWidget(self.A7, 1, 8, 1, 1)
        self.A4 = QtWidgets.QPushButton(self.frame)
        self.A4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.A4.setText("")
        self.A4.setObjectName("A4")
        self.gridLayout.addWidget(self.A4, 1, 4, 1, 1)
        self.B1 = QtWidgets.QPushButton(self.frame)
        self.B1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.B1.setText("")
        self.B1.setObjectName("B1")
        self.gridLayout.addWidget(self.B1, 3, 1, 1, 1)
        self.A6 = QtWidgets.QPushButton(self.frame)
        self.A6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.A6.setText("")
        self.A6.setObjectName("A6")
        self.gridLayout.addWidget(self.A6, 1, 6, 1, 1)
        self.A5 = QtWidgets.QPushButton(self.frame)
        self.A5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.A5.setText("")
        self.A5.setObjectName("A5")
        self.gridLayout.addWidget(self.A5, 1, 5, 1, 1)
        self.A1 = QtWidgets.QPushButton(self.frame)
        self.A1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.gridLayout.addWidget(self.A1, 1, 1, 1, 1)
        self.F2 = QtWidgets.QPushButton(self.frame)
        self.F2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.F2.setText("")
        self.F2.setObjectName("F2")
        self.gridLayout.addWidget(self.F2, 9, 2, 1, 1)
        self.B3 = QtWidgets.QPushButton(self.frame)
        self.B3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.B3.setText("")
        self.B3.setObjectName("B3")
        self.gridLayout.addWidget(self.B3, 3, 3, 1, 1)
        self.E5 = QtWidgets.QPushButton(self.frame)
        self.E5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E5.setText("")
        self.E5.setObjectName("E5")
        self.gridLayout.addWidget(self.E5, 8, 5, 1, 1)
        self.F6 = QtWidgets.QPushButton(self.frame)
        self.F6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.F6.setText("")
        self.F6.setObjectName("F6")
        self.gridLayout.addWidget(self.F6, 9, 6, 1, 1)
        self.E3 = QtWidgets.QPushButton(self.frame)
        self.E3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E3.setText("")
        self.E3.setObjectName("E3")
        self.gridLayout.addWidget(self.E3, 8, 3, 1, 1)
        self.E4 = QtWidgets.QPushButton(self.frame)
        self.E4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E4.setText("")
        self.E4.setObjectName("E4")
        self.gridLayout.addWidget(self.E4, 8, 4, 1, 1)
        self.F1 = QtWidgets.QPushButton(self.frame)
        self.F1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.F1.setText("")
        self.F1.setObjectName("F1")
        self.gridLayout.addWidget(self.F1, 9, 1, 1, 1)
        self.G1 = QtWidgets.QPushButton(self.frame)
        self.G1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.G1.setText("")
        self.G1.setObjectName("G1")
        self.gridLayout.addWidget(self.G1, 10, 1, 1, 1)
        self.F8 = QtWidgets.QPushButton(self.frame)
        self.F8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.F8.setText("")
        self.F8.setObjectName("F8")
        self.gridLayout.addWidget(self.F8, 9, 9, 1, 1)
        self.G6 = QtWidgets.QPushButton(self.frame)
        self.G6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.G6.setText("")
        self.G6.setObjectName("G6")
        self.gridLayout.addWidget(self.G6, 10, 6, 1, 1)
        self.G7 = QtWidgets.QPushButton(self.frame)
        self.G7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.G7.setText("")
        self.G7.setObjectName("G7")
        self.gridLayout.addWidget(self.G7, 10, 8, 1, 1)
        self.F4 = QtWidgets.QPushButton(self.frame)
        self.F4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.F4.setText("")
        self.F4.setObjectName("F4")
        self.gridLayout.addWidget(self.F4, 9, 4, 1, 1)
        self.E1 = QtWidgets.QPushButton(self.frame)
        self.E1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.E1.setText("")
        self.E1.setObjectName("E1")
        self.gridLayout.addWidget(self.E1, 8, 1, 1, 1)
        self.F5 = QtWidgets.QPushButton(self.frame)
        self.F5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.F5.setText("")
        self.F5.setObjectName("F5")
        self.gridLayout.addWidget(self.F5, 9, 5, 1, 1)
        self.E7 = QtWidgets.QPushButton(self.frame)
        self.E7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E7.setText("")
        self.E7.setObjectName("E7")
        self.gridLayout.addWidget(self.E7, 8, 8, 1, 1)
        self.F3 = QtWidgets.QPushButton(self.frame)
        self.F3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.F3.setText("")
        self.F3.setObjectName("F3")
        self.gridLayout.addWidget(self.F3, 9, 3, 1, 1)
        self.E6 = QtWidgets.QPushButton(self.frame)
        self.E6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E6.setText("")
        self.E6.setObjectName("E6")
        self.gridLayout.addWidget(self.E6, 8, 6, 1, 1)
        self.G2 = QtWidgets.QPushButton(self.frame)
        self.G2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.G2.setText("")
        self.G2.setObjectName("G2")
        self.gridLayout.addWidget(self.G2, 10, 2, 1, 1)
        self.G3 = QtWidgets.QPushButton(self.frame)
        self.G3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.G3.setText("")
        self.G3.setObjectName("G3")
        self.gridLayout.addWidget(self.G3, 10, 3, 1, 1)
        self.F7 = QtWidgets.QPushButton(self.frame)
        self.F7.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.F7.setText("")
        self.F7.setObjectName("F7")
        self.gridLayout.addWidget(self.F7, 9, 8, 1, 1)
        self.G4 = QtWidgets.QPushButton(self.frame)
        self.G4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.G4.setText("")
        self.G4.setObjectName("G4")
        self.gridLayout.addWidget(self.G4, 10, 4, 1, 1)
        self.G5 = QtWidgets.QPushButton(self.frame)
        self.G5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.G5.setText("")
        self.G5.setObjectName("G5")
        self.gridLayout.addWidget(self.G5, 10, 5, 1, 1)
        self.E2 = QtWidgets.QPushButton(self.frame)
        self.E2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E2.setText("")
        self.E2.setObjectName("E2")
        self.gridLayout.addWidget(self.E2, 8, 2, 1, 1)
        self.E8 = QtWidgets.QPushButton(self.frame)
        self.E8.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.E8.setText("")
        self.E8.setObjectName("E8")
        self.gridLayout.addWidget(self.E8, 8, 9, 1, 1)
        self.H1 = QtWidgets.QPushButton(self.frame)
        self.H1.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.H1.setText("")
        self.H1.setObjectName("H1")
        self.gridLayout.addWidget(self.H1, 11, 1, 1, 1)
        self.H2 = QtWidgets.QPushButton(self.frame)
        self.H2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.H2.setText("")
        self.H2.setObjectName("H2")
        self.gridLayout.addWidget(self.H2, 11, 2, 1, 1)
        self.H3 = QtWidgets.QPushButton(self.frame)
        self.H3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}\n"
"")
        self.H3.setText("")
        self.H3.setObjectName("H3")
        self.gridLayout.addWidget(self.H3, 11, 3, 1, 1)
        self.B6 = QtWidgets.QPushButton(self.frame)
        self.B6.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0); /* Красный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста для контраста */\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 0, 0); /* Темно-красный цвет при нажатии */\n"
"}")
        self.B6.setText("")
        self.B6.setObjectName("B6")
        self.gridLayout.addWidget(self.B6, 3, 6, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buyButton.setText(_translate("Dialog", "Buy"))
        self.headerText.setText(_translate("Dialog", "SEATS"))
        self.number4.setText(_translate("Dialog", "4"))
        self.number2.setText(_translate("Dialog", "2"))
        self.number1.setText(_translate("Dialog", "1"))
        self.number5.setText(_translate("Dialog", "5"))
        self.number8.setText(_translate("Dialog", "8"))
        self.letterH.setText(_translate("Dialog", "H"))
        self.number6.setText(_translate("Dialog", "6"))
        self.number7.setText(_translate("Dialog", "7"))
        self.letterC.setText(_translate("Dialog", "C"))
        self.letterF.setText(_translate("Dialog", "F"))
        self.letterB.setText(_translate("Dialog", "B"))
        self.letterA.setText(_translate("Dialog", "A"))
        self.letterE.setText(_translate("Dialog", "E"))
        self.letterD.setText(_translate("Dialog", "D"))
        self.letterG.setText(_translate("Dialog", "G"))
        self.number3.setText(_translate("Dialog", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
