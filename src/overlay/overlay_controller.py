import time

import keyboard
import threading


class OverlayController:
    def __init__(self, app):
        self.app = app
        hotkey_thread = threading.Thread(target=self._handle_hotkeys)
        hotkey_thread.daemon = True  # Ensure thread exits when main program exits
        hotkey_thread.start()

    def _handle_hotkeys(self):
        while True:
            if keyboard.is_pressed('F7'):
                if self.app.overlay_visible:
                    self.app.hide_overlay()
                else:
                    self.app.show_overlay()
                time.sleep(0.3)
            elif keyboard.is_pressed('F8'):
                self.app.update_overlay()
            elif keyboard.is_pressed('F10'):
                self.app.finish_app()
                break
