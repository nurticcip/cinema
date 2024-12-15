import sys
import random
import string
import requests  # For sending HTTP requests
from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QCheckBox, QWidget, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up with CAPTCHA")
        self.captcha_text = self.generate_captcha()

        # CAPTCHA Label
        self.captcha_label = QLabel(self)
        self.captcha_label.setPixmap(self.generate_captcha_image(self.captcha_text))

        # CAPTCHA Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter CAPTCHA here")

        # CAPTCHA Checkbox
        self.captcha_checkbox = QCheckBox("I am not a robot", self)

        # Submit Button
        self.submit_button = QPushButton("Sign Up", self)
        self.submit_button.clicked.connect(self.validate_signup)

        # Layout Setup
        layout = QVBoxLayout()
        layout.addWidget(self.captcha_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.captcha_checkbox)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def generate_captcha(self):
        """Generate a random CAPTCHA string."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def generate_captcha_image(self, text):
        """Create a CAPTCHA image from text."""
        image = QImage(200, 50, QImage.Format_RGB32)
        image.fill(QColor("white"))

        painter = QPainter(image)
        painter.setFont(QFont("Arial", 20))
        painter.setPen(QColor("black"))

        # Randomly distort the text
        for i, char in enumerate(text):
            x = 30 + i * 25
            y = random.randint(20, 40)
            painter.drawText(x, y, char)

        painter.end()

        return QPixmap.fromImage(image)

    def validate_signup(self):
        """Validate CAPTCHA and send to server."""
        user_input = self.input_field.text().strip()
        checkbox_checked = self.captcha_checkbox.isChecked()

        if not checkbox_checked:
            QMessageBox.warning(self, "Error", "Please confirm the checkbox to prove you're not a robot.")
            return

        # Send CAPTCHA and checkbox status to the server
        response = requests.post(
            "http://nurticcip.pythonanywhere.com/check_captcha",  # Replace with your server URL
            json={"captcha_text": self.captcha_text, "user_input": user_input}
        )

        if response.status_code == 200:
            result = response.json()
            if result.get("success"):
                QMessageBox.information(self, "Success", "CAPTCHA validated successfully!")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Invalid CAPTCHA. Please try again.")
                # Regenerate CAPTCHA
                self.captcha_text = self.generate_captcha()
                self.captcha_label.setPixmap(self.generate_captcha_image(self.captcha_text))
                self.input_field.clear()
        else:
            QMessageBox.critical(self, "Error", "Server error. Please try again later.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignUpWindow()
    window.show()
    sys.exit(app.exec_())
