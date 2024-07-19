from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter


class ChallengeWidget(QWidget):
    def __init__(self, category, challenge, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 15)
        layout.setSpacing(20)

        self.icon_label = QLabel(self)
        self.icon_label.setFixedSize(24, 24)
        self.set_icon(category)
        layout.addWidget(self.icon_label)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)

        self.name_label = QLabel(challenge.name, self)
        self.name_label.setStyleSheet("color: #ff4654; font-size: 16px; font-weight: bold;")
        text_layout.addWidget(self.name_label)

        self.desc_label = QLabel(challenge.description, self)
        self.desc_label.setStyleSheet("color: white; font-size: 14px;")
        self.desc_label.setWordWrap(True)
        text_layout.addWidget(self.desc_label)

        layout.addLayout(text_layout, 1)

    def set_icon(self, category):
        icon_pixmap = QPixmap(f"assets/{category}.png")
        if not icon_pixmap.isNull():
            white_pixmap = QPixmap(icon_pixmap.size())
            white_pixmap.fill(Qt.transparent)
            painter = QPainter(white_pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_Source)
            painter.drawPixmap(0, 0, icon_pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            painter.fillRect(white_pixmap.rect(), Qt.white)
            painter.end()
            self.icon_label.setPixmap(white_pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            print(f"Failed to load icon for category: {category}")
