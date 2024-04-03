from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class MyModel:
    name: str
    age: int

    @property
    def birth_year_estimate(self):
        return datetime.now(UTC).year - self.age

    def __str__(self):
        return f"{self.name} ({self.birth_year_estimate})"
