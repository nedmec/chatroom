import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel, QSizePolicy
from chat_api import get_ai_response

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('聊天程序')
        self.resize(600, 400)

        layout = QVBoxLayout()

        app_name_label = QLabel('ChatGPT')
        app_name_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        app_name_label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(app_name_label)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet('''
            background-color: #f0f0f0;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
        ''')
        layout.addWidget(self.chat_area)

        self.message_input = QLineEdit()
        self.message_input.setStyleSheet('''
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
            margin-bottom: 10px;
        ''')
        layout.addWidget(self.message_input)

        send_button = QPushButton('发送')
        send_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        send_button.setStyleSheet('''
            font-size: 140px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 50px;
            padding: 50px 100px;
        ''')
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button, alignment=Qt.AlignRight)

        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

        self.show()

    def send_message(self):
        message = self.message_input.text()
        self.chat_area.append(f"你: {message}")
        self.message_input.clear()

        ai_response = get_ai_response(message)
        self.chat_area.append(f"AI: {ai_response}")
