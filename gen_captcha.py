from captcha.image import ImageCaptcha
import os
import random
import time
import sys
from ALL_NEED import *



def gen_cptcha_text():
    text = ""
    for j in range(char_count):
        text += random.choice(characters)
    timestamp = str(time.time()).replace(".", "")
    path = os.path.join(root_dir, "{}_{}.{}".format(text, timestamp, image_suffix))
    return text, path


def gen_special_img(text, file_path):
    generator = ImageCaptcha(width=width, height=height)
    img = generator.generate_image(text)
    img.save(file_path)


if __name__ == '__main__':
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    for i in range(5000):
        captcha_text, path = gen_cptcha_text()
        gen_special_img(captcha_text, path)


def stdout_flush():
    if i % 100 == 0:
        percent = float(i) * 100 / float(1000)
    percent = float(i) * 100 / float(1000)
    sys.stdout.write("%f" % percent)
    sys.stdout.write("%\r\n")
    sys.stdout.flush()
    sys.stdout.write("100%!finish!\r\n")
    sys.stdout.flush()

