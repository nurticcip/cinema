from PyQt5 import QtCore, QtGui, QtWidgets
import requests
selected = {'movie':'avatar','seance':'17:40'}

class SeatGenerator(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.seats_now = []
        self.price = requests.get('http://viollenaki.pythonanywhere.com/get_movie_price', params={'movie': selected["movie"]}).json()
        self.total = 0


    def setupUi(self):
        self.setGeometry(100, 100, 1000, 700)  
        self.setWindowTitle('Hall') 

        self.setStyleSheet("background-color: rgb(13, 44, 62);")
        
        self.buy = QtWidgets.QPushButton('Buy',self)
        self.buy.setGeometry(QtCore.QRect(390, 610, 226, 41))
        
        
        self.total_text = QtWidgets.QLabel(self)
        self.total_text.setGeometry(QtCore.QRect(670, 610, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        self.total_text.setFont(font)
        self.total_text.setStyleSheet("background-color: rgb(124, 166, 144);\n"
"border-radius: 20px;\n"
"")
        self.total_text.setObjectName("total_text")
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.buy.setFont(font)
        self.buy.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(124, 166, 144);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.buy.clicked.connect(self.buy_ticket)


        
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(453, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(561, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(615, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(507, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(291, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(238, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(399, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(723, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(884, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(831, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(669, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(777, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(13, 44, 62);\n")
        
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(76, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(130, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(184, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(346, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")



        
        self.label = QtWidgets.QLabel('Screen',self)
        self.label.setGeometry(QtCore.QRect(47, 27, 905, 28))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(197, 158, 81);\n"
"border-radius: 14px;")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Screen</span></p></body></html>"))

        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(952, 104, 39, 428))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(8, 104, 39, 428))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">A</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">B</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">C</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">D</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">E</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">F</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">G</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">H</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">I</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">J</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">A</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">B</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">C</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">D</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">E</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">F</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">G</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">H</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">I</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">J</span></p></body></html>"))
        
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">1</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">2</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">3</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">6</span></p></body></html>"))
        
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">8</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">10</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">11</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">9</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">5</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">4</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">7</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">13</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">16</span></p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">15</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">12</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">14</span></p></body></html>"))
        self.total_text.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">0$</p></body></html>"))





        # Создаем кнопки
        self.create_buttons()







    def create_buttons(self):
        booked_seats = requests.get('http://viollenaki.pythonanywhere.com/get_movie_booked_seats', 
                                params={'movie': selected["movie"], 'seance': selected["seance"]}).json()
        rows = 'abcdefghij' 
        cols = 16  
        x_start, y_start = 76, 104  
        button_width, button_height = 41, 30  
        x_gap, y_gap = 54, 44 

        for i, row in enumerate(rows):
            for col in range(1, cols + 1):
                seat_id = f'{row}{col}'  
                x = x_start + (col - 1) * x_gap
                y = y_start + i * y_gap
                button = QtWidgets.QPushButton(self)
                button.setGeometry(x, y, button_width, button_height)
                button.setFont(QtGui.QFont('Arial', 10))

                button.clicked.connect(self.make_button_click_handler(seat_id, button))

                if seat_id not in booked_seats:
                     button.setStyleSheet(self.get_button_styles_free())  # Style for free seats
                else:
                     button.setStyleSheet(self.get_button_styles_booked())  # Style for booked seats
                     button.setEnabled(False)  # Disable booked buttons

    def make_button_click_handler(self, seat_id, button):
        def handler():
            self.toggle_seat(seat_id, button)
        return handler

    def toggle_seat(self, seat_id, button):
        if seat_id in self.seats_now:
            self.seats_now.remove(seat_id) 
            self.total -= self.price
            self.total_text.setText(f"<html><head/><body><p align=\"center\">{self.total}$</p></body></html>")
            button.setStyleSheet(self.get_button_styles_free()) 
        else:
            self.seats_now.append(seat_id) 
            self.total += self.price
            self.total_text.setText(f"<html><head/><body><p align=\"center\">{self.total}$</p></body></html>")
            button.setStyleSheet(self.get_button_styles_selected()) 

    def get_button_styles_free(self):
        return ("QPushButton:hover{\n"
        "    background-color: rgb(23, 137, 143);\n"
        "    color: rgb(255, 255, 255);\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:rgb(14, 85, 89);\n"
        "    color: rgb(255, 255, 255);\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px\n"
        "}\n"
        "QPushButton{\n"
        "background-color: rgb(124, 166, 144);\n"
        "color: rgb(0, 0, 0);\n"
        "font-size: 30px;\n"
        "border-radius: 8px\n"
        "}\n"
        "")

    def get_button_styles_selected(self):
        return (
                "QPushButton:hover{\n"
                "background-color: #de0000;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 30px;\n"
                "    border-radius: 8px\n"
                "}\n"
                "QPushButton:pressed{\n"
                "background-color: #7f0000;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 30px;\n"
                "    border-radius: 8px\n"
                "}\n"
                "QPushButton{\n"
                "background-color: #ff5733;\n"
                "color: rgb(0, 0, 0);\n"
                "font-size: 30px;\n"
                "border-radius: 8px\n"
                "}\n"
                ""
        )

    def get_button_styles_booked(self):
        return ("\n"
        "QPushButton {\n"
        "    background-color:  rgb(61, 61, 61); /* Серый фон */\n"
        "    color: rgb(0, 0, 0); /* Черный текст */\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color:  rgb(61, 61, 61); /* Сохраняем серый фон при наведении */\n"
        "    color: rgb(0, 0, 0); /* Сохраняем черный цвет текста при наведении */\n"
        "}")

    def buy_ticket(self):
        args = ','.join(self.seats_now)
        requests.get('http://viollenaki.pythonanywhere.com/movie_seance_booking', params={'user': main_user, 'movie': selected['movie'], 'seance': selected['seance'], 'seats': args})
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SeatGenerator()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
