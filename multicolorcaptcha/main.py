#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####################################################################################################

from generator import CaptchaGenerator
from os import path, makedirs

####################################################################################################

# Path to generate Captchas
GEN_CAPTCHAS_FOLDER = "./captchas"

# Captcha image size number (2 -> 640x360)
CAPCTHA_SIZE_NUM = 2

####################################################################################################

def gen_captchas(CaptchaGen, num_captchas, out_img_dir):
    '''Generate num_captchas captchas and store in out_img_dir directory.'''
    for i in range(0, num_captchas):
        # Use one of the following captcha generation options
        #captcha = CaptchaGen.gen_captcha_image()
        #captcha = CaptchaGen.gen_captcha_image(multicolor=False, margin=False)
        #captcha = CaptchaGen.gen_captcha_image(multicolor=True, margin=False)
        #captcha = CaptchaGen.gen_captcha_image(multicolor=True, margin=True)
        captcha = CaptchaGen.gen_captcha_image(difficult_level=2)
        #captcha = CaptchaGen.gen_captcha_image(difficult_level=4)
        #captcha = CaptchaGen.gen_captcha_image(chars_mode="hex")
        #captcha = CaptchaGen.gen_captcha_image(chars_mode="ascii")
        #captcha = CaptchaGen.gen_captcha_image(difficult_level=5, multicolor=True, \
        #        chars_mode="ascii")
        image = captcha["image"]
        characters = captcha["characters"]
        print("Generated captcha {}: {}".format(str(i+1), characters))
        image.save("{}/{}.png".format(out_img_dir, str(i+1)), "png")


def gen_math_captchas(CaptchaGen, num_captchas, out_img_dir):
    '''Generate num_captchas math captchas and store in out_img_dir directory.'''
    for i in range(0, num_captchas):
        # Use one of the following captcha generation options
        captcha = CaptchaGen.gen_math_captcha_image(2)
        #captcha = CaptchaGen.gen_math_captcha_image(2, multicolor=True)
        image = captcha["image"]
        equation_str = captcha["equation_str"]
        equation_result = captcha["equation_result"]
        print("Generated captcha {}: {} = {}".format(str(i+1), equation_str, equation_result))
        image.save("{}/{}.png".format(out_img_dir, str(i+1)), "png")

# Main Function #

def demo():
    '''Main Function'''
    # Create Captcha Generator object of specified size
    CaptchaGen = CaptchaGenerator(CAPCTHA_SIZE_NUM)
    # If it doesn't exists, create captchas folder to store generated captchas
    if not path.exists(GEN_CAPTCHAS_FOLDER):
        makedirs(GEN_CAPTCHAS_FOLDER)
    # Generate 20 captchas
    gen_captchas(CaptchaGen, 20, GEN_CAPTCHAS_FOLDER)
    #gen_math_captchas(CaptchaGen, 20, GEN_CAPTCHAS_FOLDER)    
    print("Process completed. Check captchas images at \"{}\" folder.".format(GEN_CAPTCHAS_FOLDER))


if __name__ == '__main__':
    demo()
