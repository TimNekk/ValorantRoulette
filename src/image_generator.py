import textwrap

from PIL import Image, ImageDraw, ImageFont, ImageOps

from src.models import Challenge


class ImageGenerator:
    _REGULAR_FONT_NAME = "arial.ttf"
    _HEADING_FONT_NAME = "arialbd.ttf"

    def __init__(self) -> None:
        self._load_fonts()

    def _load_fonts(self) -> None:
        try:
            self._giant_font = ImageFont.truetype(self._REGULAR_FONT_NAME, size=48)
            self._regular_font = ImageFont.truetype(self._REGULAR_FONT_NAME, size=18)
            self._heading_font = ImageFont.truetype(self._HEADING_FONT_NAME, size=28)
            self._small_font = ImageFont.truetype(self._REGULAR_FONT_NAME, size=12)
        except IOError:
            self._giant_font = ImageFont.load_default()
            self._regular_font = ImageFont.load_default()
            self._heading_font = ImageFont.load_default()
            self._small_font = ImageFont.load_default()

    @staticmethod
    def _draw_text(draw, position, text, font, fill = "white"):
        draw.text(position, text, font=font, fill=fill)

    @staticmethod
    def _draw_icon(image, icon_pos, icon_path) -> Image:
        icon = Image.open(icon_path).convert('RGBA')
        icon = icon.resize((40, 40))
        # Make content white and keep transparency
        alpha = icon.split()[3]
        white_content = ImageOps.colorize(icon.convert('L'), '#FFF', '#FFF')
        icon = Image.merge('RGBA', (*white_content.split(), alpha))
        image.paste(icon, icon_pos, icon)
        return icon

    @staticmethod
    def save_image(image: Image, path: str) -> None:
        image.save(path, format="PNG")

    def generate_random_challenges_image(self, random_challenges: dict[str, Challenge]) -> Image:
        if not random_challenges:
            print("No challenges available.")
            return

        line_height = 20  # Adjust as needed
        image_width = 600

        # Calculate image height based on content
        image_height = 100
        for challenge in random_challenges.values():
            wrapped_description = textwrap.fill(challenge.description, width=40)  # Adjust the width as needed
            description_lines = wrapped_description.split('\n')
            image_height += 120 + len(description_lines) * line_height

        image = Image.new('RGB', (image_width, image_height), color=(17, 17, 17))
        draw = ImageDraw.Draw(image)

        offset = 30

        self._draw_text(draw, (40, 10), "Валорант Рулетка", font=self._giant_font, fill=(60, 60, 60))

        y_position = 70
        for i, (category_name, challenge) in enumerate(random_challenges.items()):
            icon_pos = (60, y_position + offset)
            icon_path = f"assets/{category_name}.png"
            icon = self._draw_icon(image, icon_pos, icon_path)

            text_bbox = draw.textbbox(icon_pos, category_name, font=self._small_font)
            text_width = text_bbox[2] - text_bbox[0]
            text_pos = (icon_pos[0] + (icon.size[0] - text_width) // 2, icon_pos[1] + icon.size[1] + 5)
            self._draw_text(draw, text_pos, category_name, font=self._small_font, fill="white")

            self._draw_text(draw, (160, y_position + offset), challenge.name if challenge.name else 'N/A',
                            font=self._heading_font, fill=(255, 70, 85))

            wrapped_description = textwrap.fill(challenge.description, width=40)  # Adjust the width as needed
            description_lines = wrapped_description.split('\n')

            for j, line in enumerate(description_lines):
                self._draw_text(draw, (160, y_position + 35 + offset + j * line_height), line, font=self._regular_font,
                                fill="white")

            y_position += 120 + len(description_lines) * line_height

        return image
