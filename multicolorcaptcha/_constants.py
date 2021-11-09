from os import path

# Constants
SCRIPT_PATH = path.dirname(path.realpath(__file__))
FONTS_PATH = SCRIPT_PATH + "/fonts"

# Captcha with noise (turn it on add delay)
ADD_NOISE = False

# Captcha 16:9 resolution sizes (captcha_size_num -> 0 to 12)
CAPTCHA_SIZE = [(256, 144), (426, 240), (640, 360), (768, 432),
                (800, 450), (848, 480), (960, 540), (1024, 576), (1152, 648),
                (1280, 720), (1366, 768), (1600, 900), (1920, 1080)]

# Font sizes range for each size
FONT_SIZE_RANGE = [(30, 45), (35, 80), (75, 125), (80, 140),
                   (85, 150), (90, 165), (100, 175),
                   (110, 185), (125, 195), (135, 210),
                   (150, 230), (165, 250), (180, 290)]

# Difficult levels captcha generation values
# (<lines in full img>, <circles in full img>)
DIFFICULT_LEVELS_VALUES = [(0, 0), (1, 10), (2, 17), (3, 25), (4, 50), (5, 70)]
