import json

from src.models import Challenge, Category
from src.models.settings import Settings


class JsonReader:
    @staticmethod
    def get_settings(path_to_json) -> Settings:
        with open(path_to_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Settings(**data)

    @staticmethod
    def get_categories(path_to_json) -> list[Category]:
        categories_list = []

        with open(path_to_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            for category_data in data["categories"]:
                category_name = category_data["name"]
                challenges_list = [Challenge(ch["name"], ch["description"]) for ch in category_data["challenges"]]
                category = Category(name=category_name, challenges=challenges_list)
                categories_list.append(category)

        return categories_list
