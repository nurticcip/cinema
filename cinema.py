from PyQt5 import QtWidgets, QtGui, QtCore

class ExampleApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")

        coordinates = [
            76, 130, 184, 238, 291, 346, 399, 453, 507, 561, 615, 669, 723, 777, 831, 884
        ]
        
        for i, x in enumerate(coordinates, start=6):  # Start label names from 6
            label = QtWidgets.QLabel(self)
            label.setGeometry(QtCore.QRect(x, 550, 41, 30))
            label.setFont(font)
            if i != 21:  # Label 21 has a different style
                label.setStyleSheet("background-color: rgb(13, 44, 62); border-radius: 10px;")
            else:
                label.setStyleSheet("background-color: rgb(13, 44, 62);")
            label.setText(f"Label {i}")
            label.setAlignment(QtCore.Qt.AlignCenter)

        self.resize(1000, 600)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())
