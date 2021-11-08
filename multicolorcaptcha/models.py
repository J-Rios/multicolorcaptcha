from dataclasses import dataclass
from typing import Any


class Extended:
    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)


@dataclass
class RGBModal(Extended):
    R: int
    G: int
    B: int

    @property
    def color(self) -> str:
        return f"rgb({self.R}, {self.G}, {self.B})"
