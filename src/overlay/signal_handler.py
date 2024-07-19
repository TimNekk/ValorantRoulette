from PyQt5.QtCore import QObject, pyqtSignal


class SignalHandler(QObject):
    refresh_signal = pyqtSignal()
    toggle_visibility_signal = pyqtSignal()
    close_signal = pyqtSignal()
