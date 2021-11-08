from dataclasses import dataclass
from typing import Any


@dataclass
class RGBModal:
    R: int
    G: int
    B: int

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    @property
    def color(self) -> str:
        return f"rgb({self.R}, {self.G}, {self.B})"
