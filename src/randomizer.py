import random
from typing import List

from src.models import Challenge, Category


class Randomizer:
    def __init__(self, min_challenges: int = 2, max_challenges: int = 3) -> None:
        self._min_challenges = min_challenges
        self._max_challenges = max_challenges

    def get_random_challenges(self, categories: List[Category]) -> dict[str, Challenge]:
        random_challenges_dict = {}
        selected_categories = random.sample(categories, k=random.randint(self._min_challenges, self._max_challenges))

        for category in selected_categories:
            if category.challenges:
                challenge = random.choice(category.challenges)
                random_challenges_dict[category.name] = challenge

        return random_challenges_dict
