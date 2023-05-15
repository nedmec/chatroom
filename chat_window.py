import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit,
                             QPushButton, QLabel, QSizePolicy, QListWidget, QListWidgetItem)
from chat_api import get_ai_response
from chat_history import save_chat_history, load_chat_history
from my_chatbot_model import generate_response
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.current_friend = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle('聊天程序')
        self.resize(800, 600)

        main_layout = QHBoxLayout()

        # 好友列表
        self.friend_list = QListWidget()
        self.friend_list.itemClicked.connect(self.friend_selected)
        self.friend_list.setMinimumWidth(200)
        main_layout.addWidget(self.friend_list)

        # 聊天界面
        layout = QVBoxLayout()

        app_name_label = QLabel('Chat')
        app_name_label.setStyleSheet('font-size: 25px; font-weight: bold;')
        app_name_label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(app_name_label)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet('''
            background-color: #f0f0f0;
            font-size: 25px;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 5px;
            margin-bottom: 5px;
        ''')
        layout.addWidget(self.chat_area)

        self.message_input = QLineEdit()
        self.message_input.setStyleSheet('''
            font-size: 25px;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
            margin-bottom: 10px;
        ''')
        layout.addWidget(self.message_input)

        send_button = QPushButton('发送')
        send_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        send_button.setStyleSheet('''
            font-size: 25px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 5px 15px;
        ''')
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button, alignment=Qt.AlignRight)

        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        main_layout.addLayout(layout)
        self.setLayout(main_layout)

        self.add_friends(["机器人", "开放域", "好友"])

        self.show()

    def add_friends(self, friends):
        for friend in friends:
            item = QListWidgetItem(friend)
            self.friend_list.addItem(item)

    def friend_selected(self, item):
        self.current_friend = item.text()
        chat_history = load_chat_history(self.current_friend)
        self.chat_area.setPlainText("\n".join(chat_history))

    def send_message(self):
        if not self.current_friend:
            self.chat_area.append("请先从好友列表中选择一个聊天对象。")
            return

        message = self.message_input.text()
        self.chat_area.append(f"你: {message}")
        self.message_input.clear()

        if self.current_friend == "机器人":
            response = get_ai_response(message)
        if self.current_friend == "开放域":
            response = generate_response(message)
        # if self.current_friend == "好友":
        #      response = generate_response(message)

        
        self.chat_area.append(f"{self.current_friend}: {response}")

        chat_history = self.chat_area.toPlainText().split('\n')
        save_chat_history(self.current_friend, chat_history)
