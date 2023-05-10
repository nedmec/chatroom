import sys
from PyQt5.QtWidgets import QApplication
from chat_window import ChatWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    sys.exit(app.exec_())
