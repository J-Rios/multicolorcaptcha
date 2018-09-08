# coding: utf-8

####################################################################################################

from img_captcha_gen import CaptchaGenerator
from os import path, makedirs

####################################################################################################

# Captcha image height
CAPCTHA_SIZE = (160, 160)

####################################################################################################

# Main Function #

def main():
    '''Main Function'''
    # Create Captcha Generator object of specified size
    CaptchaGen = CaptchaGenerator(CAPCTHA_SIZE)
    # If it doesn't exists, create captchas folder to store generated captchas
    if not path.exists("./captchas"):
        makedirs("./captchas")
    # Generate 100 captchas
    for i in range(0, 100):
        image = CaptchaGen.gen_captcha_image(True) # Remove True to generate one color background
        image.save("./captchas/{}.png".format(str(i)), "png")


if __name__ == '__main__':
    main()
