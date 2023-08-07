from src.json_reader import JsonReader
from src.image_generator import ImageGenerator
from src.overlay.overlay import Overlay
from src.overlay.overlay_controller import OverlayController
from src.randomizer import Randomizer


class Application:
    def __init__(self):
        self._json_reader = JsonReader("valorant_challenges.json")
        self._randomizer = Randomizer(min_challenges=2, max_challenges=3)
        self._image_generator = ImageGenerator()
        self._categories = self._json_reader.get_categories()

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
        image_path = self._generate_image()
        self.overlay.update_image(image_path)

    def finish_app(self):
        self.overlay.quit()

    def _generate_image(self) -> str:
        random_categories = self._randomizer.get_random_challenges(self._categories)
        image = self._image_generator.generate_random_challenges_image(random_categories)
        file_name = "random_challenges.png"
        self._image_generator.save_image(image, file_name)
        return file_name
