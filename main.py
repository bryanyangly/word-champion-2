import levels_loader
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from ui_word_champion_lobby import Ui_MainWindow as Ui_LobbyWindow
from ui_word_champion_game import Ui_MainWindow as Ui_GameWindow
from ui_word_champion_result import Ui_MainWindow as Ui_ResultWindow

# Constants
DATA_ROOT_DIR = "input"

class LobbyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LobbyWindow()
        self.ui.setupUi(self)

        levels = level_data['level'].unique()
        for level in levels:
            image_count = len(level_data[level_data['level'] == level])
            display_text = f"{level} ({image_count} images)"
            self.ui.comboBox_levels.addItem(display_text)

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)
        self.level = None

    def show_with_level(self, level):
        self.level = level
        self.setWindowTitle(f"Word Champion Game - {level}")
        self.show()

class ResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self)

    def show_with_level(self, level):
        self.ui.label_level.setText(f"Level: {level}")
        self.show()

def main():
    global level_data
    app = QApplication(sys.argv)

    try:
        level_data = levels_loader.try_load(DATA_ROOT_DIR)
    except levels_loader.LevelLoadingError as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Error loading levels: " + str(e))
        msg.setWindowTitle("Error")
        msg.exec()
        sys.exit(1)

    lobby_window = LobbyWindow()
    game_window = GameWindow()
    result_window = ResultWindow()

    lobby_window.ui.pushButton.clicked.connect(lambda: (
        selected_level := lobby_window.ui.comboBox_levels.currentText(),
        lobby_window.hide(),
        game_window.show_with_level(selected_level)
    ))
    game_window.ui.pushButton_abort.clicked.connect(lambda: (game_window.hide(), result_window.show_with_level(game_window.level)))
    result_window.ui.pushButton_tolobby.clicked.connect(lambda: result_window.hide() or lobby_window.show())

    lobby_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
