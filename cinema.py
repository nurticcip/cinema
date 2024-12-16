from PyQt5.QtWidgets import (
    QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit,
    QMessageBox, QGridLayout, QDateEdit, QTimeEdit, QListWidget, QInputDialog
)
from PyQt5.QtCore import Qt
import sys
import random
from datetime import datetime

# Симулированная база данных
users_db = {"user": "password"}
movies = []  # Список для хранения данных о фильмах
user_history = []  # История просмотров пользователя
ticket_sales = {}  # Трекинг продаж билетов и дохода по каждому фильму
seat_status = {}  # Статус бронирования мест для каждого фильма

# Генерация случайного кода капчи
def generate_captcha():
    return str(random.randint(1000, 9999))

current_captcha = generate_captcha()


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.logged_in_user = None  # Для хранения имени вошедшего пользователя
        self.setWindowTitle("Login")
        self.resize(430, 300)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")

        self.label_title = QLabel("<span style='font-size:12pt; font-weight:600;'>FILMBOX</span>")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet("color: rgb(170, 4, 29);")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.captcha_label = QLabel(f"Captcha: {current_captcha}")
        self.captcha_input = QLineEdit()
        self.captcha_input.setPlaceholderText("Enter captcha")

        self.login_button = QPushButton("LOGIN")
        self.login_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.login_button.clicked.connect(self.login_action)

        self.register_button = QPushButton("REGISTER")
        self.register_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.register_button.clicked.connect(self.open_register)

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.captcha_label)
        layout.addWidget(self.captcha_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def login_action(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        entered_captcha = self.captcha_input.text().strip()

        if username in users_db and users_db[username] == password and entered_captcha == current_captcha:
            self.logged_in_user = username  # Сохранение имени пользователя
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid username, password, or captcha.")

    def open_register(self):
        register_dialog = RegisterDialog()
        if register_dialog.exec_() == QDialog.Accepted:
            self.accept()


class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.resize(430, 350)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")

        self.label_title = QLabel("<span style='font-size:12pt; font-weight:600;'>REGISTER</span>")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet("color: rgb(170, 4, 29);")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm your password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.captcha_label = QLabel(f"Captcha: {current_captcha}")
        self.captcha_input = QLineEdit()
        self.captcha_input.setPlaceholderText("Enter captcha")

        self.register_button = QPushButton("REGISTER")
        self.register_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.register_button.clicked.connect(self.register_action)

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.captcha_label)
        layout.addWidget(self.captcha_input)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def register_action(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        confirm_password = self.confirm_password_input.text().strip()
        entered_captcha = self.captcha_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Username and password cannot be empty.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        if entered_captcha != current_captcha:
            QMessageBox.warning(self, "Error", "Captcha is incorrect.")
            return

        if username in users_db:
            QMessageBox.warning(self, "Error", "Username already exists.")
            return

        users_db[username] = password
        QMessageBox.information(self, "Success", "User registered successfully.")
        self.accept()

class MovieDisplay(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movies and Sessions")
        self.resize(500, 600)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.username = "username"

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.label_title = QLabel("<span style='font-size:12pt; font-weight:600; color:rgb(170,4,29);'>FILMBOX</span>")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_title)

        self.movies_layout = QVBoxLayout()
        self.main_layout.addLayout(self.movies_layout)

        self.manage_button = QPushButton("Manage Movies")
        self.manage_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.manage_button.clicked.connect(self.open_movie_manager)
        self.main_layout.addWidget(self.manage_button)

        self.info_button = QPushButton("Info Movies")
        self.info_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.info_button.clicked.connect(self.show_movie_info)
        self.main_layout.addWidget(self.info_button)

        self.history_button = QPushButton("User History")
        self.history_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.history_button.clicked.connect(self.show_user_history)
        self.main_layout.addWidget(self.history_button)

        self.update_movie_list()

    def update_movie_list(self):
        """Обновление списка фильмов в интерфейсе."""
        # Очистить старые элементы в списке
        for i in reversed(range(self.movies_layout.count())):
            widget = self.movies_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Добавить фильмы в интерфейс, но избегая дублирования
        added_movies = set()  # Множество для отслеживания уже добавленных фильмов
        for movie in movies:
            if movie not in added_movies:  # Проверка, чтобы избежать добавления дубликатов
                movie_label = QLabel(movie)
                movie_button = QPushButton("Buy")
                movie_button.setStyleSheet("background-color: rgb(109, 156, 156); color: black;")

                movie_button.clicked.connect(lambda _, m=movie: self.buy_ticket(m))

                layout = QHBoxLayout()
                layout.addWidget(movie_label)
                layout.addWidget(movie_button)
                self.movies_layout.addLayout(layout)
                added_movies.add(movie)  # Добавляем в множество для предотвращения дублирования

    def open_movie_manager(self):
        movie_manager = MovieManager(self.update_movie_list)
        movie_manager.exec_()

    def show_movie_info(self):
        info_dialog = MovieInfoDialog()
        info_dialog.exec_()

    def show_user_history(self):
        history_dialog = UserHistoryDialog()
        history_dialog.exec_()

    def buy_ticket(self, movie):
        buy_dialog = BuyTicketDialog(movie, self.username)
        buy_dialog.exec_()




class MovieManager(QDialog):
    def __init__(self, update_movie_list_callback):
        super().__init__()
        self.setWindowTitle("Manage Movies")
        self.resize(500, 600)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Отображение текущих фильмов
        self.movies_list = QListWidget()
        self.layout.addWidget(self.movies_list)
        self.update_movies_list()

        # Поля ввода для добавления фильма
        self.movie_name_input = QLineEdit()
        self.movie_name_input.setPlaceholderText("Movie name")
        self.layout.addWidget(self.movie_name_input)

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Price per ticket")
        self.layout.addWidget(self.price_input)

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(datetime.now())
        self.layout.addWidget(self.date_input)

        self.time_input = QTimeEdit()
        self.time_input.setTime(datetime.now().time())
        self.layout.addWidget(self.time_input)

        # Кнопка добавления фильма
        self.add_button = QPushButton("Add Movie")
        self.add_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.add_button.clicked.connect(self.add_movie)
        self.layout.addWidget(self.add_button)

        # Поле ввода для удаления фильма
        self.remove_movie_input = QLineEdit()
        self.remove_movie_input.setPlaceholderText("Movie to remove (partial search supported)")
        self.layout.addWidget(self.remove_movie_input)

        # Кнопка удаления фильма
        self.remove_button = QPushButton("Remove Movie")
        self.remove_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.remove_button.clicked.connect(self.remove_movie)
        self.layout.addWidget(self.remove_button)

        # Кнопка редактирования фильма
        self.edit_button = QPushButton("Edit Selected Movie")
        self.edit_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.edit_button.clicked.connect(self.edit_movie)
        self.layout.addWidget(self.edit_button)

        self.update_movie_list_callback = update_movie_list_callback

    def update_movies_list(self):
        """Обновление списка фильмов в интерфейсе."""
        self.movies_list.clear()
        for movie in movies:
            self.movies_list.addItem(movie)

    def add_movie(self):
        """Добавление нового фильма."""
        name = self.movie_name_input.text().strip()
        price = self.price_input.text().strip()
        date = self.date_input.date().toString("dd/MM/yyyy")
        time = self.time_input.time().toString("hh:mm")
        movie_key = f"{name} - {date} {time}"

        # Проверка на уникальность
        if not name or not price.isdigit() or int(price) <= 0:
            QMessageBox.warning(self, "Error", "Please enter a valid movie name and a positive price.")
            return

        if movie_key in movies:
            QMessageBox.warning(self, "Error", "Movie with the same details already exists.")
            return

        # Добавление фильма
        movies.append(movie_key)
        ticket_sales[movie_key] = {"sold": 0, "income": 0, "price": int(price)}
        seat_status[movie_key] = {f"{row}{col}": False for row in "ABCDEF" for col in range(1, 10)}

        QMessageBox.information(self, "Success", "Movie added successfully!")
        self.update_movies_list()
        self.update_movie_list_callback()

    def remove_movie(self):
        """Удаление фильма с подтверждением."""
        search_term = self.remove_movie_input.text().strip().lower()

        if not search_term:
            QMessageBox.warning(self, "Error", "Please enter a movie name to remove.")
            return

        # Поиск фильмов по ключевому слову
        matching_movies = [movie for movie in movies if search_term in movie.lower()]

        if not matching_movies:
            QMessageBox.warning(self, "Error", "No matching movies found.")
            return

        # Выбор фильма для удаления
        movie_to_remove, ok = QInputDialog.getItem(self, "Remove Movie", "Select a movie to remove:", matching_movies, 0, False)

        if ok and movie_to_remove:
            movies.remove(movie_to_remove)
            ticket_sales.pop(movie_to_remove, None)
            seat_status.pop(movie_to_remove, None)
            QMessageBox.information(self, "Success", "Movie removed successfully!")
            self.update_movies_list()
            self.update_movie_list_callback()

    def edit_movie(self):
        """Редактирование фильма."""
        selected_movie_item = self.movies_list.currentItem()

        if not selected_movie_item:
            QMessageBox.warning(self, "Error", "Please select a movie to edit.")
            return

        movie_to_edit = selected_movie_item.text()
        current_price = ticket_sales[movie_to_edit]["price"]

        # Редактирование цены
        new_price, ok = QInputDialog.getInt(self, "Edit Movie", f"Current price: {current_price}. Enter new price:", current_price, 1)

        if ok:
            ticket_sales[movie_to_edit]["price"] = new_price
            QMessageBox.information(self, "Success", "Movie updated successfully!")
            self.update_movies_list()
            self.update_movie_list_callback()


class MovieInfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movies Info")
        self.resize(400, 500)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")

        layout = QVBoxLayout()

        total_income = 0
        for movie, data in ticket_sales.items():
            info_label = QLabel(f"{movie}\nTickets Sold: {data['sold']}\nIncome: ${data['income']}\nPrice: ${data['price']}")
            layout.addWidget(info_label)
            total_income += data['income']

        total_label = QLabel(f"Total Income: ${total_income}")
        layout.addWidget(total_label)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")

        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)

class UserHistoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User History")
        self.resize(400, 500)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")

        layout = QVBoxLayout()

        if user_history:
            for entry in user_history:
                history_label = QLabel(entry)
                layout.addWidget(history_label)
        else:
            layout.addWidget(QLabel("No history found."))

        back_button = QPushButton("Back")
        back_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")

        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)


