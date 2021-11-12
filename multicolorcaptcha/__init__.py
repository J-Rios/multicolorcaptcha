from ._generator import CaptchaGenerator
from ._models import (
    RGBModel, CaptchaModel, CaptchaCharModel, MathsCaptchaModel
)


__version__ = "1.2.0"
__description__ = "Python random image-captcha generator library."
__url__ = "https://github.com/J-Rios/multicolorcaptcha"
__author__ = "Jose Miguel Rios Rubio"
__author_email__ = "jrios.github@gmail.com"
__license__ = "GPLv3"


__all__ = [
    "CaptchaGenerator",
    "RGBModel",
    "CaptchaModel",
    "CaptchaCharModel",
    "MathsCaptchaModel"
]
