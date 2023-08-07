import json

from src.models import Challenge, Category


class JsonReader:
    def __init__(self, path_to_json: str):
        self._path_to_json = path_to_json

    def get_categories(self) -> list[Category]:
        categories_list = []

        with open(self._path_to_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            for category_data in data["categories"]:
                category_name = category_data["name"]
                challenges_list = [Challenge(ch["name"], ch["description"]) for ch in category_data["challenges"]]
                category = Category(name=category_name, challenges=challenges_list)
                categories_list.append(category)

        return categories_list
