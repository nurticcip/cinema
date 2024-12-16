import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QScrollArea
)
from PyQt5.QtCore import Qt


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieListApp()
    window.show()
    sys.exit(app.exec_())
