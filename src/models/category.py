from dataclasses import dataclass
from typing import List

from src.models import Challenge


@dataclass
class Category:
    name: str
    challenges: List[Challenge]
