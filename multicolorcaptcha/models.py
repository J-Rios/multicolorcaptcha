from dataclasses import dataclass
from typing import Any
from PIL import Image


class __Extended:
    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)


@dataclass
class RGBModel(__Extended):
    R: int
    G: int
    B: int

    @property
    def color(self) -> str:
        return f"rgb({self.R}, {self.G}, {self.B})"


@dataclass
class CaptchaModel(__Extended):
    image: Image.Image
    character: str
