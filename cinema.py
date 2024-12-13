from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QScrollArea,
    QWidget, QPushButton, QLabel, QMainWindow
)
from PyQt5.QtCore import Qt
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieListApp()
    window.show()
    sys.exit(app.exec_())
