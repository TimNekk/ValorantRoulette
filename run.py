from src.app import Application


def main():
    app = Application(settings_json_path="settings.json")
    app.run()


if __name__ == "__main__":
    main()
