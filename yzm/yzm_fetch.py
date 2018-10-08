# -*- coding:utf-8 -*-
import requests,time
# 文件下载，主要下载训练集


def download_pics(pic_name):
    url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    res = requests.get(url, stream=True)
    with open('yzm_data/%s.jpg' % (pic_name), 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()


if __name__ == '__main__':
    for i in range(100):
        pic_name = int(time.time() * 1000000)
        download_pics(pic_name)
