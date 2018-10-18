# -*- coding:utf-8 -*-
"""
@Time: 2018 Oct 11
@Author: Willson Luo
"""
from yzm_class import *
import base64
import shutil

def download(down_url):
  #  url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    res = requests.get(down_url, stream=True)
    with open('captcha.jpg', 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    #    f.close()
    return


def predict_url(url):
    download(url)
    yzm_clean('captcha.jpg')
    yzm_split('captcha.jpg')
    yzm_word = [abc for abc in os.listdir('yzm_split')]
    words = ''
    for x in range(len(yzm_word)):
        words += yzm_rf_pred('yzm_split'+os.sep+yzm_word[x])[0]
        os.remove('yzm_split'+os.sep+yzm_word[x])
    print(words)
    shutil.copy('captcha.jpg','yzm_download' + os.sep + words + "_" + str(int(time.time() * 1000000)) + '.jpg')
    return(words)


def predict_yzm(captcha):
    yzm = base64.b64decode(captcha)
    print(yzm)
    file = open('captcha.jpg', 'wb')
    file.write(yzm)
    file.close()
    yzm_clean('captcha.jpg')
    yzm_split('captcha.jpg')
    yzm_word = [abc for abc in os.listdir('yzm_split')]
    words = ''
    for x in range(len(yzm_word)):
        words += yzm_rf_pred('yzm_split'+os.sep+yzm_word[x])[0]
        os.remove('yzm_split'+os.sep+yzm_word[x])
    print(words)
    shutil.copy('captcha.jpg','yzm_download' + os.sep + words + "_" + str(int(time.time() * 1000000)) + '.jpg')
    return(words)


#if __name__ == '__main__':
    #captcha = base64.b64encode(open('yzm_download/1539575497643336.jpg','rb').read())
    #print(captcha)
    #print(type(captcha))
    #url='https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    #predict_url(url)  # 预测验证码
    #predict_yzm(captcha)