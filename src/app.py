from PIL import Image

from src.json_reader import JsonReader
from src.image_generator import ImageGenerator
from src.overlay.overlay import Overlay
from src.overlay.overlay_controller import OverlayController
from src.randomizer import Randomizer


class Application:
    def __init__(self, settings_json_path: str) -> None:
        self._settings = JsonReader.get_settings(settings_json_path)
        self._randomizer = Randomizer(min_challenges=self._settings.min_challenges,
                                      max_challenges=self._settings.max_challenges)
        self._image_generator = ImageGenerator()
        self._categories = JsonReader.get_categories(self._settings.challenges_json_path)

        self.overlay = Overlay(self._generate_image())
        self.overlay_visible = True
        self.controller = OverlayController(self)

    def run(self):
        self.overlay.mainloop()

    def show_overlay(self):
        self.overlay_visible = True
        self.overlay.deiconify()

    def hide_overlay(self):
        self.overlay_visible = False
        self.overlay.withdraw()

    def update_overlay(self):
        image = self._generate_image()
        self.overlay.update_image(image)

    def finish_app(self):
        self.overlay.destroy()

    def _generate_image(self) -> Image:
        random_categories = self._randomizer.get_random_challenges(self._categories)
        return self._image_generator.generate_random_challenges_image(random_categories)
