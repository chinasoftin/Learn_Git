import numpy as np


# 把彩色图像转为灰度图像（色彩对识别验证码没有什么用）
def convert2gray(img):
    if len(img.shape) > 2:
        gray = np.mean(img, -1)
        # 上面的转法较快，正规转法如下
        # r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img


def text2vec(self, text):
    """
    转标签为oneHot编码
    :param text: str
    :return: numpy.array
    """
    text_len = len(text)
    # if text_len > self.max_captcha:
    if text_len > 4:
        raise ValueError('验证码最长{}个字符'.format(self.max_captcha))
    vector = np.zeros(self.max_captcha * self.char_set_len)
    for i, ch in enumerate(text):
        idx = i * self.char_set_len + self.char_set.index(ch)
        vector[idx] = 1
    return vector

