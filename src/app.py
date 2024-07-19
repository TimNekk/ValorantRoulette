import sys
from PyQt5.QtWidgets import QApplication
import keyboard
from src.json_reader import JsonReader
from src.randomizer import Randomizer
from src.overlay.signal_handler import SignalHandler
from src.overlay.overlay_window import OverlayWindow


class Application:
    def __init__(self, settings_json_path: str) -> None:
        self._settings = JsonReader.get_settings(settings_json_path)
        self._randomizer = Randomizer(min_challenges=self._settings.min_challenges,
                                      max_challenges=self._settings.max_challenges)
        self._categories = JsonReader.get_categories(self._settings.challenges_json_path)

        self.app = QApplication(sys.argv)
        self.overlay = OverlayWindow(self)

        self.signal_handler = SignalHandler()
        self.signal_handler.refresh_signal.connect(self.get_new_challenges)
        self.signal_handler.toggle_visibility_signal.connect(self.toggle_visibility)
        self.signal_handler.close_signal.connect(self.close_application)

        keyboard.add_hotkey('f7', self.signal_handler.toggle_visibility_signal.emit)
        keyboard.add_hotkey('f8', self.signal_handler.refresh_signal.emit)
        keyboard.add_hotkey('f9', self.signal_handler.close_signal.emit)

        self.get_new_challenges()

    def toggle_visibility(self):
        if self.overlay.isVisible():
            self.overlay.hide()
        else:
            self.overlay.show()

    def get_new_challenges(self):
        challenges = self._randomizer.get_random_challenges(self._categories)
        self.overlay.update_challenges(challenges)

    def close_application(self):
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = Application("path/to/settings.json")
    app.run()
