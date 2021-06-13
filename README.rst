multicolorcaptcha
============================

Python random image-captcha generator library.

Installation
------------

To generate the images of the Captchas, the library uses Pillow module.

1. For Linux systems, it is necessary to install Pillow prerequisites (also, Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL):

.. code-block:: bash

   $ apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk

2. Install the module

.. code-block:: bash

   $ pip install multicolorcaptcha

3. Try sample captcha

.. code-block:: bash

   $ multicolorcaptchademo

4. Look at the ``captchas/`` folder.

API Usage
---------

.. code-block:: python

   from multicolorcaptcha import CaptchaGenerator

   # Captcha image size number (2 -> 640x360)
   CAPCTHA_SIZE_NUM = 2

   # Create Captcha Generator object of specified size
   generator = CaptchaGenerator(CAPCTHA_SIZE_NUM)

   # Generate a captcha image
   captcha = generator.gen_captcha_image(difficult_level=3)
   math_captcha = generator.gen_math_captcha_image(difficult_level=2)

   # Get information of standard captcha
   image = captcha["image"]
   characters = captcha["characters"]

   # Get information of math captcha
   math_image = math_captcha["image"]
   math_equation_string = math_captcha["equation_str"]
   math_equation_result = math_captcha["equation_result"]

   # Save the images to files
   image.save("captcha.png", "png")
   math_image.save("captcha.png", "png")

Generated Captchas Examples
---------------------------

Monocolor Background Captchas:

.. image:: https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Monocolor_Background.png
   :alt: Monocolor Captcha

Multicolor Background Captchas:

.. image:: https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Multicolor_Background.png
   :alt: Multicolor Captcha

ASCII Captchas:

.. image:: https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Ascii.png
   :alt: Multicolor Captcha

Modificable Difficult Level Captchas:

.. image:: https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Max_Complex.png
   :alt: Multicolor Captcha

Math Equation Captchas:

.. image:: https://github.com/J-Rios/multicolorcaptcha/raw/master/images/Math.png
   :alt: Math Captcha