class BuyTicketDialog(QDialog):
    def __init__(self, movie, username, parent=None):
        super().__init__(parent)
        self.movie = movie
        self.username = username  # Сохранение имени пользователя
        self.setWindowTitle(f"Buy Ticket - {movie}")
        self.resize(400, 500)
        self.setStyleSheet("background-color: rgb(159, 159, 159);")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.seat_grid = QGridLayout()
        self.layout.addLayout(self.seat_grid)

        self.selected_seats = []

        # Добавление кнопок для мест
        for row in "ABCDEF":
            for col in range(1, 10):
                seat_id = f"{row}{col}"
                seat_button = QPushButton(seat_id)
                if seat_status[self.movie].get(seat_id):  # Seat is taken
                    seat_button.setStyleSheet("background-color: red;")
                else:
                    seat_button.setStyleSheet("background-color: lightgreen;")
                seat_button.clicked.connect(self.select_seat)
                self.seat_grid.addWidget(seat_button, ord(row) - ord('A'), col - 1)

        self.buy_button = QPushButton("Buy Ticket")
        self.buy_button.setStyleSheet("background-color: rgb(70, 117, 122); color: black;")
        self.buy_button.clicked.connect(self.buy_ticket)
        self.layout.addWidget(self.buy_button)

    def select_seat(self):
        button = self.sender()
        seat_id = button.text()

        if seat_status[self.movie].get(seat_id):  # Seat already taken
            QMessageBox.warning(self, "Seat Taken", f"Seat {seat_id} is already taken.")
        elif seat_id in self.selected_seats:  # Seat already selected
            self.selected_seats.remove(seat_id)
            button.setStyleSheet("background-color: lightgreen;")  # Return to green
        else:  # Seat is free and not selected
            self.selected_seats.append(seat_id)
            button.setStyleSheet("background-color: yellow;")  # Selected, yellow

    def buy_ticket(self):
        if self.selected_seats:
            total_price = len(self.selected_seats) * ticket_sales[self.movie]["price"]
            # Включаем имя пользователя в историю покупок
            user_history.append(f"{self.username} bought {len(self.selected_seats)} tickets for {self.movie} ({', '.join(self.selected_seats)})")
            ticket_sales[self.movie]["sold"] += len(self.selected_seats)
            ticket_sales[self.movie]["income"] += total_price

            # Обновляем статус мест на "занято"
            for seat in self.selected_seats:
                seat_status[self.movie][seat] = True

            self.update_seat_buttons()

            QMessageBox.information(self, "Success", f"Ticket(s) bought for {total_price} KGZ!")
            self.close()
        else:
            QMessageBox.warning(self, "No Seats", "Please select seats to buy.")

    def update_seat_buttons(self):
        """Обновление кнопок мест после покупки."""
        for row in "ABCDEF":
            for col in range(1, 10):
                seat_id = f"{row}{col}"
                button = self.seat_grid.itemAtPosition(ord(row) - ord('A'), col - 1).widget()
                if seat_status[self.movie].get(seat_id):  # Seat is taken
                    button.setStyleSheet("background-color: red;")
                elif seat_id in self.selected_seats:  # Seat is selected
                    button.setStyleSheet("background-color: yellow;")
                else:  # Seat is free
                    button.setStyleSheet("background-color: lightgreen;")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        movie_display = MovieDisplay()
        movie_display.exec_()
    sys.exit(app.exec_())