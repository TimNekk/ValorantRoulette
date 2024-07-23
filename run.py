from src.app import Application


try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'timnekk.valorant-roulette.desktop-app.2.1.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


def main():
    app = Application(settings_json_path="settings.json")
    app.run()


if __name__ == "__main__":
    main()
