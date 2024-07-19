from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter
from src.overlay.challenge_widget import ChallengeWidget


class OverlayWindow(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color: rgba(0, 0, 0, 180);")

        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        main_layout.addWidget(self.scroll_area)

        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet("background-color: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setSpacing(5)
        self.scroll_area.setWidget(self.scroll_content)

        self.hotkey_hint = QLabel("Valorant Roulette | F7: Показать/скрыть | F8: Обновить | F9: Закрыть")
        self.hotkey_hint.setStyleSheet("color: darkgray; font-size: 12px; background-color: transparent;")
        self.hotkey_hint.setAlignment(Qt.AlignCenter)
        self.scroll_layout.addWidget(self.hotkey_hint)

        screen = QApplication.primaryScreen().geometry()
        self.max_height = int(screen.height() * 0.8)
        self.max_width = int(screen.width() * 0.3)
        self.setGeometry(0, screen.height() - 300, 400, 300)
        self.show()

    def update_challenges(self, challenges):
        for i in reversed(range(self.scroll_layout.count() - 1)):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for category, challenge in challenges.items():
            challenge_widget = ChallengeWidget(category, challenge)
            self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, challenge_widget)

        QTimer.singleShot(0, self.adjust_size)

    def adjust_size(self):
        content_size = self.scroll_content.sizeHint()
        margins = self.central_widget.layout().contentsMargins()
        ideal_width = content_size.width() + margins.left() + margins.right()
        ideal_height = content_size.height() + margins.top() + margins.bottom()

        new_width = min(ideal_width, self.max_width)
        new_height = min(ideal_height, self.max_height)
        new_width = max(new_width, 300)
        new_height = max(new_height, 100)

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, screen.height() - new_height, new_width, new_height)

        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded if ideal_height > new_height else Qt.ScrollBarAlwaysOff
        )
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAsNeeded if ideal_width > new_width else Qt.ScrollBarAlwaysOff
        )
        self.update()

    def hideEvent(self, event):
        super().hideEvent(event)
        self.hotkey_hint.setVisible(True)

    def showEvent(self, event):
        super().showEvent(event)
        self.hotkey_hint.setVisible(True)