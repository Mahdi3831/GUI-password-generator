from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
import sys
numbers = "1234567890"
chara = "abcdefghijklmnopqrstuwwxyz"
charb = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
sym = "@#&*.@#&*.@#&.*@#&*."

class window(QWidget):
    def __init__(self):
        global pass_difficulty_combo, char_num_lineedit, password_label, clipboard, password_copy
        QWidget.__init__(self)
        super().__init__()
        self.setWindowTitle("Random Password Generator")
        self.resize(600, 330)
        layout = QGridLayout()
        self.setLayout(layout)

        password_length_label = QLabel("Password length ")
        password_length_label.setStyleSheet("color: green")
        layout.addWidget(password_length_label, 0, 0)

        char_num_lineedit = QLineEdit()
        char_num_lineedit.setPlaceholderText("Password Length")
        layout.addWidget(char_num_lineedit, 0, 1)

        pass_difficulty_combo = QComboBox()
        pass_difficulty_combo.addItem("1")
        pass_difficulty_combo.addItem("2")
        pass_difficulty_combo.addItem("3")
        pass_difficulty_combo.addItem("4")
        layout.addWidget(pass_difficulty_combo, 1, 1)

        password_difficulty_label = QLabel("Password difficulty ")
        password_difficulty_label.setStyleSheet("color: green")
        layout.addWidget(password_difficulty_label, 1, 0)

        recommend_1 = QLabel("Recommend more than 8 characters")
        recommend_2 = QLabel("Recommend use level 3 or 4")
        recommend_1.setStyleSheet("color: red")
        recommend_2.setStyleSheet("color: red")
        layout.addWidget(recommend_1, 0, 2)
        layout.addWidget(recommend_2, 1, 2)

        generate_button = QPushButton("Generat")
        layout.addWidget(generate_button, 2, 0, 1, 4)
        generate_button.setStyleSheet("background-color: paleturquoise")
        generate_button.clicked.connect(self.passgenerate)

        password_label = QLabel("Nothing")
        layout.addWidget(password_label, 3, 1)

        your_password = QLabel("Your Password: ")
        your_password.setStyleSheet("color : darkred")
        layout.addWidget(your_password, 3, 0)
        clipboard = QApplication.clipboard()

        password_copy = QLabel("password will Copy to clipboard")
        layout.addWidget(password_copy, 3, 2)
        password_copy.setStyleSheet("color: tomato")

        delete_clipboard = QPushButton("Delete Clipboard")
        layout.addWidget(delete_clipboard, 4, 0)
        delete_clipboard.clicked.connect(self.delete)

    def passgenerate(self):
        length_value = int(char_num_lineedit.text())
        password  = ""

        difficulty_value = pass_difficulty_combo.currentText()
        if difficulty_value == "1":
            for x in range(0, length_value):
                password_char = random.choice(numbers)
                password      = password + password_char
                password_label.setText(password)
                clipboard.setText(password)
                password_copy.setText("Password copied to clipboard")

        if difficulty_value == "2":
            for x in range(0, length_value):
                password_char = random.choice(numbers + chara)
                password      = password + password_char
                password_label.setText(password)
                clipboard.setText(password)
                password_copy.setText("Password copied to clipboard")

        if difficulty_value == "3":
            for x in range(0, length_value):
                password_char = random.choice(numbers + chara + charb)
                password      = password + password_char
                password_label.setText(password)
                clipboard.setText(password)
                password_copy.setText("Password copied to clipboard")

        if difficulty_value == "4":
            for x in range(0, length_value):
                password_char = random.choice(numbers + chara + charb + sym)
                password      = password + password_char
                password_label.setText(password)
                clipboard.setText(password)
                password_copy.setText("Password copied to clipboard")

    def delete(self):
        clipboard.setText("/")

app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
