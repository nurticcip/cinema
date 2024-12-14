from PyQt5 import QtCore, QtGui, QtWidgets

class SeatGenerator(QtWidgets.QWidget):
    def __init__(self, time, movie):
        super().__init__()  # Properly initialize the parent class
        self.time = time
        self.movie = movie
        self.seats_now = []
        self.setupUi()

    def setupUi(self):
        # Set up the main window
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle('Hall')

        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()

        # Add screen label below the seats
        screen_label = QtWidgets.QLabel('SCREEN')
        screen_label.setAlignment(QtCore.Qt.AlignCenter)
        screen_label.setStyleSheet("font-size: 20px; font-weight: bold; color: white; background-color: black; padding: 10px;")

        # Create a grid layout for the seats
        seat_layout = QtWidgets.QGridLayout()
        seat_layout.setSpacing(10)

        # Define rows (A-G) and columns (1-10)
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        columns = range(1, 11)

        for row_idx, row in enumerate(rows):
            for col_idx, col in enumerate(columns):
                # Create a button for each seat
                seat_button = QtWidgets.QPushButton(f"{row}{col}")
                seat_button.setFixedSize(50, 50)
                seat_button.setStyleSheet("background-color: lightgray; border: 1px solid black;")

                # Connect button to a method for selection (optional, to be implemented)
                seat_button.clicked.connect(lambda _, r=row, c=col: self.selectSeat(r, c))

                # Add the button to the grid layout
                seat_layout.addWidget(seat_button, row_idx, col_idx)

        # Add the seat layout and screen label to the main layout
        main_layout.addLayout(seat_layout)
        main_layout.addWidget(screen_label)

        # Set the main layout
        self.setLayout(main_layout)

    def selectSeat(self, row, col):
        seat = f"{row}{col}"
        if seat in self.seats_now:
            self.seats_now.remove(seat)
            print(f"Deselected seat: {seat}")
        else:
            self.seats_now.append(seat)
            print(f"Selected seat: {seat}")

# Example usage (Uncomment below lines to test)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SeatGenerator("17:40", "Avatar")
    window.show()
    sys.exit(app.exec_())
