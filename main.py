import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_word_champion_lobby import Ui_MainWindow as Ui_LobbyWindow
from ui_word_champion_game import Ui_MainWindow as Ui_GameWindow
from ui_word_champion_result import Ui_MainWindow as Ui_ResultWindow

class LobbyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LobbyWindow()
        self.ui.setupUi(self)

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)

class ResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)

    lobby_window = LobbyWindow()
    game_window = GameWindow()
    result_window = ResultWindow()

    lobby_window.ui.pushButton.clicked.connect(lambda: lobby_window.hide() or game_window.show())
    game_window.ui.pushButton_abort.clicked.connect(lambda: game_window.hide() or result_window.show())
    result_window.ui.pushButton_tolobby.clicked.connect(lambda: result_window.hide() or lobby_window.show())

    lobby_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
