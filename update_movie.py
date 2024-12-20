# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_movie.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class updateMoviePage(object):
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deleteButton)
        self.addButton_2 = QtWidgets.QPushButton(Dialog)
        self.addButton_2.setGeometry(QtCore.QRect(230, 630, 101, 38))
        self.addButton_2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: #dda15e; /* Лаймово-зелёный цвет */\n"
"    color: rgb(255, 255, 255); /* Белый цвет текста */\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #bc6c25; /* Тёмно-зелёный цвет при нажатии */\n"
"}\n"
"\n"
"")
        self.addButton_2.setObjectName("addButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "UPDATE MOVIE"))
        self.fILMLabel.setText(_translate("Dialog", "FILM:"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.filmDel.setText(_translate("Dialog", "FILM:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Moana2"))
        self.comboBox.setItemText(1, _translate("Dialog", "Venom3"))
        self.comboBox.setItemText(2, _translate("Dialog", "Evil"))
        self.comboBox.setItemText(3, _translate("Dialog", "Gladiator2"))
        self.comboBox.setItemText(4, _translate("Dialog", "Home alone"))
        self.comboBox.setItemText(5, _translate("Dialog", "Home alone2"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.addButton_2.setText(_translate("Dialog", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = updateMoviePage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
