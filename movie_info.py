# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 701)
        self.headerText = QtWidgets.QLabel(Dialog)
        self.headerText.setGeometry(QtCore.QRect(140, 20, 261, 51))
        self.headerText.setStyleSheet("color:black;\n"
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
        self.QuantityLabel = QtWidgets.QLabel(self.frame)
        self.QuantityLabel.setObjectName("QuantityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.QuantityLabel)
        self.QuantityTitle = QtWidgets.QLineEdit(self.frame)
        self.QuantityTitle.setObjectName("QuantityTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.QuantityTitle)
        self.seanseLabel = QtWidgets.QLabel(self.frame)
        self.seanseLabel.setObjectName("seanseLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.seanseLabel)
        self.seanseTitle = QtWidgets.QLineEdit(self.frame)
        self.seanseTitle.setObjectName("seanseTitle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.seanseTitle)
        self.peopleLabel = QtWidgets.QLabel(self.frame)
        self.peopleLabel.setObjectName("peopleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.peopleLabel)
        self.listUsers = QtWidgets.QListWidget(self.frame)
        self.listUsers.setObjectName("listUsers")
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.listUsers)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headerText.setText(_translate("Dialog", "MOVIE INFO"))
        self.filmText.setText(_translate("Dialog", "FILM:"))
        self.QuantityLabel.setText(_translate("Dialog", "QUANTITY:"))
        self.QuantityTitle.setText(_translate("Dialog", "1258"))
        self.seanseLabel.setText(_translate("Dialog", "SEANCE:"))
        self.seanseTitle.setText(_translate("Dialog", "6"))
        self.peopleLabel.setText(_translate("Dialog", "PEOPLE:"))
        __sortingEnabled = self.listUsers.isSortingEnabled()
        self.listUsers.setSortingEnabled(False)
        item = self.listUsers.item(0)
        item.setText(_translate("Dialog", "Nurti - 16:00"))
        item = self.listUsers.item(1)
        item.setText(_translate("Dialog", "Kutman - 17:30"))
        item = self.listUsers.item(2)
        item.setText(_translate("Dialog", "Jumu - 18:40"))
        item = self.listUsers.item(3)
        item.setText(_translate("Dialog", "Aiat - 20:10"))
        item = self.listUsers.item(4)
        item.setText(_translate("Dialog", "Adina - 22;15"))
        item = self.listUsers.item(5)
        item.setText(_translate("Dialog", "Sumay - 00:00"))
        item = self.listUsers.item(6)
        item.setText(_translate("Dialog", "Aktan - 00:30"))
        item = self.listUsers.item(7)
        item.setText(_translate("Dialog", "Adilet - 00:50"))
        item = self.listUsers.item(8)
        item.setText(_translate("Dialog", "Isma - 20:00"))
        item = self.listUsers.item(9)
        item.setText(_translate("Dialog", "Nurjigit - 20:00"))
        item = self.listUsers.item(10)
        item.setText(_translate("Dialog", "Atai - 19:50"))
        item = self.listUsers.item(11)
        item.setText(_translate("Dialog", "Omur - 15:45"))
        item = self.listUsers.item(12)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(13)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(14)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(15)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(16)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(17)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(18)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listUsers.item(19)
        item.setText(_translate("Dialog", "New Item"))
        self.listUsers.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("Dialog", "Moana2"))
        self.comboBox.setItemText(1, _translate("Dialog", "Venom3"))
        self.comboBox.setItemText(2, _translate("Dialog", "Evil"))
        self.comboBox.setItemText(3, _translate("Dialog", "Gladiator2"))
        self.comboBox.setItemText(4, _translate("Dialog", "Home alone"))
        self.comboBox.setItemText(5, _translate("Dialog", "Home alone2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
