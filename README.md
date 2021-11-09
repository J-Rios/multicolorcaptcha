# multicolorcaptcha
Python random image-captcha generator library.

## Installation
To generate the images of the Captchas, the library uses Pillow module.
- For Linux systems, it is necessary to install Pillow prerequisites (also, Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL):
```bash
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
```

- Install the module
```bash
pip3 install multicolorcaptcha
```

## API Usage
```py
from multicolorcaptcha import CaptchaGenerator

# Captcha image size number (2 -> 640x360)
CAPCTHA_SIZE_NUM = 2

# Create Captcha Generator object of specified size
generator = CaptchaGenerator(CAPCTHA_SIZE_NUM)

# Generate a captcha image
captcha = generator.gen_captcha_image(difficult_level=3)
math_captcha = generator.gen_math_captcha_image(difficult_level=2)

# Get information of standard captcha
image = captcha.image
characters = captcha.characters

# Get information of math captcha
math_image = math_captcha.image
math_equation_string = math_captcha.equation_str
math_equation_result = math_captcha.equation_result

# Save the images to files
image.save("captcha.png", "png")
math_image.save("captcha.png", "png")
```

## Generated Captchas Examples

### Monocolor Background Captchas
![Monocolor Captcha](https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Monocolor_Background.png)

### Multicolor Background Captchas
![Multicolor Captcha](https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Multicolor_Background.png)

### ASCII Captchas
![Multicolor Captcha](https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Ascii.png)

### Modificable Difficult Level Captchas
![Multicolor Captcha](https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Max_Complex.png)

### Math Equation Captchas
![Math Captcha](https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Math.png)
