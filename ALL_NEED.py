

root_dir = "D:/Python_Captcha/"

image_suffix = "png"
# characters = "0123456789"
characters = "0123456789abcdefghijklmnopqrstuvwxyz"
count = 100
char_count = 4
width = 100
height = 60

from easydict import EasyDict
import os
import json
sample_conf = EasyDict()

# 图片文件夹
sample_conf.origin_image_dir = "D:/Python_Captcha/"
sample_conf.train_image_dir = "D:/captch_pic/sample/train/"
sample_conf.test_image_dir = "D:/captch_pic/sample/test/"
sample_conf.api_image_dir = "D:/captch_pic/sample/api/"
sample_conf.online_image_dir = "D:/captch_pic/sample/online/"
sample_conf.local_image_dir = "D:/captch_pic/sample/local/"

# 模型文件夹
sample_conf.model_save_dir = "D:/captch_pic/model/"

# 图片相关参数
sample_conf.image_width = 100
sample_conf.image_height = 60
sample_conf.max_captcha = 4
sample_conf.image_suffix = "png"

# 验证码字符相关参数
sample_conf.char_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# char_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# char_set = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

use_labels_json_file = True
if use_labels_json_file:
    if os.path.exists("gen_image/labels.json"):
        with open("gen_image/labels.json", "r") as f:
            content = f.read()
            if content:
                sample_conf.char_set = json.loads(content)
            else:
                pass
    else:
        pass

sample_conf.remote_url = "https://www.xxxxx.com/getImg"