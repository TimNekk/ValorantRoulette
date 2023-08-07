from dataclasses import dataclass


@dataclass
class Settings:
    challenges_json_path: str
    min_challenges: int
    max_challenges: int
