import levels_loader
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QTimer
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
            display_text = f"{level}"
            self.ui.comboBox_levels.addItem(display_text)

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)
        self.level = None
        self.countdown = 0
        self.time_used = 0
        self.passed_count = 0  # Initialize passed_count
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.ui.label_timeleft.setText("")

    def show_with_level(self, level, countdown):
        self.level = level
        self.countdown = countdown
        self.setWindowTitle(f"Word Champion Game - {level}")
        self.time_used = 0
        self.passed_count = 0 # Reset passed_count when a new game starts
        self.skipped_count = 0 # Reset skipped_count when a new game starts
        self.update_passed_count_label()
        self.update_skipped_count_label()
        self.timer.start(1000) # Update every 1 second
        self.show()

    def update_time(self):
        self.time_used += 1
        time_left = self.countdown - self.time_used
        self.ui.label_timeleft.setText(f"{time_left}")
        if self.time_used > self.countdown:
            self.timer.stop()
            self.hide()
            result_window.show_with_level(self.level, self.time_used, self.passed_count, self.skipped_count)

    def increment_passed_count(self):
        self.passed_count += 1
        self.update_passed_count_label()

    def update_passed_count_label(self):
        self.ui.label_passedcount.setText(str(self.passed_count))

    def increment_skipped_count(self):
        self.skipped_count += 1
        self.update_skipped_count_label()

    def update_skipped_count_label(self):
        self.ui.label_skippedcount.setText(str(self.skipped_count))

class ResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self)

    def show_with_level(self, level, time_used, passed_count, skipped_count):
        self.ui.label_level.setText(level)
        self.ui.label_timeused.setText(f"{time_used}")
        self.ui.label_passedcount.setText(str(passed_count))
        self.ui.label_skippedcount.setText(str(skipped_count))
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

    global result_window
    lobby_window = LobbyWindow()
    game_window = GameWindow()
    result_window = ResultWindow()

    lobby_window.ui.pushButton.clicked.connect(lambda: (
        selected_level := lobby_window.ui.comboBox_levels.currentText(),
        countdown := lobby_window.ui.spinBox.value(),
        lobby_window.hide(),
        game_window.show_with_level(selected_level, countdown)
    ))
    game_window.ui.pushButton_abort.clicked.connect(lambda: (game_window.hide(), result_window.show_with_level(game_window.level, game_window.time_used, game_window.passed_count, game_window.skipped_count)))
    game_window.ui.pushButton_pass.clicked.connect(game_window.increment_passed_count)
    game_window.ui.pushButton_skip.clicked.connect(game_window.increment_skipped_count)
    result_window.ui.pushButton_tolobby.clicked.connect(lambda: result_window.hide() or lobby_window.show())

    lobby_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
