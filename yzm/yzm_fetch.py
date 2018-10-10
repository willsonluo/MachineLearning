# -*- coding:utf-8 -*-
import requests
import time
import os
import cv2
from PIL import Image


def download_pics(pic_name):
    url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    res = requests.get(url, stream=True)
    with open('yzm_data/%s.jpg' % (pic_name), 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()


def clean(image_clean):
    img = cv2.imread(image_clean, 0)  # 直接读为灰度图像
    ret, thresh1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    cv2.imwrite(image_clean, thresh1)


def split():
    img_list = os.listdir('yzm_data')
    print(img_list)
    for abc in range(len(img_list)):
        clean('yzm_data' + os.sep + img_list[abc])
        img = Image.open('yzm_data'+ os.sep + img_list[abc])
        im = img.convert("L")
        split_lines = [4,18,32,46,60]
        y_min = 1
        y_max = 23
        for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
            im.crop([x_min, y_min, x_max, y_max]).save('yzm_test' + os.sep + '000_%s.jpeg' % (int(time.time() * 1000000)),
                                                       'jpeg')  # (str(c)+'.jpeg')


if __name__ == '__main__':
    for i in range(10):
        pic_name = int(time.time() * 1000000)
        download_pics(pic_name)
    split()
