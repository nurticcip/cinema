import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout,
    QPushButton, QComboBox, QSpinBox, QWidget, QMessageBox
)

class CinemaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cinema Booking App")
        self.setGeometry(100, 100, 400, 300)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()

        # Movie selection
        self.movie_label = QLabel("Select a Movie:")
        self.layout.addWidget(self.movie_label)
        
        self.movie_combo = QComboBox()
        self.movie_combo.addItems(["Avatar: The Way of Water", "Inception", "The Matrix", "Avengers: Endgame"])
        self.layout.addWidget(self.movie_combo)

        # Showtime selection
        self.showtime_label = QLabel("Select Showtime:")
        self.layout.addWidget(self.showtime_label)

        self.showtime_combo = QComboBox()
        self.showtime_combo.addItems(["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"])
        self.layout.addWidget(self.showtime_combo)

        # Number of tickets
        self.ticket_label = QLabel("Number of Tickets:")
        self.layout.addWidget(self.ticket_label)

        self.ticket_spinbox = QSpinBox()
        self.ticket_spinbox.setRange(1, 10)
        self.layout.addWidget(self.ticket_spinbox)

        # Book button
        self.book_button = QPushButton("Book Tickets")
        self.book_button.clicked.connect(self.book_tickets)
        self.layout.addWidget(self.book_button)

        self.central_widget.setLayout(self.layout)

    def book_tickets(self):
        movie = self.movie_combo.currentText()
        showtime = self.showtime_combo.currentText()
        tickets = self.ticket_spinbox.value()

        QMessageBox.information(
            self,
            "Booking Confirmed",
            f"You have successfully booked {tickets} ticket(s) for '{movie}' at {showtime}. Enjoy the show!"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CinemaApp()
    window.show()
    sys.exit(app.exec_())