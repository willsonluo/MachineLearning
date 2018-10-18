import requests,os,time,cv2
from PIL import Image


def yzm_download(down_url):
  #  url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
    res = requests.get(down_url, stream=True)
    with open('yzm_download'+os.sep+str(int(time.time() * 1000000))+'.jpg', 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    #    f.close()
    return

def yzm_clean(yzm_file):
    # print(os.getcwd())
    img = cv2.imread(yzm_file, 0)  # 直接读为灰度图像
    ret, thresh1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    cv2.imwrite(yzm_file, thresh1)
    return

def yzm_split(yzm_file):
    img = Image.open(yzm_file)
    im = img.convert("L")
    split_lines = [4, 18, 32, 46, 60]
    y_min = 1
    y_max = 23
    for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
        im.crop([x_min, y_min, x_max, y_max]).save(
                'yzm_split' + os.sep + str('zz_')+str(int(time.time() * 1000000))+'.jpg',
                'jpeg')  # (str(c)+'.jpg')
    return

# url = 'https://app.singlewindow.cn/cas/plat_cas_verifycode_gen'
# for i in range(20):
#     yzm_download(url)

#
# captcha = os.listdir('yzm_download')
# for i in range(len(captcha)):
#     yzm_split('yzm_download'+os.sep+captcha[i])